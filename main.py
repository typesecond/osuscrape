from ossapi import Ossapi, UserLookupKey, GameMode, RankingType, ScoringType, ScoreType
import discord
from discord.ext import commands, tasks
import certifi 
import interactions
import json 
import os 

if os.path.exists(os.getcwd() + "/config.json"):
    
    with open("./config.json") as f:
        configData = json.load(f)

else: 
    configTemplate = {"Token": "", "Prefix": "!", "client_secret": "", "Channel_ID": ""}
    
    with open(os.getcwd() + "/config.json", "w+") as f: 
        json.dump(configTemplate, f)

token = configData["Token"]
prefix = configData["Prefix"]
client_secret = configData["client_secret"]
channel_id = configData["channel_id"]




os.environ["SSL_CERT_FILE"] = certifi.where()

client_id = 28923



api = Ossapi(client_id, client_secret)




top= api.ranking(GameMode.OSU, RankingType.PERFORMANCE)

top= api.ranking("osu", "performance")

top25 = api.ranking(GameMode.OSU, RankingType.PERFORMANCE)

top25= api.ranking("osu", "performance")


top25 = [ranking.user.username for ranking in top25.ranking[:25]]


top25 ="\n".join([f"{index}. {username}" for index, username in enumerate(top25, start=1)])
print(top25)









usscore = api.user_scores(29312082, ScoreType.BEST)

best_map = usscore[0].beatmap.url

first_user_score = usscore[0].pp










# Discord integration 

intents = discord.Intents.all()

client = discord.Client(intents=intents)

bot = commands.Bot(command_prefix='!', intents=intents)


bot = interactions.Client(token=token)

@bot.command(
    name="my_first_command",
    description="This is the first command I made!",

)
async def my_first_command(ctx: interactions.CommandContext):
    await ctx.send("Hi there!")

@bot.command(  name="topscorer",
    description="This is the first command I made!",
)
async def topscorer(ctx):
    

    # Replace with actual method to fetch top scorer from Osu! API
   
    # Format the data in a user-friendly way
    response = (f"The king: {top.ranking[0].user.username}")
    await ctx.send(response)
@bot.command(name="mybest",
    description="This is the first command I made!")
async def mybest(ctx):
   
    response = (f"Your top score is: {first_user_score} pp on {best_map}")
    await ctx.send(response)

@bot.command(name="topquarter",
    description="This is the first command I made!")
async def topquarter(ctx):
    
    response = (f"Top 25: {top25}")
    await ctx.send(response)

bot.start()
 
