import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='[')

@bot.event
async def on_ready():
    print(">> Bot is online <<")

@bot.event 
async def on_member_join(member):
    channel = bot.get_channel(606867059837501470)
    await channel.send(f'{member}上線囉~~')


@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(606867165123182595)
    await channel.send(f'{member}離線囉~~')

@bot.command()
async def ping(ctx):
    await ctx.send(f'{round(bot.latency*1000)}(ms)')

bot.run('NjA2Nzc5MDc0NTM4NTA0MTk0.XURZmQ.nmM585zPMp-TOeQvQ68NtIOlO48')