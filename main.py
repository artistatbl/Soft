import tracemalloc
import json
import os
import asyncio
import discord
from discord.ext import commands
from cogs.event import Event
from cogs.music import Music



intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

async def load():
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            await bot.load_extension(f'cogs.{filename[:-3]}')

@bot.event
async def on_ready():
    activity = discord.Activity(name='!help', type=discord.ActivityType.listening)
    await bot.change_presence(status=discord.Status.online, activity=activity)
    guilds = [guild.name for guild in bot.guilds]
    print(f"Connected to {len(guilds)} guilds: {', '.join(guilds)}")
    print(f'{bot.user.name} has connected to Discord!')
    print("---------------------------------------")
    await bot.add_cog(Event(bot))
    await bot.add_cog(Music(bot))

async def main():
    tracemalloc.start()
    await load()
    await bot.start(os.environ["discord_bot_token"])


asyncio.run(main())


 
