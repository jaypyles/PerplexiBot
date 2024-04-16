# STL
import logging

# PDM
import discord
from discord.ext import commands

# LOCAL
from perplexibot.utils.AI import call_search, call_research

LOG = logging.getLogger(__name__)


class SearchCommands(commands.Cog):
    def __init__(self, bot) -> None:
        super().__init__()
        self.bot = bot

    search_xng = discord.SlashCommandGroup("search")

    @search_xng.command(name="search", description="Search Anything.")
    async def search(self, ctx, message_content: str):
        await ctx.respond("Searching...", ephemeral=True)
        response = await call_search(message_content)

        data = response.get("data")
        if data:
            form_response = []
            for result in data[:1]:
                formatted_result = (
                    f"Search: {message_content}\n"
                    f"## {result.get('url')}\n"
                    f"```\n{result.get('snippet').strip()}\n```\n"
                )
                form_response.append(formatted_result)

            await ctx.respond("\n".join(form_response))

    @search_xng.command(name="research", description="Search Anything.")
    @discord.option("content", str, description="Content you want to search.")
    async def research(self, ctx, content: str):
        await ctx.respond("Researching...", ephemeral=True)
        response = call_research(content)
        try:
            await ctx.respond(response)
        except discord.DiscordException as e:
            LOG.error(f"Response was too long (over 2000 tokens): {e}")
            await ctx.respond(
                "Response was too long (over 2000 tokens). Try again.", ephemeral=True
            )
