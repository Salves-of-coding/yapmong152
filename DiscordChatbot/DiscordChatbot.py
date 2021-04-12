import discord
from discord.ext import commands
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup

token = 'ODI3MTI4NjE2NTAwMzMwNTI3.YGWhjQ.iNHhY3sJ9VjXqNweUscaYJ71QCM'

client = commands.Bot(command_prefix='')

@client.event
async def on_ready():
    game = discord.Game("명령어 => 씹섭아 도움||테스트버전")
    await client.change_presence(status=discord.Status.online, activity=game)
    print("READY")

@client.command(name='씹섭아')
async def common(ctx,command,seccommand=''):
    if command == '도움':
        await ctx.send(f'```cs\n# 씹섭봇 사용법'
                       f'\n명령어 목록만 보려면 \'씹섭아 명령어\'를 쳐주세요'
                       f'\n\n\"1.명령어 사용방법\"'
                       f'\n아래 목록에 있는 명령어들을 씹섭아 또는 씹섭이 뒤에 적어서 사용합니다.'
                       f'\n\n\"2.씹섭아 명령어 목록\"'
                       f'\n안녕-씹섭이와 인사를 주고받습니다.'
                       f'\n\n\"3.씹섭이 명령어 목록\"'
                       f'\n병신-씹섭이에게 시비를 겁니다.```')

    if command == '안녕':
        await ctx.send(f'ㅎㅇ')

    if command == '오스':
        req = Request(f'{seccommand}')
        res = urlopen(req)
        html = res.read()

        bs = BeautifulSoup(html, 'html.parser')
        tags = bs.find('div', attrs={'class': 'value-display__value'})
        print(tags.text)
        await ctx.send(tags.text)

@client.command(name='씹섭이')
async def common(ctx,command):
    if command == '병신':
        await ctx.send(f'뭐 시발')

client.run(token)