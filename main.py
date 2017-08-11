# _*_ coding: utf-8 _*_

from config import config
import feedparser
import telebot
import json
import re
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
    image_url = re.search('src=".*"', content)

    if image_url:
        image_url = image_url.group(0).strip('"').strip('src="')

    brpos = content.index(d)
    text = content[brpos+len(d):].replace('{}{}'.format(d,d), '\n').replace(d, '\n')
    post = {}
    if image_url:
        post['image'] = image_url
    post['text'] = text
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
