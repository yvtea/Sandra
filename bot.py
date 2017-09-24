#import discord.py libraries, secret token config
import discord
import config
from discord.ext import commands
client = discord.Client()
# when the bot is ready, print a message to the console
@client.event
async def on_ready():
    print('{0.user} online!'.format(client))
# when a message is sent, check to see if the author is the bot. if not--
@client.event
async def on_message(message):
    if message.author == client.user:
        return
#check to see if the message starts with the prefix + a command, if so, send a message
    if message.content.startswith('q!hello'):
        await message.channel.send('Hello!')

    elif message.content.startswith('q!yeet'):
    	await message.channel.send('yee')

    elif message.content.startswith('q!server'):
    	await message.channel.send('I am serving ' + str(users) + 'users!')

client.run(config.secret_token)