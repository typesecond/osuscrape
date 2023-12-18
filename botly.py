from discord import commands
from ossapi import * 
bot = commands.Bot(command_prefix='!')

@bot.command()
async def topscorer(ctx):
    # Replace with actual method to fetch top scorer from Osu! API
    top_scorer_data = Ossapi.get_top_scorer()  
    # Format the data in a user-friendly way
    response = f"Top Scorer: {top_scorer_data['username']} with {top_scorer_data['score']} points"
    await ctx.send(response)