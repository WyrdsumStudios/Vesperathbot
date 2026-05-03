import discord
from discord.ext import commands
import os
from grok import GrokAPI

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Vesperath is online as {bot.user}")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if bot.user.mentioned_in(message):
        async with message.channel.typing():
            response = GrokAPI(os.getenv("GROK_API_KEY")).chat(message.content)
            await message.reply(response)
    
    await bot.process_commands(message)

bot.run(os.getenv("DISCORD_TOKEN"))
