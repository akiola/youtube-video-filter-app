from flask import Flask, render_template, url_for, request, redirect, json
import youtube_api_search, create_database, search_database


app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def api_and_database():
    if request.method == "POST":
        
        search_key = request.form['key']
        max_limit = int(request.form['limit'])
        filter_by = request.form['filter']
        video_duration = request.form["duration"]
        
        response = youtube_api_search.video_search(max_limit, video_duration, search_key, filter_by)
        
        
        videos = []
        for i in range(max_limit):
            video_data = {
                'id':response['items'][i]['id']['videoId'],
                'url':f"https://www.youtube.com/watch?v={response['items'][i]['id']['videoId']}",
                'thumbnail':response['items'][i]['snippet']['thumbnails']['high']['url'],
                'description':response['items'][i]['snippet']['description'],
                'title':response['items'][i]['snippet']['title']  
            }
            videos.append(video_data)
        
        
        return render_template("index.html", videos = videos)
        
       
    else:
        return render_template("index.html")   
        
if __name__ == "__main__":
    app.run(debug=True)