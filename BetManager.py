import os
import discord

# Get Bot token from settings file
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

    await message.channel.send("Test 3!")
    return

# Launch Bot
client.run(token)