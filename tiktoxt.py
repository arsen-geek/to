import selenium
import random as rr
from selenium import webdriver
driver = webdriver.Chrome()
from TikTokApi import TikTokApi
api = TikTokApi.get_instance()

def tiktoxt(hashtag):
    dct = rr.choice(api.by_hashtag(hashtag, count=5))
    link = 'https://www.tiktok.com/@' + dct['author']['id'] + '/video/'
    link += dct['video']['id']
    return link
