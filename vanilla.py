import discord
import os
import requests
# import json
# import random

client = discord.Client()

# def get_quote():
# response = requests.get("")
#  json_data = json.loads(response.text)
#  quote = json_data[0]['q'] + " -" + json_data[0]['a']
#  return(quote)

@client.event
async def on_ready():
  await client.change_presence(activity=discord.Game(name="this is a status"))
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return
    
  if message.content.startswith('hello'):
    msg = 'Yo wassup'.format(message)
    await message.channel.send(msg)   
    
  if message.content.startswith(';help'):
      msg = 'commands are as follows. ;help '.format(message)
      await message.channel.send(msg)
    

client.run('paste your bot token here in these apostropheses')


# other stuff
# {0.author.mention}  pings user
