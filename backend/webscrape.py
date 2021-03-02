from backend.functions import add_video, get_data, check_data
import selenium 
from selenium import webdriver
from bs4 import BeautifulSoup





class FindVideos:
    def __init__(self, channel):
        self.HEADERS = {'User-Agent':
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'}
        self.channel = channel
        
    def openWindow(self):
        self.browser = webdriver.Chrome("C:/Users/home/Downloads/chromedriver_win32/chromedriver.exe")
        self.browser.get(self.url)
        self.soup = BeautifulSoup(self.browser.page_source, 'html.parser')
        
    def get_url(self):
        url = f"https://www.youtube.com/c/{self.channel}/videos"
        self.url = url
        
        
    def scrap_videos(self):
        results = self.soup.find_all('div', {'id': 'items', 'class': 'ytd-grid-renderer'})
        for item in results:
            results = self.item_info(item)
        return results
            
    def item_info(self, item):
        atags = []
        for a in item.find_all('a', href=True):
            atags.append('https://www.youtube.com' + a['href'])
        return atags
        
            
            
    def add_video(self, link):
        add_video(str(link))
    
    def get_data(self):
        data = get_data()
        return data
        
    def check_data(self, input):
        video_list, total = check_data(str(input))
        return video_list, total   
    
    def download_channel(self, links):
        for link in links:
            try:
                self.add_video(str(link))
            except:
                print('Memory Error!')
    
    def start(self):
        self.get_url()
        self.openWindow()
        results = self.scrap_videos()
        self.browser.close()
        self.download_channel(results)