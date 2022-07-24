import os
import discord
import openai as openai_api
from discord import Message
from discord.ext import commands
from discord.ext.commands import Context

DEBUG_MODE = os.environ.get('DEBUG_MODE', False)
DISCORD_BOT_TOKEN = os.environ.get("DISCORD_BOT_TOKEN")
ENGINE = "text-davinci-002"

intents = discord.Intents.default()
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name} with ID {bot.user.id}")


@bot.command()
async def openai(context: Context):
    message: Message = context.message.strip()

    if DEBUG_MODE:
        print(f"Reading message: {message.content}")

    completion = openai_api.Completion.create(engine=ENGINE, prompt=message.content)

    output = completion.choices[0].text.strip()

    if DEBUG_MODE:
        print(f"Replying: {output}")

    await context.send(output)


bot.run(DISCORD_BOT_TOKEN)
