### Description

This program can help you to download videos by using [youtube-dl](https://github.com/ytdl-org/youtube-dl).

Follow the instructions below and simply send links of videos to the bot, and it will download the videos to you computer.

Currently this bot can only be executed on the user's device, but I'm planning to implement this on the Cloud (AWS, Azure, Google Cloud, etc) in the future.

### Instruction

(assuming that you have a Telegram account and is familiar with Telegram)
(I am using WSL in windows 10 with Ubuntu 18.04 LTS, so the pipenv should be done in bash while ngrok is done in cmd. Feel free to use the way you are familiar but be aware of some unexpected behavior.)

- Create a bot, get the token, put it into the config file. (contact BotFather)
- "pipenv install --three python-telegram-bot flask youtube-dl" in bash
- “pipenv run python3 main.py” in bash (Note that the debug option is False.)
- Go ngrok.com and unzip the zip file into the project folder. 
- “ngrok http 5000" in cmd
- ![](https://imgur.com/PqNHlI0.jpg) is your webhook_url (2efb29db part will be different every time)
- Go to https://api.telegram.org/bot{$your_token}/setWebhook?url={$webhook_url}/hook
- Your bot should be active. Go Try it.

### Reference

I took examples in youtube-dl and [this article (Taiwanese Mandarin or Chinese in general](https://medium.com/@zaoldyeck9970/%E5%AF%A6%E6%88%B0%E7%AF%87-%E6%89%93%E9%80%A0%E4%BA%BA%E6%80%A7%E5%8C%96-telegram-bot-ed9bb5b8a6d9) as reference.