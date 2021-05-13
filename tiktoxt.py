import random
from TikTokApi import TikTokApi

from selenium import webdriver
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")
browser = webdriver.Chrome(options=chrome_options)

api = TikTokApi.get_instance()
dummylink = 'https://vk.com/katakhma'

def tiktoxt(hashtag):
    try:
        dct = random.choice(api.by_hashtag(hashtag, count=5))
    except AssertionError as error:
        print(error)
        return dummylink
    link = 'https://www.tiktok.com/@' + dct['author']['id'] + '/video/' + dct['video']['id']
    return link

def choose_word(li_words):
    n_list = li_words
    random.shuffle(n_list)
    for word in n_list:
        link = tiktoxt(word)
        if link:
            return link
    return tiktoxt('преисполниться')
