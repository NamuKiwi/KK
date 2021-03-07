import discord
import random
import os

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    game = discord.Game("!안내 를 사용해서 디스코드 서버에 들어가주세요!")
    await client.change_presence(status=discord.Status.online, activity=game)

@client.event
async def on_message(message):
    if message.content.startswith('!ping'):
        await message.channel.send('pong')
    if message.content.startswith('!안내'):
        await message.channel.send(f'{message.author.mention}, 아래의 링크를 서버에 꼭 들어가주세요. 서버에 있어야 아래 링크 자료가 보입니다.')
        embed = discord.Embed(title="안내",description="https://discord.gg/7Zm3DDsGTb", color=0x00ff00)
        embed.set_thumbnail(url="https://discord.gg/7Zm3DDsGTb")
        await message.channel.send(embed=embed)
    if message.content.startswith('!던전퍼즐'):
        await message.channel.send(f'{message.author.mention}, 아래의 링크를 눌러 참고하세요')
        embed = discord.Embed(title="던전 퍼즐",description="http://bit.ly/3rmcgwp", color=0x00ff00)
        embed.set_thumbnail(url="https://kin-phinf.pstatic.net/20170724_80/1500884837790lFVgc_JPEG/photo.jpg?type=w750")
        await message.channel.send(embed=embed)
    if message.content.startswith('!던전직업'):
        await message.channel.send(f'{message.author.mention}, 아래의 링크를 눌러 참고하세요')
        embed = discord.Embed(title="던전 직업",description="https://bit.ly/3c53iNE -출처-나무위키 (하이픽셀/Skyblock/던전)", color=0x00ff00)
        embed.set_thumbnail(url="https://kin-phinf.pstatic.net/20170724_80/1500884837790lFVgc_JPEG/photo.jpg?type=w750")
        await message.channel.send(embed=embed)
    if message.content.startswith('!던전입구'):
        await message.channel.send(f'{message.author.mention}, 아래의 링크를 눌러 참고하세요')
        embed = discord.Embed(title="던전 입구",description="http://bit.ly/3uX7Hux", color=0x00ff00)
        embed.set_thumbnail(url="https://kin-phinf.pstatic.net/20170724_80/1500884837790lFVgc_JPEG/photo.jpg?type=w750")
        await message.channel.send(embed=embed)
    if message.content.startswith('!던전1층'):
        await message.channel.send(f'{message.author.mention}, 아래의 링크를 눌러 참고하세요')
        embed = discord.Embed(title="던전 1층",description="https://bit.ly/3rpYSHA", color=0x00ff00)
        embed.set_thumbnail(url="https://kin-phinf.pstatic.net/20170724_80/1500884837790lFVgc_JPEG/photo.jpg?type=w750")
        await message.channel.send(embed=embed)
    if message.content.startswith('!던전2층'):
        await message.channel.send(f'{message.author.mention}, 아래의 링크를 눌러 참고하세요')
        embed = discord.Embed(title="던전 2층",description="http://bit.ly/3eh47FS", color=0x00ff00)
        embed.set_thumbnail(url="https://kin-phinf.pstatic.net/20170724_80/1500884837790lFVgc_JPEG/photo.jpg?type=w750")
        await message.channel.send(embed=embed)
    if message.content.startswith('!던전3층'):
        await message.channel.send('pong')
    if message.content.startswith('!던전4층'):
        await message.channel.send('pong')
    if message.content.startswith('!초대'):
        await message.channel.send(f'{message.author.mention}, 아래의 링크를 눌러 키위봇을 초대하세요!')
        embed = discord.Embed(title="초대", description="http://bit.ly/키위봇초대", color=0x00ff00)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/811098843617296395/817701603720167445/5ed14b980281d09eb54b5e8a25391560.png")
        await message.channel.send(embed=embed)
    if message.content.startswith('!키위'):
        await message.channel.send(f'{message.author.mention}, 봇제작자')
        embed = discord.Embed(title="키위는 맛있습니다", description="http://bit.ly/ㅋㅁ", color=0x00ff00)
        embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/817686947287531531/230e1a7777dd7edfd394b189dad75b2c.png?size=1024")
        await message.channel.send(embed=embed)
    if message.content.startswith('!포'):
        await message.channel.send(f'{message.author.mention},귀여운 포')
        embed = discord.Embed(title="귀여운 포!", color=0x00ff00)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/817023052591923220/817953483839635476/image0.png")
        await message.channel.send(embed=embed)
    if message.content.startswith('!오버로드'):
        await message.channel.send(f'{message.author.mention}, 오버로드 트롤!')
        embed = discord.Embed(title="0ver1ord killed a Blaze in the wrong order! Yikes!", description="http://bit.ly/0ver1ord", color=0x00ff00)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/817023052591923220/817955539836338216/unknown.png")
        await message.channel.send(embed=embed)
    if message.content.startswith('!ㅇㅂㄹㄷ'):
        await message.channel.send(f'{message.author.mention}, 오버로드 트롤!')
        embed = discord.Embed(title="0ver1ord killed a Blaze in the wrong order! Yikes!", description="http://bit.ly/0ver1ord", color=0x00ff00)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/817023052591923220/817955539836338216/unknown.png")
        await message.channel.send(embed=embed)
    if message.content.startswith('!ㅋㅇ'):
        await message.channel.send(f'{message.author.mention}, 봇제작자')
        embed = discord.Embed(title="키위는 맛있습니다", description="http://bit.ly/ㅋㅁ", color=0x00ff00)
        embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/817686947287531531/230e1a7777dd7edfd394b189dad75b2c.png?size=1024")
        await message.channel.send(embed=embed)
    if message.content.startswith('!플마'):
        await message.channel.send(f'{message.author.mention}, 플마님!')
        embed = discord.Embed(title="pllma", color=0x00ff00)
        embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/738614630070485024/e478ca1b4c6a417d5c2f1267ac6aa28d.png?size=1024")
        await message.channel.send(embed=embed)




access_token = os.environ["BOT_TOKEN"]
client.run('access_token')
