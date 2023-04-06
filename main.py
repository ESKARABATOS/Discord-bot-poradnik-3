import discord
import os
from discord.ext import commands


intents=discord.Intents.all()
initents = discord.Intents.default()
initents.members = True

client = commands.Bot(command_prefix=".", intents=intents)


for file in os.listdir("./cogs"):
    if file.endswith(".py"):
        client.load_extension(f'cogs.{file[:-3]}')


client.run("TOKEN")
