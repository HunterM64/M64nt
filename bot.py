# bot.py

import os
import discord
import datetime
from discord.ext import commands
from dotenv import load_dotenv
from cogs import owner

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
owner_id = os.getenv('OWNER_ID')

start_time = datetime.datetime.utcnow() # Timestamp of when bot came online

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
  
# @bot.command()
# async def orderPizza(ctx):
#     """Orders pizza from Dominos?"""
#     await ctx.author.send("This is not finished yet. Check back later!")

@bot.command()
async def wsl(ctx):
    """Did you know about WSL?"""
    await ctx.send("Did you know WSL lets you use a Bash terminal on Windows? Epic!")
                              
@bot.command()
async def uptime(ctx):
    """Shows bot uptime"""
    now = datetime.datetime.utcnow() #Timestamp of when uptime function is run
    delta = now - start_time
    hours, remainder = divmod(int(delta.total_seconds()), 3600)
    minutes, seconds = divmod(remainder, 60)
    days, hours = divmod(hours, 24)
    if days:
        time_format = "**{d}** days, **{h}** hours, **{m}** minutes, and **{s}** seconds."
    else:
        time_format = "**{h}** hours, **{m}** minutes, and **{s}** seconds."
    uptime_stamp = time_format.format(d=days, h=hours, m=minutes, s=seconds)
    await ctx.send("I have been up for {}".format(uptime_stamp))

# @bot.command()
# @commands.is_owner()
# async def log(ctx, *, args):
    
#     #write to file 
#     f = open("log.txt", "a")
#     f.write("\n")
#     f.write(args)
#     f.close()

#     #send what was written
#     await ctx.author.send('Wrote {}'.format(args))


# bot events
@bot.event
async def on_message(message):

    if ("owo" in message.content) and (message.author.bot == False):
        await message.channel.send("don't you freaking owo me")
        
    await bot.process_commands(message)

bot.run(TOKEN)
