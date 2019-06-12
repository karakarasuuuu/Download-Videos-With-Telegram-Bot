from __future__ import unicode_literals
import configparser
import logging
import telegram
import youtube_dl
import re
import sys
from flask import Flask, request
from telegram.ext import Dispatcher, MessageHandler, Filters
from subprocess import run

config = configparser.ConfigParser()
config.read('config.ini')

logging.basicConfig(format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s', level = logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)

bot = telegram.Bot(token = (config['TELEGRAM']['ACCESS_TOKEN']))

fail = None
class MyLogger(object):
    def debug(self, msg):
        pass
    def warning(self, msg):
        pass
    def error(self, msg):
        fail = True
        print('Error.')

def my_hook(d):
    if d['status'] == 'finished':
        print('Done.')

ydl_opts = {
    'logger': MyLogger(),
    'progress_hooks': [my_hook],
}

@app.route('/hook', methods = ['POST'])
def webhook_handler():
    if request.method == 'POST':
        update = telegram.Update.de_json(request.get_json(force = True), bot)
        dispatcher.process_update(update)
    return 'ok'

def reply_handler(bot, update):
    text = update.message.text
    try:
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([text])

        if not fail:
            update.message.reply_text(text)
            update.message.reply_text('Downloaded successfully.')
    except:
        update.message.reply_text(text)
        text = "Unexpected error: " + str(sys.exc_info()[0])
        update.message.reply_text(text)

dispatcher = Dispatcher(bot, None)

dispatcher.add_handler(MessageHandler(Filters.text, reply_handler))

if __name__ == '__main__':
    app.run(debug=False)