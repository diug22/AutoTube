from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow

class YouTubeUploader:
    def __init__(self, client_secret_file, scopes):
        self.client_secret_file = client_secret_file
        self.scopes = scopes
        self.youtube = self.get_authenticated_service()

    def get_authenticated_service(self):
        flow = InstalledAppFlow.from_client_secrets_file(
            self.client_secret_file, self.scopes)
        credentials = flow.run_local_server(port=0)
        return build('youtube', 'v3', credentials=credentials)

    def upload_video(self, video_path, title, description, privacy_status):
        request_body = {
            'snippet': {
                'title': title,
                'description': "#Shorts " + description,
                'categoryId': '10'
            },
            'status': {
                'privacyStatus': privacy_status
            }
        }

        try:
            insert_request = self.youtube.videos().insert(
                part='snippet,status',
                body=request_body,
                media_body=video_path
            )
            response = insert_request.execute()
            video_id = response['id']
            print('Video uploaded successfully! Video ID:', video_id)
        except HttpError as e:
            print('An HTTP error occurred:', e.content.decode('utf-8'))

# Ejemplo de uso
client_secret_file = './channels/mental mini challenges/mental_mini_challenges.json'
scopes = ['https://www.googleapis.com/auth/youtube.upload']
video_path = './out/test.mp4'
title = 'Título del video'
description = 'Descripción del video'
privacy_status = 'private'  # Puede ser 'private', 'public' o 'unlisted'

uploader = YouTubeUploader(client_secret_file, scopes)
uploader.upload_video(video_path, title, description, privacy_status)