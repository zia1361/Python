import requests
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from os.path import basename
API_URL = 'http://127.0.0.1:5000'
with open('video.mp4', 'rb') as fp:
    files = {'file': fp}
    response = requests.post(
    '{}/file-upload'.format(API_URL), files=files
    )

print(response.text) 