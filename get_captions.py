'''
This file is used to get the captions from the video using the youtube API.
A function to get the captions list from a Youtube video,  
with parameters: videoId(string), part=snippet, key=API_KEY
'''
import requests;
from config import API_KEY, API_URL;

def get_captions_list(videoId):
    if videoId is None or not videoId.strip():
        raise ValueError('videoId is required')
    
    url = f'{API_URL}?videoId={videoId}&part=snippet&key={API_KEY}'

    response = requests.get(url)
    if response.status_code != 200:
        raise Exception(f'Error: {response.status_code}')
    
    data = response.json()
    return data

'''
this is the format of response from the API 
{
   "kind":"youtube#captionListResponse",
   "etag":"rdqI3bT-ZO8sghRKnyjvuZ2kKpM",
   "items":[
      {
         "kind":"youtube#caption",
         "etag":"6nlVUOzeG8AqunAI_SPIwCHh5Lg",
         "id":"AUieDabi7MlVfhlOiIeiJdvD3ie8wKBrr1KOXmSklkM_6kZKHFM",
         "snippet":{
            "videoId":"c3qu51WuKHA",
            "lastUpdated":"2022-03-28T06:48:32.112106Z",
            "trackKind":"asr",
            "language":"en",
            "name":"",
            "audioTrackType":"unknown",
            "isCC":false,
            "isLarge":false,
            "isEasyReader":false,
            "isDraft":false,
            "isAutoSynced":false,
            "status":"serving"
         }
      }
   ]
}
'''

def get_captions_id(data):
    if data is None:
        raise ValueError('data is required')
    
    items = data.get('items')
    if len(items) == 0:
        return None
    else:
        return items[0].get('id')
    
'''
this function is used to download the captions by the captions_id
use this URL: https://www.googleapis.com/youtube/v3/captions/{id}
and save the result to a file
'''

def download_captions(captions_id):
    if captions_id is None or not captions_id.strip():
        raise ValueError('captions_id is required')
    
    url = f'{API_URL}/{captions_id}?key={API_KEY}'
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception(f'Error: {response.status_code}')

    return response.text
  

    
    
