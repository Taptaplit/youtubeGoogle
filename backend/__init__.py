# import speech_recognition as sr
from backend.webscrape import FindVideos
from backend.functions import download_data


# r = sr.Recognizer()

class Backend:
    def __init__(self, channel):
        self.videos = FindVideos(str(channel))
        
    def query(self, input):
        videos, total = self.videos.check_data(input)
        return videos, total
        
    
    def scrape_videos(self):
        self.videos.start()
        
    def get_data(self):
        data = self.videos.get_data()
        return data





        

  
