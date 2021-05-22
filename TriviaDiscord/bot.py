import discord
from discord.ext import commands

client = commands.Bot(command_prefix=".")

@client.event
async def on_ready():
    print("im ready")

client.run("ODQ1Njg1ODM2NDk0NDA1NjU0.YKkkTw.RYlFkiiqSvrH9wr0_R0YRabP6G0")