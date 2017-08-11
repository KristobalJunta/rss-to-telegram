# _*_ coding: utf-8 _*_

from config import config
from bs4 import BeautifulSoup
import feedparser
import telebot
import json
import os


bot = telebot.TeleBot(config.get('telegram-token'))
feed = feedparser.parse(config.get('feed'))
new_posts = []
d = config.get('delimeter')

if not os.path.exists('posts.json'):
    with open('posts.json', 'w') as f:
        json.dump([], f)
        f.close()

with open('posts.json') as f:
    guids = json.load(f)
    f.close()

for entry in feed.entries:
    content = entry['description']
    post = {}
    soup = BeautifulSoup(content, 'html.parser')
    if soup.img:
        post['image'] = soup.img['src']
    post['text'] = soup.get_text()
    if entry['guid'] not in guids:
        new_posts.append(post)
        guids.append(entry['guid'])

new_posts.reverse()

for post in new_posts:
    bot.send_message(config.get('channel-id'), post.get('text'))
    if post.get('image'):
        bot.send_photo(config.get('channel-id'), post.get('image'))

with open('posts.json', 'w') as f:
    json.dump(guids, f)
    f.close()
