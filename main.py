import discord
import json
import requests
import random
import datetime
import aiohttp
import asyncio
import io
import requests
import telebot
import telegram
import asyncio
import colorama
from akaneko import akaneko
from colorama import Fore, Back, Style
from discord.ext import commands
# from config import settings
from telegram.ext import Updater, CommandHandler
from aiogram import Bot, Dispatcher, types
import webbrowser

bot = commands.Bot(command_prefix = ".")
bot.remove_command("help")

@bot.command() # Не передаём аргумент pass_context, так как он был нужен в старых версиях.
async def hello(ctx): # Создаём функцию и передаём аргумент ctx.
    author = ctx.message.author # Объявляем переменную author и записываем туда информацию об авторе.
    await ctx.send(f'Привет, {author.mention}!') # Выводим сообщение с упоминанием автора, обращаясь к переменной author.

@bot.command()
async def help(ctx):
    embed = discord.Embed(color = random.randint(0, 0xFFFFFF),title = "**Помощь по командам бота!**", description=(
    	f'.fox - Случайная лисичка\n.cat - Случайная кошечка\n.dog - Случайная собачка\n.lyrics - Текст любой песни\n.pat - Погладить кого-то\n.gay - Аватарка в цвета радуги\n.wasted - Аватарка как в GTA5\n.trigger - Аватарка в триггер эффект\n .hug - Обнять кого-то\n.facepalm - рука лицо\n .avatar - Отправляет аватарку '))
    embed.set_footer(text=f"Requested by {ctx.author}",icon_url=ctx.author.avatar_url,)
    await ctx.send(embed = embed)

@bot.command()
async def avatar(ctx, user = None):
  idd = user or str(ctx.author.id)
  try:
    member = await commands.MemberConverter().convert(ctx, idd)
  except:
    member = await bot.fetch_user(int(idd))
  em = discord.Embed(title = f'{member.name}#{member.discriminator}', color = member.color)
  webp = member.avatar_url_as(format=None, static_format='webp', size=2048)
  png = member.avatar_url_as(format=None, static_format='png', size=2048)
  jpg = member.avatar_url_as(format=None, static_format='jpg', size=2048)
  em.set_image(url=member.avatar_url)

  em.add_field(name="Link as", value=f"[webp]({webp}) | [jpg]({jpg}) | [png]({png})")
  await ctx.send(embed = em)

@bot.command()
async def fox(ctx):
    response = requests.get('https://some-random-api.ml/img/fox') # Get-запрос
    json_data = json.loads(response.text) # Извлекаем JSON

    embed = discord.Embed(color = random.randint(0, 0xFFFFFF), title = 'Случайная Лисичка') # Создание Embed'a
    embed.set_image(url = json_data['link']) # Устанавливаем картинку Embed'a
    await ctx.send(embed = embed) # Отправляем Embed

@bot.command()
async def cat(ctx):
    response = requests.get('https://some-random-api.ml/img/cat') # Get-запрос
    json_data = json.loads(response.text) # Извлекаем JSON

    embed = discord.Embed(color = random.randint(0, 0xFFFFFF), title = 'Случайная Кошачка') # Создание Embed'a
    embed.set_image(url = json_data['link']) # Устанавливаем картинку Embed'a
    await ctx.send(embed = embed) # Отправляем Embed

@bot.command()
async def dog(ctx):
    response = requests.get('https://some-random-api.ml/img/dog') # Get-запрос
    json_data = json.loads(response.text) # Извлекаем JSON

    embed = discord.Embed(color = random.randint(0, 0xFFFFFF), title = 'Случайная @') # Создание Embed'a
    embed.set_image(url = json_data['link']) # Устанавливаем картинку Embed'a
    await ctx.send(embed = embed) # Отправляем Embed

@bot.command()
async def facepalm(ctx):
    response = requests.get('https://some-random-api.ml/animu/face-palm') # Get-запрос
    json_data = json.loads(response.text) # Извлекаем JSON

    embed = discord.Embed(color = random.randint(0, 0xFFFFFF), title = '**Чел ты**') # Создание Embed'a
    embed.set_image(url = json_data['link']) # Устанавливаем картинку Embed'a
    await ctx.send(embed = embed) # Отправляем Embed

@bot.command()
async def pat(ctx, user: discord.Member= None):
    response = requests.get('https://some-random-api.ml/animu/pat') # Get-запрос
    json_data = json.loads(response.text) # Извлекаем JSON

    embed = discord.Embed(color = random.randint(0, 0xFFFFFF),title= '', description=(f"**:raised_hand:{ctx.author.display_name}** погладил **{user.display_name}**")) # Создание Embed'a
    embed.set_image(url = json_data['link']) # Устанавливаем картинку Embed'a
    await ctx.send(embed = embed) # Отправляем Embed

@bot.command()
async def hug(ctx, user: discord.Member= None):
    response = requests.get('https://some-random-api.ml/animu/hug') # Get-запрос
    json_data = json.loads(response.text) # Извлекаем JSON

    embed = discord.Embed(color = random.randint(0, 0xFFFFFF),title= '', description=(f"**:raised_hand:{ctx.author.display_name}** обмнял **{user.display_name}**")) # Создание Embed'a
    embed.set_image(url = json_data['link']) # Устанавливаем картинку Embed'a
    await ctx.send(embed = embed) # Отправляем Embed

@bot.command()
async def piss(ctx, user: discord.Member= None):

    embed = discord.Embed(color = random.randint(0, 0xFFFFFF),title= '', description=(f"**:eggplant:{ctx.author.display_name}** пописал на **{user.display_name}**")) # Создание Embed'a
    embed.set_image(url = "https://media.discordapp.net/attachments/634427526898515978/819489674145038337/xvataibecplatno.gif") # Устанавливаем картинку Embed'a
    await ctx.send(embed = embed) # Отправляем Embed

@bot.command()
async def manyman(ctx):
    a = await bot.fetch_user(396749451605049355)
    r = requests.get(f"https://api.imgur.com/3/album/RXjh6bm/images?client_id=6b7949e3ed6c2db").json()
    em = discord.Embed(description = f"Великий и привосходный МэниМен! {a.mention}")
    indexmax = len(r['data']) - 1

    size = random.randrange(0, indexmax, 1)
    em.set_image(url=str(r['data'][size]['link']))

    try:
        await ctx.send(embed=em)
    except:
        await ctx.send(str(r['data'][size]['link']))

@bot.command(aliases=["lrcs"])
async def lyrics(ctx, *, arg):

    await ctx.trigger_typing()
    arg = arg.replace(" ", "+")

    lrcsession = aiohttp.ClientSession()
    async with lrcsession.get(
        f"https://some-random-api.ml/lyrics?title={arg}"
    ) as lrcgetlnk:
        lrcdata = await lrcgetlnk.json()
    try:
        lyrrc = str(lrcdata["lyrics"])
        for chunk in [lyrrc[i : i + 2000] for i in range(0, len(lyrrc), 2000)]:
            embed = discord.Embed(
                title=f"**{(str(lrcdata['title']))} by {(str(lrcdata['author']))}**",
                description=chunk,
                color = 0x000000,
            )
            embed.set_footer(
                text=f"Requested by {ctx.author}",
                icon_url=ctx.author.avatar_url,
            )
            embed.timestamp = datetime.datetime.utcnow()
            await ctx.send(embed=embed)
    except discord.HTTPException:
        embe = discord.Embed(
            title=f"**{(str(lrcdata['title']))} by {(str(lrcdata['author']))}**",
            color=0x000000,
            description=chunk,
        )
        embe.set_footer(
            text=f"Requested by {ctx.author}",
            icon_url=ctx.author.avatar_url,
        )
        embe.timestamp = datetime.datetime.utcnow()
        await ctx.send(embed=embe)
    await lrcsession.close()

@bot.command()
async def wasted(ctx, member: discord.Member=None):
  if not member:
    member = ctx.author

  wastedsession = aiohttp.ClientSession()
  async with wastedsession.get(f"https://some-random-api.ml/canvas/wasted?avatar={member.avatar_url_as(format='png')}") as img:
    if img.status != 200:
      await ctx.send("Unable to get image")

    else:
      data = io.BytesIO(await img.read())
      await ctx.send(file=discord.File(data, 'wasted.png'))

@bot.command()
async def gay(ctx, member: discord.Member=None):
  if not member:
    member = ctx.author

  wastedsession = aiohttp.ClientSession()
  async with wastedsession.get(f"https://some-random-api.ml/canvas/gay?avatar={member.avatar_url_as(format='png')}") as img:
    if img.status != 200:
      await ctx.send("Unable to get image")

    else:
      data = io.BytesIO(await img.read())
      await ctx.send(file=discord.File(data, 'wasted.png'))

@bot.command()
async def trigger(ctx, member: discord.Member=None):
  if not member:
    member = ctx.author

  wastedsession = aiohttp.ClientSession()
  async with wastedsession.get(f"https://some-random-api.ml/canvas/triggered?avatar={member.avatar_url_as(format='png')}") as img:
    if img.status != 200:
      await ctx.send("Unable to get image")

    else:
      data = io.BytesIO(await img.read())
      await ctx.send(file=discord.File(data, 'wasted.png'))

@bot.command()
async def message (ctx,*,message):

    await ctx.send(f"Ты отправил вот это сообщение: {message}")
    requests.get(f"https://api.telegram.org/bot2127771308:AAH_iA2CwPy-9ojgAXyqHtHIHsH-pEoTIDc/sendMessage?chat_id=407753587&text={message}\nОтправил: {ctx.author}")

mss = message

bot.run(settings['token']) # Обращаемся к словарю settings с ключом token, для получения то