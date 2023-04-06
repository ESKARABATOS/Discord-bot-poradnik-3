import discord
from discord.ext import commands


client = commands.Bot(command_prefix= "!")


class pomocy(commands.Cog):

    def __init__(self, client):
        self.client = client

    @client.command()
    async def pomoc(self, ctx):
        await ctx.channel.send("Cos tam cos tam nie pamientam")

def setup(client):
    client.add_cog(pomocy(client))
