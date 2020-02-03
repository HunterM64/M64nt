# bot.py

import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

description = '''Your lord and saviour, M64n't!'''
bot = commands.Bot(command_prefix='!', description=description)
 
@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    
    await bot.change_presence(activity=discord.Game("with your emotions"))
        
# bot commands
@bot.command()
async def hello(ctx):
    """Says world"""
    await ctx.send("world")


@bot.command()
async def add(ctx, left : int, right : int):
    """Adds two numbers together."""
    await ctx.send(left + right)

@bot.command()
async def ping(ctx):
    """Tests bot latency"""
    await ctx.send("pong! {0} ms".format(round(bot.latency, 3) * 1000))

@bot.command()
async def dm(ctx):
    """Sends a DM"""
    await ctx.author.send("whomst has summoned the ancient one?")
  
@bot.command()
async def orderPizza(ctx):
    """Oders pizza from Dominos?"""
    await ctx.author.send("This is not finished yet. Check back later!")
                              
# bot events
@bot.event
async def on_message(message):

    if ("owo" in message.content) and (message.author.bot == False):
        await message.channel.send("don't you freaking owo me")
        
    await bot.process_commands(message)
    


bot.run(TOKEN)
