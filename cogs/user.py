# user.py 

import discord
from discord.ext import commands
import datetime
import random

start_time = datetime.datetime.utcnow() # Timestamp of when bot came online

class User(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    # commands

    @commands.command()
    async def ping(self, ctx):
        """Tests bot latency"""
        await ctx.send("pong! {0} ms".format(round(self.bot.latency, 3) * 1000))
                                
    @commands.command()
    async def uptime(self, ctx):
        """Shows bot uptime"""
        now = datetime.datetime.utcnow() # Timestamp of when uptime function is run
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

    @commands.command()
    async def roll(self, ctx, n, x):
        """roll n x: Rolls n dice of x sides"""
        roll = 0
        #i = 0
        for i in range(int(n)):
            rolledNumber = random.randint(1, int(x))
            roll = roll + rolledNumber
        await ctx.send(n + "d" + x + " rolled: " + str(roll))

    @commands.command()
    async def mroll(self, ctx, x, y, z):
        """roll n x: Rolls n dice of x sides"""
        roll = 0
        #i = 0
        for i in range(int(x)):
            rolledNumber = random.randint(1, int(y))
            roll = roll + rolledNumber
        roll = roll + int(z)
        await ctx.send(x + "d" + y + " rolled with modifier " + z + ": " + str(roll))


    # old commands 

    # @commands.command()
    # async def hello(self, ctx):
    #     """Says world"""
    #     await ctx.send("world")

    # @commands.command()
    # async def add(self, ctx, left : int, right : int):
    #     """Adds two numbers together."""
    #     await ctx.send(left + right)

    # @commands.command()
    # async def dm(self, ctx):
    #     """Sends a DM"""
    #     await ctx.author.send("whomst has summoned the ancient one?")

    # @commands.command()
    # async def wsl(self, ctx):
    #     """Did you know about WSL?"""
    #     await ctx.send("Did you know WSL lets you use a Bash terminal on Windows? Epic!")