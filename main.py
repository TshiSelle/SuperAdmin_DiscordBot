import settings
import discord
from discord.ext import commands

def run():
  intents = discord.Intents.default()
  bot = commands.Bot(command_prefix="!", intents = intents)
  
  @bot.event
  async def on_ready():
    print(f"bot is logged in as {bot.user}")
    print(f"with ID {bot.user.id}")
    print("------------------")
    
  bot.run(settings.BOT_TOKEN)

if __name__ == "__main__":
  run()