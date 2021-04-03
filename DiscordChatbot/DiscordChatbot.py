import discord
from discord.ext import commands

token = 'ODI3MTI4NjE2NTAwMzMwNTI3.YGWhjQ.iNHhY3sJ9VjXqNweUscaYJ71QCM'

client = commands.Bot(command_prefix='')

@client.event
async def on_ready():
    game = discord.Game("명령어 => 씹섭아 도움||테스트버전")
    await client.change_presence(status=discord.Status.online, activity=game)
    print("READY")

@client.command(name='씹섭아')
async def common(ctx,command):
    if command == '도움':
        await ctx.send(f'추후 추가 예정')

    if command == '안녕':
        await ctx.send(f'ㅎㅇ')

@client.command(name='씹섭이')
async def common(ctx,command):
    if command == '병신':
        await ctx.send(f'뭐 시발')

client.run(token)