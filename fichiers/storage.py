from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from googleapiclient.errors import HttpError

class GoogleDriveStorage:
    _instance = None
    
    def __init__(self):
        # Chemin vers votre fichier de credentials
        self.credentials_file = 'config/drive_credentials.json'
        self.folder_id = '15N-honTVsCz-qp_JQJ8ac5jQ3NsiPrZu'  # Créez un dossier sur Google Drive et récupérez son ID
        self.credentials = service_account.Credentials.from_service_account_file(
            self.credentials_file, scopes=["https://www.googleapis.com/auth/drive"]
        )
        self.service = build('drive', 'v3', credentials=self.credentials)

    @classmethod
    def get_instance(cls):
        if not cls._instance:
            cls._instance = cls()
        return cls._instance


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

    from googleapiclient.errors import HttpError

    def get_file_id_by_name(self, file_name):
        try:
            # Requête pour chercher le fichier sur Google Drive par son nom
            results = self.service.files().list(  # pylint: disable=no-member
                q=f"name = '{file_name}'",  # Filtrer par nom du fichier
                spaces='drive',
                fields="files(id, name)",  # Récupère uniquement l'ID et le nom du fichier
                pageSize=1  # Nous nous attendons à n'avoir qu'un seul fichier avec ce nom
            ).execute()

            files = results.get('files', [])

            if not files:
                print(f"Aucun fichier trouvé avec le nom : {file_name}")
                return None

            # Retourner l'ID du fichier trouvé
            file_id = files[0]['id']
            print(f"Fichier trouvé : {file_name} (ID : {file_id})")
            return file_id

        except HttpError as error:
            print(f"Erreur lors de la recherche du fichier dans Google Drive : {error}")
            return None
        except Exception as e:
            # Capture de toutes autres erreurs inattendues
            print(f"Une erreur est survenue : {e}")
            return None

    
    
    def delete_file(self, file_id):
        """Supprimer un fichier de Google Drive."""
        try:
            # Tentative de suppression du fichier via l'API Google Drive
            self.service.files().delete(fileId=file_id).execute()
            print(f"Le fichier avec l'ID {file_id} a été supprimé avec succès.")
        except HttpError as error:
            # Gestion des erreurs HTTP, comme un fichier inexistant ou une permission manquante
            print(f"Erreur lors de la suppression du fichier : {error}")
        except Exception as e:
            # Gestion des autres types d'erreurs (ex. problèmes de connexion, API indisponible, etc.)
            print(f"Une erreur est survenue lors de la suppression : {e}")