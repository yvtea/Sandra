#load discord.py libraries, config, whatever modules

import discord
from discord.ext import commands
import config
import random
from datetime import datetime

client = discord.Client()
now = datetime.now()

# when the bot is ready, print a message to the console

@client.event
async def on_ready():  
    print('{0.user} is now online!'.format(client))
    await client.change_presence(game=discord.Game(name=config.game))
# when a message is sent, check to see if the message author is the bot. if not, execute the specified command

@client.event
async def on_message(message):
    if message.author == client.user:
        return
   
    if message.content.startswith(config.prefix + 'hello'):
        await message.channel.send('Hello!')

    elif message.content.startswith(config.prefix + 'up'):
    	await message.channel.send('I have been up since %s-%s-%s, %s:%s!' % (now.day, now.month, now.year, now.hour, now.minute))

    elif message.content.startswith(config.prefix + 'code'):
    	await message.channel.send('I was made by <@202137748885340160>, and my source code is at https://github.com/yvtea/Sandra !')

    elif message.content.startswith(config.prefix + 'd20'):
    	await message.channel.send('I rolled a %s!' % (random.randint(0, 20)))

client.run(config.token)
