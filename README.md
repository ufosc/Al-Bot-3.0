# Al-Bot-3.0

The third attempt at a Discord bot for the UF OSC Discord server. Uses the [UF API Group API](https://github.com/ufosc/UF-API-GROUP) and displays information from it.

## Setting Up

First, follow the instructions from [this guide](https://pythiauf.github.io/Triya-UF-OSC-Docs/guides/python_project.html).

After that, you'll need to make a bot application and add it to a server:
- [Discord.js has a good guide](https://discordjs.guide/preparations/setting-up-a-bot-application.html) on how to make a bot application. Make sure to save the token somewhere!
- [Join the Testing Labs Server for Al Bot](https://discord.gg/TnnezVjrdv) and follow the instructions in #readme to add your bot to the server.

Then, you'll want to create a `.env` file in your base directory. Make it look something like this:
```
BOT_TOKEN="YOUR_BOT_TOKEN"
API_URL="https://uf-api-group.pythiauf.repl.co"
```
(Note: You can change the API URL to any website that's running [the UF API Group API](https://github.com/ufosc/UF-API-GROUP), IE https://localhost:8080. The URL suggested here may also change in the future.)

You should be able to run the bot by running `main.py` after that!
