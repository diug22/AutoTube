import praw
from praw.models import MoreComments
from core.video_item import VideoItem
from googletrans import Translator

secret = "szbrG5E8ILChg3umSgF1vunNXCxr7g"
client_id = "nUFsTWMjvKSwNhwjxgNAvA"


        
class Reddit_sc:
    reddit : praw.Reddit
    subreddit : str
    submissions = []
    ending = "Dale a like y suscríbete para mas historias como estas"
    video_items = []
    
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
            comments = list(filter(lambda x : len(x.body)>1500 & len(x.body)<2000, raw_comments))
            comments = comments[:5]
            comment_str = []
            comment_num = 0
            
            cooked_title = ""
            
            desc = self.gen_desc(title=title)
            for comment in comments:
                
                comment_num += 1
                cooked_title = title+" parte " + str(comment_num)
                if isinstance(comment.body, str):
                    translated_body = self.translate_text(comment.body)
                    body = self.gen_text(translated_body, title=title)
                    self.video_items.append(VideoItem("Preguntas Reddit Español: " + title, desc=desc, content=body, tags=["", ""]))
                

            
            
    def translate_text(self, text):
        translator = Translator()
        return translator.translate(text=text, src="en", dest="es").text
    
    def gen_desc(self, title):
        return  "#shorts " + title + "\n" + "#redditespañol #askreddit \n Te traigo las respuestas traducidas de este hilo en reddit del foro r/askreddit"
    
    def gen_text(self, body, title):
        return "Preguntas Reddit en español: " + title + " " + body
                
redd = Reddit_sc()
redd.get_subreddits(1)
redd.get_video_texts()