import discord
from discord.ext import commands
import asyncio
from .config import TOKEN
from .logger import setup_logger

import os

LOG = setup_logger()

intents = discord.Intents.default()
intents.message_content = True
intents.members = True


class AutomationBot(commands.Bot):
    def __init__(self):
        super().__init__(
            command_prefix="!",
            intents=intents
        )

    async def setup_hook(self):
        """Load all cogs automatically"""
        for filename in os.listdir("./bot/cogs"):
            if filename.endswith(".py") and filename != "__init__.py":
                await self.load_extension(f"bot.cogs.{filename[:-3]}")
                LOG.info(f"Loaded cog: {filename}")

    async def on_ready(self):
        LOG.info(f"Logged in as {self.user} (ID: {self.user.id})")
        print("Bot is ready!")


def run_bot():
    bot = AutomationBot()
    bot.run(TOKEN)
