# user.py 

import discord
from discord.ext import commands
import random

class DnD(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    # commands

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
        """roll x y z: Rolls x dice of y sides and adds z to the total"""
        roll = 0
        #i = 0
        for i in range(int(x)):
            rolledNumber = random.randint(1, int(y))
            roll = roll + rolledNumber
        roll = roll + int(z)
        await ctx.send(x + "d" + y + " rolled with modifier " + z + ": " + str(roll))