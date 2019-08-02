import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='[')

@bot.event
async def on_ready():
    print(">> Bot is online <<")

bot.run('NjA2Nzc5MDc0NTM4NTA0MTk0.XUQLdQ.eKk1lmtftCOY2Nh0X0Nu8kQCHPg')