# STL
import os
import logging

# PDM
import discord
from dotenv import load_dotenv
from discord.ext import commands

# LOCAL
from perplexibot.cogs.Searchxng import SearchCommands

logging.basicConfig(level=logging.INFO)
LOG = logging.getLogger()


# LOAD ENV
load_dotenv()
token = os.getenv("TOKEN")

intents = discord.Intents.default()
intents.messages = True
intents.message_content = True
bot = commands.Bot(command_prefix="**", intents=intents)

bot.add_cog(SearchCommands(bot))


@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game("Researching"))
    print(f"Logged in as {bot.user}")


assert token
bot.run(token)
