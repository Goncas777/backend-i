import discord
import os
import logging
import sys
from ollama import AsyncClient
from dotenv import load_dotenv

logging.basicConfig(level=logging.DEBUG, handlers=[logging.StreamHandler(sys.stdout)])

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    logging.info(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    logging.info("message arrived.")
    if message.author == client.user:
        return

    if message.content.startswith('!ai'):
        logging.info("AI Message is going to interact with ollama")
        response = await AsyncClient(
            host='http://ollama:11434'
        ).chat(model='tinyllama:1.1b-chat-v0.6-q2_K', messages=[
            {
                'role': 'user',
                'content': 'Why is the sky blue?',
            },
        ])
        await message.channel.send(response.message.content)

def start():
    load_dotenv()
    client.run(os.getenv("DISCORD_TOKEN"))
