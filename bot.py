# bot.py
import os

import discord
from discord.ext import commands
from dotenv import load_dotenv

from discord_slash import SlashCommand # Importing the newly installed library.

load_dotenv()
TOKEN = os.getenv('TOKEN')

intents = discord.Intents.all()
client = discord.Client(intents=intents)

slash = SlashCommand(bot, sync_commands=True)  #
@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to my Discord server!'
    )

client.run('TOKEN')