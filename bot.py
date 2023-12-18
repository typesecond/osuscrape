# bot.py
import os

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('MTE4NjExMjgxNTIxMjI2OTY4MA.GfwQtm.sqKn5zEWlTD8xs56yKbMUel5WNk0VwNnj2uZGA')

intents = discord.Intents.all()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to my Discord server!'
    )

client.run('MTE4NjExMjgxNTIxMjI2OTY4MA.GfwQtm.sqKn5zEWlTD8xs56yKbMUel5WNk0VwNnj2uZGA')