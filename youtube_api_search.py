import googleapiclient.discovery
import json 
import pandas as pd 

def video_search(max_limit, video_duration, search_keyword, order):

    version = 'v3'
    api_service = 'youtube'
    api_key = ''
    
    final_video_data = {}

    youtube = googleapiclient.discovery.build(api_service, version, developerKey = api_key)
    request = youtube.search().list(
    q= search_keyword, #input the key word search here 
    part="id,snippet",
    type = "video",
    videoDuration = video_duration,
    order = order,
    videoEmbeddable = "true",
    maxResults = max_limit
)
    
    response = request.execute()
    data = json.dumps(response, indent = 3)
    arr = []
    for i in range(max_limit):
        
        new = {}
        new['video_id'] = response['items'][i]['id']["videoId"]
        new['video_title'] = response['items'][i]['snippet']['title']
        new['video_description'] = response['items'][i]['snippet']['description']
        new['video_thumbnail'] = response['items'][i]['snippet']['thumbnails']['high']['url']
        new['video_link'] = 'https://youtu.be/'+response['items'][i]['id']["videoId"]
        
        arr.append(new)
        final_video_data['search_video'+str(i+1)] = new 
    data = json.dumps(final_video_data, indent = 3)
    return response

def convert_data_to_dataframe(limit, duration, key, order):
    
    data = video_search(limit, duration, key, order)
    data_frame = pd.DataFrame.from_dict(data, orient="index", columns=["video_id", "video_title", "video_description", "video_thumbnail", "video_link"])
    return data_frame




