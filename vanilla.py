import discord
import os
import requests
import json
import random

virgin = [
'https://cdn.discordapp.com/attachments/296056831514509312/764176051730776075/26927006Ebe9da350b150bba495fda09a1091197-1.mp4',   
'https://cdn.discordapp.com/attachments/680928395399266314/812329088815464458/delete_persona.mp4',
'https://cdn.discordapp.com/attachments/764925620790493206/817857946364018698/video0_11_1.mp4',
'https://cdn.discordapp.com/attachments/464147924960673792/824072849308254259/video0-31.mp4',
'https://cdn.discordapp.com/attachments/810922220003000351/833389446460080138/specialist_special_ed.mp4'
'https://cdn.discordapp.com/attachments/810922220003000351/833390732765167656/asex.mp4',
'https://cdn.discordapp.com/attachments/810922220003000351/833390744173150248/fb.mp4',
'https://www.youtube.com/watch?v=Y9LISqYslWQ&list=PLh6XM2uQrTLcb6McPDELVDRz6GsworNYE&index=3',
'https://cdn.discordapp.com/attachments/810922220003000351/833391743978307655/Wear_A_Bag_Persona_4_Specialist_meme.mp4'
]

client = discord.Client()

# def get_quote():
# response = requests.get("")
#  json_data = json.loads(response.text)
#  quote = json_data[0]['q'] + " -" + json_data[0]['a']
#  return(quote)

@client.event
async def on_ready():
  await client.change_presence(activity=discord.Game(name="with your feelings | ;help"))
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return
    
  if message.content.startswith('hello'):
    msg = 'Yo wassup'.format(message)
    await message.channel.send(msg)
    
  if message.content.startswith(';virginity'):
    msg = random.choice(virgin).format(message)
    await message.channel.send(msg)
    
  if message.content.startswith(';help'):
      msg = 'commands are as follows. ;help ;virginity '.format(message)
      await message.channel.send(msg)
    

client.run('paste your bot token here in these apostropheses')


# other stuff
# {0.author.mention}  pings user
