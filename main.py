import os
import discord
import openai as openai_api
from discord import Message
from discord.ext import commands
from discord.ext.commands import Context

DISCORD_BOT_TOKEN = os.environ.get("DISCORD_BOT_TOKEN")
ENGINE = "text-davinci-002"

intents = discord.Intents.default()
bot = commands.Bot(command_prefix='!', intents=intents)


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name} with ID {bot.user.id}")


@bot.command(name="commands")
async def print_commands(ctx: Context):
    await ctx.send("!commands - List of commands"
                   "!openai - Ask the bot a question"
                   "!engine - Print the current engine")


@bot.command()
async def engine(context: Context):
    await context.send(f"I am using the engine \"{ENGINE}\"")


@bot.command(name="openai", help="Ask OpenAI about something")
async def prompt(context: Context):
    message: Message = context.message
    message_content = str(message.content).strip()

    # this will hopefully prevent the engine from continuing the prompt instead
    # of giving a response to the prompt
    if not message_content.endswith((".", "?", "!")):
        message_content += "."

    completion = openai_api.Completion.create(
        engine=ENGINE,
        prompt=message_content,
        n=1,
        max_tokens=100,
    )

    output = completion.choices[0].text.strip()

    await context.send(output)


bot.run(DISCORD_BOT_TOKEN)
