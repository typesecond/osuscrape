from ossapi import Ossapi, UserLookupKey, GameMode, RankingType
import discord
from discord.ext import commands, tasks
import certifi 

import json 
import os 

if os.path.exists(os.getcwd() + "/config.json"):
    
    with open("./config.json") as f:
        configData = json.load(f)

else: 
    configTemplate = {"Token": "", "Prefix": "!"}
    
    with open(os.getcwd() + "/config.json", "w+") as f: 
        json.dump(configTemplate, f)

token = configData["Token"]
prefix = configData["Prefix"]

from apscheduler.schedulers.asyncio import AsyncIOScheduler
from datetime import datetime, time
# import interactions

os.environ["SSL_CERT_FILE"] = certifi.where()

client_id = 28923

client_secret = 'pv6WR4HNI4yKlL7vWuvtDx2Owy8qUf2aoNpsT55v'

api = Ossapi(client_id, client_secret)




top50 = api.ranking(GameMode.OSU, RankingType.PERFORMANCE)
# can also use string version of enums
top50 = api.ranking("osu", "performance")


print(top50.ranking[0].user.username)

intents = discord.Intents.all()

bot = commands.Bot(command_prefix='!', intents=intents)
scheduler = AsyncIOScheduler() 

@bot.command()
async def topscorer(ctx):
    # Replace with actual method to fetch top scorer from Osu! API
   
    # Format the data in a user-friendly way
    response = (f"Top 25: {top50.ranking[0].user.username}\n\t\t\t {top50.ranking[1].user.username}")
    await ctx.send(response)


@bot.command()
async def dailypp(ctx): 
    response = (f"Daily leader: {top50.ranking[0].user.username}")
    await ctx.send(response)

async def send_leaderboard():
    channel = bot.get_channel('1186354377745780767')  # Replace with your channel ID
    leaderboard = await dailypp()
    await channel.send(leaderboard)

    # Schedule the task (e.g., everyday at 10 AM)
scheduler.add_job(send_leaderboard, 'cron', hour=12, minute=28, second=1)


scheduler.start()




bot.run(token)


