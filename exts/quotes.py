import os

import aiohttp
import interactions as ipy

class Quotes(ipy.Extension):
    @ipy.slash_command()
    async def random_quote(self, ctx: ipy.SlashContext):
        async with aiohttp.ClientSession() as session:  # create session to make web request
            async with session.get(f"{os.environ['API_URL']}/quote") as resp:  # make web request to api website's quotes
                data = await resp.json()  # get the data from the response - it's a dictionary {"quote": "e", "author": "e"}
                await ctx.send(f"> {data['quote']}\n\\- {data['author']}")  # send it as a message