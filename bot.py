import os
import discord
import random
import time
import asyncio
from dotenv import load_dotenv



load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

counter = 5
intents = discord.Intents.all()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILD:
            break

@client.event
async def on_message(message):



    if 'ssp' in message.content.lower():
            SSPalternativ = ["Papir","Saks","Stein"]
            Botss = random.choice(SSPalternativ)
            await message.channel.send(Botss)
            if ' stein' in message.content.lower() and Botss == "Saks":
                await message.channel.send("du vant")
            elif ' papir' in message.content.lower() and Botss == "Stein":
                await message.channel.send("du vant")
            elif ' saks' in message.content.lower() and Botss == "Papir":
                await message.channel.send("du vant")
            elif ' stein' in message.content.lower() and Botss == "Stein":
                await message.channel.send("Det ble likt")
            elif ' saks' in message.content.lower() and Botss == "Saks":
                await message.channel.send("Det ble likt")
            elif ' papir' in message.content.lower() and Botss == "Papir":
                await message.channel.send("Det ble likt")
            else:
                 await message.channel.send("Du tapte")



client.run(TOKEN)


