# bot.py

import os
import discord
from discord.ext import commands
from discord.ext.commands import CommandNotFound
from dotenv import load_dotenv
from cogs import owner
from cogs import user
from cogs import dnd
import logging

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
owner_id = os.getenv('OWNER_ID')

description = '''Your lord and saviour, M64n't!'''
bot = commands.Bot(command_prefix='!', description=description)
 
@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    
    await bot.change_presence(activity=discord.Game("with your emotions"))

# add cogs
bot.add_cog(owner.Owner(bot))
bot.add_cog(user.User(bot))
bot.add_cog(dnd.DnD(bot))

# bot events
@bot.event
async def on_message(message):
    owo = "owo"
    if (owo.lower in message.content.lower) and (message.author.bot == False):
        await message.channel.send("don't you freaking owo me")

    await bot.process_commands(message)

# functions 

# finds command most similar to command given 
def findSimilarString(inputString):
    returnString = ""
    commands = [ "help", "uptime", "ping", "roll", "mroll" ]
    overlap = 0
    bestOverlap = 0
    bestString = ""

    for testString in commands:

        i = 0
        overlap = 0

        if(len(inputString) < len(testString)):
            while (i < len(inputString)):
                if(inputString[i] == testString[i]):
                    overlap += 1
                i += 1
        else:
            while (i < len(testString)):
                if (inputString[i] == testString[i]):
                    overlap += 1
                i += 1

        if(overlap > bestOverlap):
            bestOverlap = overlap
            bestString = testString
    
    returnString = bestString
    return returnString

# error bot event
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, CommandNotFound):
        await ctx.send("Command not found, did you mean !" + findSimilarString(ctx.message.content[1:]) + "?")
         
    else:
        await ctx.send(error)

bot.run(TOKEN)
