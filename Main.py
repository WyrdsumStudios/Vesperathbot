import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Vesperath is online as {bot.user}")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    
    if bot.user.mentioned_in(message):
        await message.channel.typing()
        await message.reply("Vesperath is here. What do you need, my friend?")
    
    await bot.process_commands(message)

bot.run(os.getenv("DISCORD_TOKEN"))
