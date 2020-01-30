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
    
    await bot.change_presence(activity=discord.Game("with your emotions") 
        
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
async def foo(ctx):
    """just testing bot event and command conflicts"""
    await ctx.send("did i pass the test?")

@bot.command()
async def ping(ctx):
    """Tests ping"""
    await ctx.send("pong! {round(bot.latency * 1000)}ms")

@bot.command()
async def dm(ctx):
    """Sends a DM"""
    await ctx.author.send("whomst has summoned the great one?")
                              
# bot events
@bot.event
async def on_message(message):

    if ("owo" in message.content) and (message.author.bot == False):
        await message.channel.send("don't you freaking owo me")

    if ("foo" in message.content) and (message.author.bot == False):
        await message.channel.send("foo to you too!")
        
    await bot.process_commands(message)
    


bot.run(TOKEN)
