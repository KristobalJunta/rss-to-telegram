rss-to-telegram

# RSS to Telegram reposter bot

This is a bot to repost items from an RSS feed to a Telegram channel.

## Prerequisites

1. Create a new bot via [BotFather](t.me/botfather) and obtain its token.
2. Get the `channel id` of the channel you want the bot to post to ([@getidsbot](t.me/getidsbot) can help you with this).
3. Add your bot to the channel as administrator (permission to create posts is necessary).

## Installation and running

This bot is designed to be run with cron or some other scheduler to regularly retrieve new feed items and post them.
 
The bot uses Python 3.5+. Requirements are listed in the `Pipfile`.

1. Clone this repo.
2. Run `pipenv install` in the project directory.
3. Copy `config.example.py` to `config.py`.
4. Populate the `config.py` with your bot token, channel id and a link to RSS feed.

