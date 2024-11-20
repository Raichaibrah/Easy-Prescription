from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

class GoogleDriveStorage:
    def __init__(self):
        # Chemin vers votre fichier de credentials
        self.credentials_file = 'config/drive_credentials.json'
        self.folder_id = '15N-honTVsCz-qp_JQJ8ac5jQ3NsiPrZu'  # Créez un dossier sur Google Drive et récupérez son ID
        self.credentials = service_account.Credentials.from_service_account_file(
            self.credentials_file, scopes=["https://www.googleapis.com/auth/drive"]
        )
        self.service = build('drive', 'v3', credentials=self.credentials)

    def upload_file(self, file_path, file_name):
        file_metadata = {'name': file_name, 'parents': [self.folder_id]}
        media = MediaFileUpload(file_path, resumable=True)
        uploaded_file = self.service.files().create( #pylint: disable=no-member
            body=file_metadata, media_body=media, fields='id, webContentLink'
        ).execute()
        return uploaded_file.get('webContentLink')  # Retourne le lien accessible

    def delete_file(self, file_id):
        self.service.files().delete(fileId=file_id).execute() #pylint: disable=no-member
