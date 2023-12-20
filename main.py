from ossapi import Ossapi, UserLookupKey, GameMode, RankingType, ScoringType, ScoreType
import discord
from discord.ext import commands, tasks
import certifi 

import json 
import os 

if os.path.exists(os.getcwd() + "/config.json"):
    
    with open("./config.json") as f:
        configData = json.load(f)

else: 
    configTemplate = {"Token": "", "Prefix": "!", "client_secret": ""}
    
    with open(os.getcwd() + "/config.json", "w+") as f: 
        json.dump(configTemplate, f)

token = configData["Token"]
prefix = configData["Prefix"]
client_secret = configData["Client_secret"]


from apscheduler.schedulers.asyncio import AsyncIOScheduler
from datetime import datetime, time
# import interactions

os.environ["SSL_CERT_FILE"] = certifi.where()

client_id = 28923



api = Ossapi(client_id, client_secret)




top50 = api.ranking(GameMode.OSU, RankingType.PERFORMANCE)

top50 = api.ranking("osu", "performance")


usscore = api.user_scores(29312082, ScoreType.BEST)

best_map = usscore[0].beatmap.url

first_user_score = usscore[0].pp










# Discord integration 

intents = discord.Intents.all()

bot = commands.Bot(command_prefix='!', intents=intents)
scheduler = AsyncIOScheduler() 

@bot.command()
async def topscorer(ctx):
    # Replace with actual method to fetch top scorer from Osu! API
   
    # Format the data in a user-friendly way
    response = (f"Top 25: {top50.ranking[0].user.username}")
    await ctx.send(response)
@bot.command()
async def mybest(ctx):
   
    response = (f"Your top score is: {first_user_score} pp on {best_map}")
    await ctx.send(response)


bot.run(token)


