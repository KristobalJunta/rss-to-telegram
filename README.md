rss-to-telegram

# RSS to Telegram reposter bot

This is a bot to repost given RSS feed to a Telegram channel.

To run it you gotta create your own bot via [BotFather](t.me/botfather) and obtain the token. Then do:
- Clone this repo
- Copy `config.example.py` to `config.py`
- Put all the data there: your token, chat id and feed link. [@getidsbot)](t.me/getidsbot) can help you with getting channel id.

Then run the bot, for example via cron as for it to regularly retrieve new feed items.