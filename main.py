import difflib
import traceback
from bs4 import BeautifulSoup
import pandas as pd
import xml.etree.ElementTree as et
from urllib.parse import urlencode, quote_plus, unquote
import random
import os 
import json
import discord
import time
import aiohttp
from discord.ext import commands
from discord.ui import Button, View
from discord import app_commands, Interaction
import random

sentence_list = [
    "가는 날이 장날이다.",
    "가는 말이 고와야 오는 말이 곱다.",
    "가랑비에 옷 젖는 줄 모른다.",
    "가재는 게 편이라.",
    "개같이 벌어서 정승같이 쓴다.",
    "개 눈에는 똥만 보인다.",
    "개는 잘 짖는 다고 좋은 개가 아니다.",
    "개도 닷새만 되면 주인을 안다.",
    "개미 구멍이 둑을 무너뜨릴 수도 있다.",
    "고슴도치에 놀란 호랑이 밤송이 보고 절한다.",
    "고양이가 발톱을 감춘다.",
    "고양이 목에 방울 단다.",
    "고양이 죽은데 쥐 눈물만큼.",
    "돼지 발톱에 봉숭아 들이기.",
    "똥 묻은 개가 겨 묻은 개를 나무란다.",
    "못된 송아지 엉덩이에 뿔난다.",
    "밥 먹을 때는 개도 안 건들인다.",
    "배부른 고양이는 쥐를 잡지 않는다.",
    "소 잃고 외양간 고친다.",
    "열 길 물속은 알아도 한 길 사람 속은 모른다.",
    "점잖은 고양이가 부뚜막에 먼저 올라간다.",
    "조용한 고양이가 쥐를 잡는다.",
    "콩 심은데 콩나고, 팥 심은데 팥난다.",
    "하룻강아지 범 무서운 줄 모른다.",
    "호랑이 굴에 들어가야 호랑이 새끼를 잡는다.",
    "호랑이에게 물려가도 정신만 바짝 차리면 산다.",
    "뱁새가 황새를 따라간다.",
    "송충이는 솔잎을 먹어야 산다.",
    "뱁새가 황새를 따라가단 가랭이가 찢어진다.",
    "개똥도 약에 쓰려니 없다.",
    "자라보고 놀란가슴 솥뚜껑보고 놀란다.",
    "지렁이도 밟으면 꿈틀한다.",
    "서당개 3년이면 풍월을 읊는다.",
    "포수 집 강아지 범 무서운 줄 모른다.",
    "얌전한 고양이 부뚜막에 먼저 올라간다."
]

secret_file = os.path.join('../secrets.json')

with open(secret_file) as f:
    secrets = json.loads(f.read())

def get_secret(setting, secrets=secrets):
    try:
        return secrets[setting]
    except KeyError:
        error_msg = "Set the {} environment variable".format(setting)
        return False

class aclient(discord.Client):
    def __init__(self):
        intents = discord.Intents.all()
        super().__init__(intents=intents)
        self.synced = False

    async def on_ready(self):
        await self.wait_until_ready()
        if not self.synced:
            await tree.sync()
            self.synced = True
        print(f'{self.user} is started!')
        game = discord.Game('[/도움말] 을 해보세요!')
        await self.change_presence(status=discord.Status.online, activity=game)


class MyView(discord.ui.View):
    def __init__(self):  # 오타: init → __init__
        super().__init__()
        self.add_item(discord.ui.Button(label="버튼 1", style=discord.ButtonStyle.primary, custom_id="button1"))
        self.add_item(discord.ui.Button(label="버튼 2", style=discord.ButtonStyle.secondary, custom_id="button2"))
        self.add_item(discord.ui.Button(label="버튼 3", style=discord.ButtonStyle.grey, custom_id="button3"))
        self.add_item(discord.ui.Button(label="버튼 4", style=discord.ButtonStyle.success, custom_id="button4"))
        self.add_item(discord.ui.Button(label="종료", style=discord.ButtonStyle.danger, custom_id="button5"))


    async def interaction_check(self, interaction: discord.Interaction) -> bool:
        # Only allow the user who initiated the original command to interact with the buttons
        return interaction.user.id == interaction.message.interaction.user.id
    
class CalculatorView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=120)
        self.expression = ""

    async def update_message(self, interaction: discord.Interaction):
        content = f"```\n{self.expression if self.expression else '0'}\n```"
        await interaction.response.edit_message(content=content, view=self)

    def add_to_expression(self, value: str):
        self.expression += value

    @discord.ui.button(label='7', style=discord.ButtonStyle.secondary, row=0)
    async def seven(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.add_to_expression("7")
        await self.update_message(interaction)

    @discord.ui.button(label='8', style=discord.ButtonStyle.secondary, row=0)
    async def eight(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.add_to_expression("8")
        await self.update_message(interaction)

    @discord.ui.button(label='9', style=discord.ButtonStyle.secondary, row=0)
    async def nine(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.add_to_expression("9")
        await self.update_message(interaction)

    @discord.ui.button(label='/', style=discord.ButtonStyle.primary, row=0)
    async def divide(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.add_to_expression("/")
        await self.update_message(interaction)

    @discord.ui.button(label='4', style=discord.ButtonStyle.secondary, row=1)
    async def four(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.add_to_expression("4")
        await self.update_message(interaction)

    @discord.ui.button(label='5', style=discord.ButtonStyle.secondary, row=1)
    async def five(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.add_to_expression("5")
        await self.update_message(interaction)

    @discord.ui.button(label='6', style=discord.ButtonStyle.secondary, row=1)
    async def six(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.add_to_expression("6")
        await self.update_message(interaction)

    @discord.ui.button(label='*', style=discord.ButtonStyle.primary, row=1)
    async def multiply(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.add_to_expression("*")
        await self.update_message(interaction)

    @discord.ui.button(label='1', style=discord.ButtonStyle.secondary, row=2)
    async def one(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.add_to_expression("1")
        await self.update_message(interaction)

    @discord.ui.button(label='2', style=discord.ButtonStyle.secondary, row=2)
    async def two(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.add_to_expression("2")
        await self.update_message(interaction)

    @discord.ui.button(label='3', style=discord.ButtonStyle.secondary, row=2)
    async def three(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.add_to_expression("3")
        await self.update_message(interaction)

    @discord.ui.button(label='-', style=discord.ButtonStyle.primary, row=2)
    async def minus(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.add_to_expression("-")
        await self.update_message(interaction)

    @discord.ui.button(label='C', style=discord.ButtonStyle.danger, row=3)
    async def clear(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.expression = ""
        await self.update_message(interaction)

    @discord.ui.button(label='0', style=discord.ButtonStyle.secondary, row=3)
    async def zero(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.add_to_expression("0")
        await self.update_message(interaction)

    @discord.ui.button(label='.', style=discord.ButtonStyle.secondary, row=3)
    async def dot(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.add_to_expression(".")
        await self.update_message(interaction)

    @discord.ui.button(label='+', style=discord.ButtonStyle.primary, row=3)
    async def plus(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.add_to_expression("+")
        await self.update_message(interaction)

    @discord.ui.button(label='=', style=discord.ButtonStyle.success, row=4)
    async def equals(self, interaction: discord.Interaction, button: discord.ui.Button):
        try:
            result = str(eval(self.expression))
            self.expression = result
        except Exception:
            self.expression = "Error"
        await self.update_message(interaction)

class NoticePager(discord.ui.View):
    def __init__(self, user: discord.User, notices: list):
        super().__init__(timeout=120)
        self.user = user
        self.notices = notices
        self.index = 0

    def create_embed(self):
        notice = self.notices[self.index]
        embed = discord.Embed(title=notice.get('title', '공지'), color=0x00aaff)
        content0 = f"{notice.get('content0', '')}"
        content1 = f"{notice.get('content1', '')}"
        if len(content0) > 1024:
            content0 = content0[:1021] + "..."
        if len(content1) > 1024:
            content1 = content1[:1021] + "..."
        embed.add_field(name="내용", value=content0, inline=False)
        embed.add_field(name=" ", value=content1, inline=False)
        embed.set_footer(text=f"{self.index + 1} / {len(self.notices)}")
        return embed

    async def interaction_check(self, interaction: discord.Interaction) -> bool:
        if interaction.user.id != self.user.id:
            await interaction.response.send_message("이 버튼은 당신만 사용할 수 있습니다.", ephemeral=True)
            return False
        return True

    @discord.ui.button(label="이전", style=discord.ButtonStyle.secondary)
    async def previous(self, interaction: discord.Interaction, button: discord.ui.Button):
        if self.index > 0:
            self.index -= 1
            embed = self.create_embed()
            await interaction.response.edit_message(embed=embed, view=self)
        else:
            await interaction.response.send_message("첫 공지입니다.", ephemeral=True)

    @discord.ui.button(label="다음", style=discord.ButtonStyle.primary)
    async def next(self, interaction: discord.Interaction, button: discord.ui.Button):
        if self.index < len(self.notices) - 1:
            self.index += 1
            embed = self.create_embed()
            await interaction.response.edit_message(embed=embed, view=self)
        else:
            await interaction.response.send_message("마지막 공지입니다.", ephemeral=True)


async def fetch_notices(url: str):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            if resp.status == 200:
                return await resp.json()
            return None


client = aclient()
tree = app_commands.CommandTree(client)


@tree.command(description='도움말을 띄웁니다.')
async def 도움말(interaction : discord.Interaction):
    embed = discord.Embed(title="도움말", color=0x66FFFF)
    embed.add_field(name='/도움말', value='현제 이 창을 띄웁니다.', inline=False)
    embed.add_field(name='/타자연습', value='타자 실력을 계산해줍니다.', inline=False)
    embed.add_field(name='/청소', value='메세지를 지웁니다.', inline=False)
    embed.add_field(name='/계산기', value='버튼으로 만든 계산기를 띄웁니다.', inline=False)
    embed.add_field(name='/중요공지', value='웹사이트의 중요 공지를 가져옵니다.', inline=False)
    embed.add_field(name='/일반공지', value='웹사이트의 일반 공지를 가져옵니다.', inline=False)
    embed.add_field(name='/아카이브공지', value='웹사이트의 아카이브 공지를 가져옵니다.', inline=False)
    embed.add_field(name='/팩트', value='이 서버의 모든 팩트를 알려줍니다.', inline=False)
    embed.add_field(name='/ping', value='봇의 처리 지연시간을 알려줍니다.', inline=False)
    await interaction.response.send_message(embed=embed)

@tree.command(description='봇의 처리 지연시간을 알려줍니다.')
async def ping(interaction : discord.Interaction):
    if client.latency>0 and client.latency<50:
        embed = discord.Embed(title="🔵 Pong!", color=0x2ADFF7)
        embed.add_field(name=' ', value=':ping_pong: Pong! {0}ms'.format(round(client.latency, 1)), inline=False)
        await interaction.response.send_message(embed=embed, ephemeral=True)
    if client.latency>51 and client.latency<500:
        embed = discord.Embed(title="🟢 Pong!", color=0x74f702)
        embed.add_field(name=' ', value=':ping_pong: Pong {0}ms'.format(round(client.latency, 1)), inline=False)
        await interaction.response.send_message(embed=embed, ephemeral=True)
    if client.latency>501 and client.latency<1000:
        embed = discord.Embed(title="🟠 Pong!", color=0xf76002)
        embed.add_field(name=' ', value=':ping_pong: Pong..... {0}ms'.format(round(client.latency, 1)), inline=False)
        await interaction.response.send_message(embed=embed, ephemeral=True)
    if client.latency>1001 and client.latency<5000:
        embed = discord.Embed(title="🔴 Pong(!waring! !waring!)", color=0xea4335)
        embed.add_field(name=' ', value=':ping_pong: Pong! {0}ms'.format(round(client.latency, 1)), inline=False)
        await interaction.response.send_message(embed=embed, ephemeral=True)
    if client.latency>5001 and client.latency<100000:
        embed = discord.Embed(title="💀 Pong????????????????(wtf???????)", color=0x000000)
        embed.add_field(name=' ', value=':ping_pong: Pong! {0}ms'.format(round(client.latency, 1)), inline=False)
        await interaction.response.send_message(embed=embed, ephemeral=False)
    print(client.latency)

@tree.command(name="계산기", description="버튼 기반 계산기를 실행합니다.")
async def 계산기(interaction: discord.Interaction):
    view = CalculatorView()
    await interaction.response.send_message("```\n0\n```", view=view)

@tree.command(name="팩트", description="이 서버의 모든 팩트를 알려줍니다.")
async def 팩트(interaction: discord.Interaction):
    embed = discord.Embed(title="팩트", color=0x66FFFF)
    embed.add_field(name='1.DICEDICEFACE1은 멍청하다', value='공부할 생각도 없음.', inline=False)
    await interaction.response.send_message(embed=embed, ephemeral=False)

    
@tree.command(name="중요공지", description="웹사이트에서 최신 중요공지를 가져옵니다.")
async def 중요공지(interaction: discord.Interaction):
    url = "https://www.wltp.world/api/important_notices/"
    data = await fetch_notices(url)
    if not data or len(data) == 0:  
        await interaction.response.send_message("❌ 공지사항을 가져오지 못했습니다.", ephemeral=True)
        return

    view = NoticePager(interaction.user, data)
    embed = view.create_embed()
    await interaction.response.send_message("📢 중요 공지 목록입니다.", embed=embed, ephemeral=True, view=view)


@tree.command(name="일반공지", description="웹사이트에서 최신 일반공지를 가져옵니다.")
async def 일반공지(interaction: discord.Interaction):
    url = "https://www.wltp.world/api/normal_notices/"
    data = await fetch_notices(url)
    if not data or len(data) == 0:
        await interaction.response.send_message("❌ 공지사항을 가져오지 못했습니다.", ephemeral=True)
        return

    view = NoticePager(interaction.user, data)
    embed = view.create_embed()
    await interaction.response.send_message("📢 일반 공지 목록입니다.", embed=embed, ephemeral=True, view=view)


@tree.command(name="아카이브공지", description="웹사이트에서 최신 아카이브공지를 가져옵니다.")
async def 아카이브공지(interaction: discord.Interaction):
    url = "https://www.wltp.world/api/archived_notices/"
    data = await fetch_notices(url)
    if not data or len(data) == 0:
        await interaction.response.send_message("❌ 공지사항을 가져오지 못했습니다.", ephemeral=True)
        return

    view = NoticePager(interaction.user, data)
    embed = view.create_embed()
    await interaction.response.send_message("📢 아카이브 공지 목록입니다.", embed=embed, ephemeral=True, view=view)



@tree.command(description='타자 실력을 계산해줍니다.')
async def 타자연습(interaction: discord.Interaction):
    class TypingTestView(View):
        def __init__(self):
            super().__init__(timeout=10)
            self.choice = random.choice(sentence_list)
            self.start_time = None
            self.message_check = None

        @discord.ui.button(label="✅ 시작", style=discord.ButtonStyle.success)
        async def start_button(self, interaction2: discord.Interaction, button: Button):
            if interaction2.user != interaction.user:
                return await interaction2.response.send_message("이 타자 연습은 당신을 위한 것이 아닙니다.", ephemeral=True)

            self.start_time = time.time()
            await interaction2.response.send_message(f"아래의 글을 입력하세요:\n`{self.choice}`")

            def check(m):
                return m.author == interaction.user and m.channel == interaction.channel

            try:
                message = await client.wait_for("message", timeout=60.0, check=check)
                delta = time.time() - self.start_time
                accuracy = difflib.SequenceMatcher(None, self.choice, message.content).ratio()
                speed = len(self.choice) * accuracy * 3 / delta * 60

                await interaction.channel.send(f"타자: `{round(speed)}타`\n정확도: `{accuracy * 100:.1f}%`")
            except:
                await interaction.channel.send("시간이 초과되었습니다.")

            self.stop()

        @discord.ui.button(label="❌ 취소", style=discord.ButtonStyle.danger)
        async def cancel_button(self, interaction2: discord.Interaction, button: Button):
            if interaction2.user != interaction.user:
                return await interaction2.response.send_message("이 버튼은 당신을 위한 것이 아닙니다.", ephemeral=True)

            await interaction2.response.send_message("타자 연습을 취소했습니다.")
            self.stop()

    embed = discord.Embed(
        title="타자연습 (10초 안에 선택하세요)",
        description="✅ 시작을 누르면 연습이 시작됩니다.\n❌ 취소를 누르면 종료됩니다.",
        color=0x00aaaa
    )

    await interaction.response.send_message(embed=embed, view=TypingTestView())




@tree.command(description='랜덤 봇과 주사위를 굴립니다')
async def 주사위(interaction: discord.Interaction, numrange: int):
    if numrange < 2:
        await interaction.response.send_message("2 이상의 숫자를 입력해주세요.", ephemeral=True)
        return

    a = random.randrange(1, numrange)
    b = random.randrange(1, numrange)

    bot1 = str(a)
    user = str(b)

    if a > b:
        result = f'{interaction.user.name}의 패배'
        _color = 0xFF0000
    elif a == b:
        result = '무승부'
        _color = 0xFAFA00
    else:
        result = f'{interaction.user.name}의 승리'
        _color = 0x00ff56

    embed = discord.Embed(title="🎲 주사위 게임 결과", description=result, color=_color)
    embed.add_field(name="봇의 숫자", value=f":game_die: {bot1}", inline=True)
    embed.add_field(name=f"{interaction.user.name}의 숫자", value=f":game_die: {user}", inline=True)

    await interaction.response.send_message(embed=embed)



@tree.command(description='메세지를 지웁니다')
async def 청소(interaction: discord.Interaction, number: int):
    if number is not None and number > 0:
        await interaction.response.send_message(f'**{number}개**의 메세지를 삭제합니다...', ephemeral=True)
        deleted = await interaction.channel.purge(limit=number + 2)
        msg = await interaction.channel.send(f'**{len(deleted)}개**의 메세지를 삭제했습니다.(이 메세지는 3초 후에 사라집니다)')
        await asyncio.sleep(3)
        await msg.delete()
    else:
        await interaction.response.send_message('올바른 값을 입력해주세요.', ephemeral=True)




params = "def"



client.run(get_secret("Token")) #지세봇
