import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='[')

@bot.event
async def on_reeady();
    print(">> Bot is online <<")

bot.run('NjA2Nzc5MDc0NTM4NTA0MTk0.XUQBMw.C2hgfWkLgtsGE0JlW0ljnQ7yV4U')