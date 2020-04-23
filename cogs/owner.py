# owner.py 

import discord
from discord.ext import commands

class Owner(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    # commands 
    @commands.command()
    @commands.is_owner()
    async def log(self, ctx, *, args):
        """Writes arguments to log.txt"""
    
        #write to file 
       
        try: 
            f = open("log.txt", "a")
            f.write("\n")
            f.write(args)
        except IOError:
            await ctx.author.send("IOError")
        finally:
            f.close()

        #send what was written
        await ctx.author.send('Wrote {}'.format(args))

    @commands.command()
    @commands.is_owner()
    async def orderPizza(self, ctx):
        """Orders pizza from Dominos?"""
        await ctx.author.send("This is not finished yet. Check back later!")

    @commands.command()
    @commands.is_owner()
    async def read(self, ctx):
        """Reads contents of log.txt"""
        await ctx.author.send('Still working!')
        try:
            f = open("log.txt", "r")
            await ctx.author.send(f.read())
        except IOError:
            await ctx.author.send("IOError")
        finally: 
            f.close()

    
