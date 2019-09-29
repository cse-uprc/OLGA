from sys import path
import os
olgaDir = os.getcwd().replace("Front-End"+os.sep, "")
path.append(olgaDir)
from olga import OLGA, OutputObject
import discord
from discord.ext import commands
import json

client = commands.Bot(command_prefix = "!")

olgaInstance = OLGA()

with open("keys.json") as json_file:  
    data = json.load(json_file)
    TOKEN = data["discordKey"]

@client.event
async def on_ready():
    # Display OLGA logging in
    print("Logged in as")
    print(client.user.name)
    print(client.user.id)
    print("------")

@client.command(name = "olga")
async def on_command(ctx, *args:str):
    command = " ".join(args)
    global olgaInstance
    output = olgaInstance.run(command)
    if(output.error != None):
        await ctx.send(output.error)
    else:
        await ctx.send(output.text)

client.run(TOKEN)