class VideoItem:
    title = ""
    desc = ""
    tags = []
    content = ""
    
    def __init__(self, tittle, desc, content, tags) -> None:
        self.title = tittle
        self.desc = desc
        self.content = content
        self.tags = tags
        