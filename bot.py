#import discord.py libraries, config

import discord
import config
import random
from datetime import datetime
from discord.ext import commands
client = discord.Client()
now = datetime.now()
# when the bot is ready, print a message to the console

@client.event
async def on_ready():
    print('{0.user} is online!'.format(client))
    await client.change_presence(game=discord.Game(name=config.game))

# when a message is sent, check to see if the author is the bot. if not--

@client.event
async def on_message(message):
    if message.author == client.user:
        return

#check to see if the message starts with the prefix + a command, if so, send a message

    if message.content.startswith(config.prefix + 'hello'):
        await message.channel.send('Hello!')

    elif message.content.startswith(config.prefix + 'yeet'):
    	await message.channel.send('yee')

    elif message.content.startswith(config.prefix + 'up'):
    	await message.channel.send('I have been up since %s-%s-%s, %s:%s!' % (now.day, now.month, now.year, now.hour, now.minute))

client.run(config.token)
