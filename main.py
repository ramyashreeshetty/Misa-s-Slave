
import discord
import os
import random
from keep_alive import keep_alive

client = discord.Client()

li=['rock','paper','scissor']
secure_random = random.SystemRandom()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$rock'):
        msg=secure_random.choice(li)
        await message.channel.send(msg)
        if(msg=='paper'):
          await message.channel.send('You lost mf!')
        elif (msg=='scissor'):
          await message.channel.send('You won, lucky hoe!')
        else:
          await message.channel.send('You strong as me -_-')

    if message.content.startswith('$paper'):
        msg1=secure_random.choice(li)
        await message.channel.send(secure_random.choice(li))
        if(msg1=='scissor'):
          await message.channel.send('You lost mf!')
        elif (msg1=='rock'):
          await message.channel.send('You won, lucky hoe!')
        else:
          await message.channel.send('You strong as me -_-')

    if message.content.startswith('$scissor'):
        msg2=secure_random.choice(li)
        await message.channel.send(secure_random.choice(li))
        if(msg2=='rock'):
          await message.channel.send('You lost mf!')
        elif (msg2=='paper'):
          await message.channel.send('You won, lucky hoe!')
        else:
          await message.channel.send('You strong as me -_-')

keep_alive()
client.run(os.getenv('TOKEN'))