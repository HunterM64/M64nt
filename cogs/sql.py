# user.py 

from M64nt.cogs.user import User
import discord
from discord.ext import commands
import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()
USERNAME = os.getenv('USER')
PASSWORD = os.getenv('PASS')

mydb = mysql.connector.connect(
    host="localhost",
    user=USERNAME,
    password=PASSWORD,
    database="m64nt"
)

mycursor = mydb.cursor()

class SQL(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    # commands

    @commands.command()
    @commands.is_owner()
    async def test(self, ctx):
        await ctx.send("this is working.")

    @commands.command()
    @commands.is_owner()
    async def doitraw(self, ctx):
        mycursor.execute("show tables")

        for x in mycursor:
            await ctx.send(x)