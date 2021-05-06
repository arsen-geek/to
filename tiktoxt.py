import random
from selenium import webdriver
from TikTokApi import TikTokApi


driver = webdriver.Chrome()
api = TikTokApi.get_instance()

    
def tiktoxt(hashtag):
    try:
        dct = random.choice(api.by_hashtag(hashtag, count=5))
    except:
        return ''
    link = 'https://www.tiktok.com/@' + dct['author']['id'] + '/video/' + dct['video']['id']
    return link
