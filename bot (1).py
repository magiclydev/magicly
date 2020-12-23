import discord 
from discord.ext import commands
import config
import re
import os
#---------------------------------
client = commands.Bot(command_prefix=config.Prefix, case_insensitive = True)
client.remove_command('help')
#---------------------------------ONLINE
@client.event
async def on_ready():
    print('---------------------------------')
    print(f'Logged in as {client.user.name}!')
    print('---------------------------------')
    await client.change_presence(status= discord.Status.online ,activity=discord.Activity(type=discord.ActivityType.watching, name=f'{config.status}'))
    channel = client.get_channel(config.Log_channel_id)
    em = discord.Embed(title=f"",color=0xff8c69)
    em.add_field(name=f"{client.user.name} | Online!",value=f"{client.user.mention} has come online!")
    await channel.send(embed=em) # this is the logging message for the beta server
#---------------------------------
@client.event
async def on_message(message):
    if f'{config.trigger}' in message.content:
        for i in await message.channel.history(limit=3).flatten(): #This will make the bot look at the history of the channel (NEEDED)
            if i.author == client.user:
                await i.delete() # this deletes the old bot message
        em = discord.Embed(color=config.embed_color)
        em.add_field(name=f"__Reminder__",value=f"{config.Rule_1}\n{config.Rule_2}\n{config.Rule_3}\n{config.Rule_4}\n{config.Rule_5}")
        em.add_field(name=f"__Useful links__",value=f"{config.link_1} | {config.link_2} | {config.link_3} | {config.link_4}",inline=False) # ONLY CHANGE THE EMBED IN THE CONFIG FILE
        em.set_thumbnail(url=client.user.avatar_url)
        await message.channel.send(embed=em) 



# ONLY CHANGE THE CONFIG IF YOU NEED THIS STUFF CHANGING ASK ME AS IT ALWAYS FUCKS UP! <  <   <   <

#---------------------------------

client.run(os.environ['TOKEN'])
