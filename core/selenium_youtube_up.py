from Tiktok_uploader import uploadVideo


file = "my_video.mp4"
title = "MY SUPER TITLE"
tags = ["Funny", "Joke", "fyp"]
schedule_time = 1672592400

# Publish the video
uploadVideo(session_id, file, title, tags, verbose=True)

