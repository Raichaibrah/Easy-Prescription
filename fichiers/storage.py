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
        # Création des métadonnées pour le fichier sur Drive
        file_metadata = {'name': file_name, 'parents': [self.folder_id]}
        media = MediaFileUpload(file_path, resumable=True)
        
        # Téléchargement du fichier
        uploaded_file = self.service.files().create(  # pylint: disable=no-member
            body=file_metadata, media_body=media, fields='id'
        ).execute()

        # Récupération de l'ID du fichier
        file_id = uploaded_file.get('id')
        
        # Rendre le fichier public
        self.make_public(file_id)

        # Retourner l'URL publique du fichier
        return f'https://drive.google.com/uc?id={file_id}'

    def make_public(self, file_id):
        """Rendre un fichier accessible publiquement sur Google Drive"""
        self.service.permissions().create( #pylint: disable=no-member
            fileId=file_id,
            body={
                'role': 'reader',
                'type': 'anyone',
            }
        ).execute()

    def delete_file(self, file_id):
        """Supprimer un fichier de Google Drive"""
        self.service.files().delete(fileId=file_id).execute()  # pylint: disable=no-member
