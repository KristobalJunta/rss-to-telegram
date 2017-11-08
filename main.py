# _*_ coding: utf-8 _*_

from bs4 import BeautifulSoup
from datetime import datetime
from config import config
import feedparser
import telebot
import json
import os


def get_timestamp(dt):
    return datetime.strptime(dt, '%a, %d %b %Y %H:%M:%S %z').timestamp()


bot = telebot.TeleBot(config.get('telegram-token'))

feeds = list()

if type(config.get('feeds')) == str:
    feeds.append(feedparser.parse(config.get('feeds')))
else:
    for feed in config.get('feeds'):
        feeds.append(feedparser.parse(feed))

new_posts = []

if not os.path.exists('posts.json'):
    with open('posts.json', 'w') as f:
        json.dump([], f)
        f.close()

with open('posts.json') as f:
    guids = json.load(f)
    f.close()

for feed in feeds:
    for entry in feed.entries:
        content = entry['description']
        post = {}
        soup = BeautifulSoup(content, 'html.parser')
        if soup.img:
            post['image'] = soup.img['src']
        post['text'] = '\n'.join(soup.stripped_strings)
        post['text'] += '\n\n{}'.format(entry['link'])
        post['date'] = get_timestamp(entry['published'])

        if entry['guid'] not in guids:
            # TODO: strip guid with a regex like /d{4,}\/{?}$/
            new_posts.append(post)
            guids.append(entry['guid'])

new_posts.sort(key=lambda x: x['date'])

for post in new_posts:
    bot.send_message(config.get('channel-id'), post.get('text'))

with open('posts.json', 'w') as f:
    json.dump(guids, f)
    f.close()
