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

    brpos = content.index("<br/>")
    text = content[brpos+6:].replace('<br/><br/>', '\n').replace('<br/>', '\n')
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
