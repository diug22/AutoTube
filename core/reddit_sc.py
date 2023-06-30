import praw
from praw.models import MoreComments
from video_item import VideoItem
from googletrans import Translator

secret = "szbrG5E8ILChg3umSgF1vunNXCxr7g"
client_id = "nUFsTWMjvKSwNhwjxgNAvA"


        
class Reddit_sc:
    reddit : praw.Reddit
    subreddit : str
    submissions = []
    ending = "Dale a like y suscríbete para mas historias como estas"
    
    def __init__(self, secret = "szbrG5E8ILChg3umSgF1vunNXCxr7g", client_id = "nUFsTWMjvKSwNhwjxgNAvA"):
        self.reddit = praw.Reddit(
                        client_id=client_id,
                        client_secret=secret,
                        user_agent="my user agent",
                    )
    
    def get_subreddits(self, limit):
        self.submissions = self.reddit.subreddit("AskReddit").hot(limit=limit)
    
    def get_video_texts(self):
        video_items = []
        for sub in self.submissions:
            title = self.translate_text(sub.title)
            raw_comments : list = filter(lambda x : not isinstance(x, MoreComments), sub.comments)            
            comments = list(filter(lambda x : len(x.body)>500, raw_comments))
            comments = comments[:5]
            comment_str = []
            comment_num = 0
            
            cooked_title = ""
            for comment in comments:
                comment_num += 1
                cooked_title = title+" parte " + str(comment_num)
                translated_body = self.translate_text(comment.body)
                print(translated_body)
                

            
            
    def translate_text(self, text):
        translator = Translator()
        return translator.translate(text=text, src="en", dest="es").text
    
    
                
redd = Reddit_sc()
redd.get_subreddits(1)
redd.get_video_texts()