import os

import aiohttp
import interactions as ipy

class Quotes(ipy.Extension):
    @ipy.slash_command()
    async def random_quote(self, ctx: ipy.SlashContext):
        async with aiohttp.ClientSession() as session:
            async with session.get(f"{os.environ['API_URL']}/quote") as resp:
                data = await resp.json()
                await ctx.send(f"> {data['quote']}\n\\- {data['author']}")