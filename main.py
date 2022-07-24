import discord
import openai
from discord import Message
from discord.ext import commands
from discord.ext.commands import Context

ENGINE = "text-davinci-002"

intents = discord.Intents.default()
bot = commands.Bot(command_prefix='!openai', intents=intents)


@bot.command()
async def on_message(context: Context):
    message: Message = context.message

    completion = openai.Completion.create(engine=ENGINE, prompt=message.content)

    output = completion.choices[0].text.strip()

    await context.send(output)


bot.run('token')
