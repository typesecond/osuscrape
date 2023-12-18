from ossapi import Ossapi, UserLookupKey, GameMode, RankingType
from discord.ext import commands
import discord
import requests
from discord import SlashCommand, SlashContext

client_id = 'None'

client_secret = 'None'

api = Ossapi(client_id, client_secret)




top50 = api.ranking(GameMode.OSU, RankingType.PERFORMANCE)
# can also use string version of enums
top50 = api.ranking("osu", "performance")


print(top50.ranking[0].user.username)

intents = discord.Intents.all()

bot = commands.Bot(command_prefix='!', intents=intents)

slash = SlashCommand(bot, sync_commands=True)  #
@bot.command()
async def topscorer(ctx):
    # Replace with actual method to fetch top scorer from Osu! API
   
    # Format the data in a user-friendly way
    response = (f"Top 25: {top50.ranking[0].user.username}")
    await ctx.send(response)


@bot.command()
async def top(ctx):
    
   requests.get("https://osu.ppy.sh/api/v2/users?ids%5B%5D=1") 
   
#response = (f"Your top play: {top.scores_best_count()}")
bot.run('TOKEN')



