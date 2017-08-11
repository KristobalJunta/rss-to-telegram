# _*_ coding: utf-8 _*_

from config import config
import feedparser
import requests
import os
import telebot

bot = telebot.TeleBot(config.get('telegram-token'))
bot.send_message(config.get('channel-id'), "Hello from the bot!")
