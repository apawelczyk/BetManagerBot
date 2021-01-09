import os
from dotenv import load_dotenv
import discord
import GoogleSheetsAPI

# Get Bot token from settings file
BASEDIR = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(BASEDIR, '.env'))
token = os.getenv("TOKEN")

# Connect Bot to Discord
client = discord.Client()

# On Bot Start
@client.event
async def on_ready():
    print("Started!")

# On Discord Message
@client.event
async def on_message(message):
    # Block Bot from sending because of itself
    if message.author == client.user:
        return

    await message.channel.send(GoogleSheetsAPI.GetRows())
    return

# Launch Bot
client.run(token)