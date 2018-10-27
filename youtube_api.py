# Sample Python code for user authorization

import os

import google.oauth2.credentials

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google_auth_oauthlib.flow import InstalledAppFlow

# The CLIENT_SECRETS_FILE variable specifies the name of a file that contains
# the OAuth 2.0 information for this application, including its client_id and
# client_secret.
CLIENT_SECRETS_FILE = "client_secret.json"

# This OAuth 2.0 access scope allows for full read/write access to the
# authenticated user's account and requires requests to use an SSL connection.
SCOPES = ['https://www.googleapis.com/auth/youtube.force-ssl']
API_SERVICE_NAME = 'youtube'
API_VERSION = 'v3'
DEVELOPER_KEY='AIzaSyBGnnhNiUHEbNqSZJRvdJHxFaA7Wwl-VPY'

def get_authenticated_service():
  #flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRETS_FILE, SCOPES)
  #credentials = flow.run_console()
  return build(API_SERVICE_NAME, API_VERSION, developerKey=DEVELOPER_KEY)#credentials = credentials)

'''
if __name__ == '__main__':
  # When running locally, disable OAuthlib's HTTPs verification. When
  # running in production *do not* leave this option enabled.
  os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'
  service = get_authenticated_service()
  channels_list_by_username(service,
      part='snippet,contentDetails,statistics',
      forUsername='GoogleDevelopers')
'''

def youtube_search(videoName,youtube):

  # Call the search.list method to retrieve results matching the specified
  # query term.
  search_response = youtube.search().list(
    q=videoName,
    type='video',
    part='id,snippet',
    maxResults=1
  ).execute()

  search_videos = []

  # Merge video ids
  for search_result in search_response.get('items', []):
    search_videos.append(search_result['id']['videoId'])

  os.system('youtube-dl '+'https://www.youtube.com/watch?v='+search_videos[0]+' -x --audio-format mp3 -o "./downloads/%(title)s.%(ext)s"')


def downloadVideos(videoNames):
  os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'
  service = get_authenticated_service()

  try:
    for name in videoNames:
      youtube_search(name,service)
  except HttpError, e:
    print 'An HTTP error %d occurred:\n%s' % (e.resp.status, e.content)
