import googleapiclient.discovery as API
import os 

API_KEY = os.environ.get("API_KEY")

youtube = API.build('youtube', 'v3', developerKey = API_KEY)

request = youtube.channels().list(
  part = "statistics", 
  id = 'schafer5'
)

response = request.execute()
print(response)