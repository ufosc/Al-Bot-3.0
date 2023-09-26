import os
import contextlib
import asyncio

from interactions import Client, Intents, listen, slash_command, SlashContext
from dotenv import load_dotenv

load_dotenv()  # load the .env file

bot = Client(intents=Intents.DEFAULT)
# intents are what events we want to receive from discord, `DEFAULT` is usually fine


@listen()  # this decorator tells interactions.py that it needs to listen for the corresponding event, and run this coroutine
async def on_ready():
    # This event is called when the bot is ready to respond to commands
    print("Ready")
    print(f"This bot is owned by {bot.owner}")


@slash_command()  # this decorator tells interactions.py to make a slash command with the corresponding name
async def ping(ctx: SlashContext):
    # slash commands are always passed a SlashContext object, used to actually respond to the command
    await ctx.send("Pong!")  # send a message to the channel the command was used in


async def main():
    bot.load_extensions("exts")
    await bot.astart(os.environ["BOT_TOKEN"])

if __name__ == "__main__":
    with contextlib.suppress(KeyboardInterrupt):
        asyncio.run(main())
