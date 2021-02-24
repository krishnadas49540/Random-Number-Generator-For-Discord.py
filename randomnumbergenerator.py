import random
import discord
import asyncio
from discord.ext import commands
prefix = "?"
bot = commands.Bot(command_prefix = prefix)
token = 'NzIyMjY2OTM5NzQ5MTcxMjMx.Xuh0ig.GWiHYMesyUFkCE2Y5ZFnAwE8QtI'
@bot.event
async def on_ready():
    print("The bot is ready!")

@bot.command(pass_context = True)
async def randomnumber(ctx):
    embed = discord.Embed(title = "Random Number", description = (random.randint(1, 101)), color = (0xF85252))
    await ctx.send(embed = embed)

bot.run(token)