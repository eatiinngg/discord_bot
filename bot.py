import discord
from discord.ext import commands
import json
import random

with open('setting.json', mode='r', encoding='utf8') as jfile:
    jdata=json.load(jfile)

bot = commands.Bot(command_prefix='-')

@bot.event
async def on_ready():
    print(">> Bot is online <<")

@bot.event 
async def on_member_join(member):
    channel = bot.get_channel(int(jdata['Welcome_channel']))
    await channel.send(f'{member}上線囉~~')

@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(int(jdata['Leave_channel']))
    await channel.send(f'{member}離線囉~~')

@bot.command()#隨機選圖
async def 圖片(ctx):
    random_pic=random.choice(jdata['pic'])
    pic=discord.File(random_pic)
    await ctx.send(file=pic)

@bot.command()#隨機選圖網址上
async def web(ctx):
        random_pic=random.choice(jdata['url_pic'])
        await ctx.send(random_pic)    

@bot.command()   #觸發
async def p(ctx, keyword):
    if keyword == '媽媽':
        pic=discord.File(jdata['pic'])
        await ctx.send(file=pic)
    elif keyword == '貓貓':
        gf=discord.File(jdata['gf'])
        await ctx.send(file=gf)
    else:
        channel = bot.get_channel(int(jdata['Welcome_channel']))
        await channel.send(f'沒有這張圖啦~~~')

@bot.command()
async def ping(ctx):
    await ctx.send(f'{round(bot.latency*1000)}(ms)')

bot.run(jdata['TOKEN'])