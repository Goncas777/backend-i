# This example requires the 'message_content' intent.

import discord
from discord.ext import commands
from dotenv import load_dotenv
import os


load_dotenv()


intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('hello'):
        await message.channel.send('BROOOO SHUT THE F*CK UP')


def run(token):
    client.run(token)

def welcome():
        print("HELLO, HOW ARE YOU?")



