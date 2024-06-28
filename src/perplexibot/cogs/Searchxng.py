# STL
import logging

# PDM
import discord
from discord.ext import commands
from meta_ai_api import MetaAI

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

        attempts = 1

        while attempts <= 5:
            response = call_research(content)
            attempts += 1

            if len(response) < 1999:
                break
        try:
            await ctx.respond(response)
        except discord.DiscordException as e:
            LOG.error(f"Response was too long (over 2000 tokens): {e}")
            await ctx.respond(
                "Response was too long (over 2000 tokens). Try again.", ephemeral=True
            )

    @search_xng.command(name="meta-search", description="Search using Meta AI")
    @discord.option("content", str, description="Content you want to search.")
    async def meta_search(self, ctx, content: str):
        LOG.debug(f"Recieved ask: {content}")
        meta_ai = MetaAI()
        await ctx.respond("Searching...", ephemeral=True)
        response = meta_ai.prompt(message=content, attempts=3)

        message = response["message"]
        sources = response["sources"]
        links = "\n".join([source["link"] for source in sources])

        LOG.debug(f"Generated Response: {message}")

        bot_response = (
            f"Prompt: {content.strip()}\n"
            "-----------------\n"
            f"{message.strip()}\n\n"
            "Citations\n"
            f"{links.strip()}\n"
        )

        try:
            await ctx.respond(bot_response)
        except discord.DiscordException as e:
            LOG.error(f"Response was too long (over 2000 tokens): {e}")
            await ctx.respond(
                "Response was too long (over 2000 tokens). Try again.", ephemeral=True
            )
