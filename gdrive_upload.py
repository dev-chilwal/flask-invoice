from oauth2client.service_account import ServiceAccountCredentials
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials
from googleapiclient.http import MediaFileUpload

# Connect to gdrive
drive_scope = ['https://www.googleapis.com/auth/drive']

creds = ServiceAccountCredentials.from_json_keyfile_name(
    'imposing-water-315811-262f5e8593ca.json', drive_scope)

drive_service = build('drive', 'v3', credentials=creds)


def create_folder(folder, parent_id=['1u8itRD21yYt_JXrFiIv_G0QqRKsgDfod']):
    file_metadata = {
        'name': folder,
        'parents': parent_id,
        'mimeType': 'application/vnd.google-apps.folder'
    }
    file = drive_service.files().create(body=file_metadata,
                                        fields='id').execute()
    grant_permission(file.get('id'))
    return file.get('id')


def find_folder(foldername):
    page_token = None
    response = drive_service.files().list(q="mimeType='application/vnd.google-apps.folder' and name='{}'".format(foldername),
                                          spaces='drive',
                                          fields='nextPageToken, files(id, name)',
                                          pageToken=page_token).execute()
    try:
        if len(response['files']) == 1:
            return response['files'][0]['id']
        else:
            return ""
    except:
        return ""


def callback(request_id, response, exception):
    if exception:
        # Handle error
        print(exception)
    else:
        print("Permission Id: %s" % response.get('id'))


def grant_permission(file_id):

    batch = drive_service.new_batch_http_request(callback=callback)

    domain_permission = {
        'type': 'domain',
        'role': 'writer',
        'domain': 'thepianosa.com'
    }
    batch.add(drive_service.permissions().create(
        fileId=file_id,
        body=domain_permission,
        fields='id',
    ))
    batch.execute()


def upload_to_gdrive(filename, location, folder_id):
    file_metadata = {
        'name': filename,
        'mimeType': 'application/pdf',
        'parents': [folder_id],
    }
    media = MediaFileUpload(location,
                            mimetype='application/pdf',
                            resumable=True)
    file = drive_service.files().create(body=file_metadata,
                                        media_body=media,
                                        fields='id').execute()
    print(file)
