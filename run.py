import asyncio
import discord
import os
from discord.ext import commands
from discord.utils import get
import random

client = discord.Client()
app = commands.Bot(command_prefix='!')
game = discord.Game("개발중")

token_path = os.path.dirname( os.path.abspath( __file__ ) )+"/token.txt"    
t = open(token_path,"r",encoding="utf-8")
token = t.read().split()[0]
print("Token_key : ",token)

@app.event
async def on_ready():
    print("이 봇으로 로그인 : "+(app.user.name))
    print("=============")
    game = discord.Game("개발중")
    await app.change_presence(status=discord.Status.online, activity=game)

@app.event
async def on_message(message):
    await app.process_commands(message)
    if message.author.bot:
        return None
    if message.content.startswith("!변태쉑 전번"):
        await message.channel.send('01040787377')

@app.command(name="멘션", pass_context=True)
async def _HumanRole(ctx, member: discord.Member=None):
    for x in range (10):
        await ctx.send(str(member.mention)+"멘션")

@app.command()
async def 도움(ctx):
    embed=discord.Embed(title= f"멘션봇 사용방법", description=f"!멘션 [멘션할사람 멘션]", color=0xf3bb76)
    embed.add_field(name=f"예시",value=f"!멘션 @이승민#2377",inline=True)
    embed.add_field(name=f"멘션봇은 더 많은 기능이 추가가 가능합니다",value=f"아이디어를 주시면 봇에추가가 가능합니다",inline=False)
    await ctx.send(embed=embed)

app.run(token)