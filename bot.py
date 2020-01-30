# bot.py

import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

description = '''Your M64 away from M64'''
bot = commands.Bot(command_prefix='!', description=description)
 
@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
        
# bot commands
@bot.command()
async def hello(ctx):
    """Says world"""
    await ctx.send("world")


@bot.command()
async def add(ctx, left : int, right : int):
    """Adds two numbers together."""
    await ctx.send(left + right)

# bot events
@bot.event
async def on_message(message):
    if ("foo" in message.content) and (message.author.bot == False):
        await message.channel.send("foo to you too")
    await bot.process_commands(message)
    
@bot.event
async def on_message(message):
    if ("owo" in message.content) and (message.author.bot == False):
        await message.channel.send("don't you freaking owo me")
    await bot.process_commands(message)
    


bot.run(TOKEN)
