# bot.py

import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
from cogs import owner
from cogs import user

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

# bot events
@bot.event
async def on_message(message):

    if ("owo" in message.content) and (message.author.bot == False):
        await message.channel.send("don't you freaking owo me")
        
    await bot.process_commands(message)

# error bot event
@bot.event
async def on_command_error(ctx, error):
    await ctx.send("sorry but" + error)

bot.run(TOKEN)
