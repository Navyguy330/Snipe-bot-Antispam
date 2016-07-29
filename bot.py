#
# Snipe-bot-Antispam
# Author: Navyguy330
#

import asyncio
import discord
import json
import re

client = discord.Client()

config = {}
with open('config.json') as output:
     config = json.load(output)

api_key = config.get('api_key', 'NA')
channels = config.get('channels', [])    

@client.event
async def on_ready():
    if api_key == 'NA':
        raise Exception('Specify API Key')

    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    # Check if includes lat and long

    # patern for check string contains lat and long
    partern = "(\-?\d+(\.\d+)?),\s*(\-?\d+(\.\d+)?)"
    
    print(message.content +': '+ message.channel.name)
    # Manage channel rare_spottings only
    if message.channel.name in channels:
        print('this channel')
        if not re.match(partern, message.content):
            # Delete message if not contain lat/long
            await client.delete_message(message)

# Start client
client.run(api_key)
