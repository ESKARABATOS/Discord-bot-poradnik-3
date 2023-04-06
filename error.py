import discord
from discord.ext import commands


class errory(commands.Cog):

    def __init__(self, client):
        self.clinet = client
    
    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CommandNotFound):
            await ctx.channel.send("Nie ma takiej komendy sprawdz czy wszystko jest poprawne")




def setup(client):
    client.add_cog(errory(client))

    
