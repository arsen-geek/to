import random
from selenium import webdriver
from TikTokApi import TikTokApi


def tiktoxt(hashtag):
    driver = webdriver.Chrome()
    api = TikTokApi.get_instance()
    try:
        dct = random.choice(api.by_hashtag(hashtag, count=5))
    except:
        return ''
    link = 'https://www.tiktok.com/@' + dct['author']['id'] + '/video/' + dct['video']['id']
    return link
