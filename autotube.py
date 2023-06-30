from core.at_io import read_properties_file, read_csv
from core.autovideo import AutoVideo

from tube_selenium.yt_uploader_selenium import Yt_selenium_uploader

from core.video_item import VideoItem

from core.reddit_sc import Reddit_sc

import random

def search_by_tags(file, query): 
    csv = read_csv(file)
    path_list = []
    for video in csv:
        tag_list = str(video[1]).split()
        for word in query:
            if (word in tag_list):
                path_list.append(video[0])
    return path_list
    

session_id = "14590ef73ddd7411b35b519bf6829358"
LOAD_NEW_REDDIT = True


def __main__() :
    config = read_properties_file("./settings.config")
    screen_w = config["screen_width"]
    screen_h = config["screen_heigth"]
    username = config["username"]
    password = config["password"]
    csv = read_csv("quote/imaginemos_1.csv")
    bg_videos = search_by_tags("bg_videos/bg_videos.csv", ["minecraft"])
    
    n_video = 0
    
    client_secret_file = './channels/mental mini challenges/mental_mini_challenges.json'
    scopes = ['https://www.googleapis.com/auth/youtube.upload']
    
    upload_kind = "yt_selenium" #yt_selenium 
    
    if (upload_kind == "yt_api"):
        from core.youtube_uploader import YouTubeUploader
        uploader = YouTubeUploader(client_secret_file, scopes)
    elif (upload_kind == 'yt_selenium'):
        yt_uploader = Yt_selenium_uploader()
        yt_uploader.login(username=username, password=password)
       
    video_items = []
    
    if LOAD_NEW_REDDIT:
        reddit_sc = Reddit_sc()
        reddit_sc.get_subreddits(5)
        reddit_sc.get_video_texts()
        video_items = reddit_sc.video_items
        print(len(video_items))
    else:
        for line in csv:
            print(n_video)
            n_video += 1
            text = line[0]
            title = line[1]
            desc = line[2]
            bg_tags = line[3].split(" ")
            
            video_item = VideoItem(tittle=title, desc=desc,content=text, tags=bg_tags)
            video_items.append(video_item)
        
        
   
        
        
    for video_item in video_items:    
        bg_tags = ["minecraft", "misterio"]
        bg_videos = search_by_tags("bg_videos/bg_videos.csv", bg_tags)
        v1 = AutoVideo(video_item, screen_h, screen_w, "output.mp4", random.choice(bg_videos))
        v1.generate_video()
        
        video_path = './out/output.mp4'
        privacy_status = 'public'  
        
        if (upload_kind == "yt_api"):
            uploader.upload_video(video_path, title, desc, privacy_status)
        elif (upload_kind == 'yt_selenium'):
            if (yt_uploader.upload_video(video_path, video_item.title, video_item.desc)):
                print("upload ok")
            
       
        #uploadVideo(session_id, video_path, title, tags, verbose=True)
            
    

__main__()