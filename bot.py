import discord
import asyncio
import random
import time
import datetime
import os

from discord.ext import commands

intents = discord.Intents.all()
client = commands.Bot(command_prefix='$', intents=intents)
client.remove_command("help")


@client.event
async def on_member_join(member):
    if (datetime.datetime.utcnow() - member.created_at).total_seconds() < 864000:
        guild = member.guild
        role = guild.get_role(799274955392417802)
        await member.add_roles(role)
        print((datetime.datetime.utcnow() - member.created_at).total_seconds())
    else:
        print("test")
        print((datetime.datetime.utcnow() - member.joined_at).total_seconds())



client.run(os.environ['TOKEN'])
