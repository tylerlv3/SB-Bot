import discord
from discord.ext import commands
import time
from bs4 import BeautifulSoup
from urllib.request import  Request, urlopen
import sched
import threading

TOKEN = 'NjA1OTU0MDQwMjc4NTQ4NTEw.Xg1q6g.6lpgDDjpZTV0h3FmmN_5pApnAqo'
client = commands.Bot(command_prefix='.')
client.remove_command('help')
client.remove_command('play')

channel_updates = client.get_channel(606184739166093337)


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    await vxniilive()

@client.command(pass_context=True)
async def istop(ctx):
    channel = ctx.message.channel
    channel_updates = client.get_channel(606184739166093337)
    istop_channel = client.get_channel(606188136925626489)
    if channel == channel_updates:
        istop_lvl = ctx.message.content.replace('.istop', '')
        await istop_channel.edit(name="🔝 𝐈𝐬 𝐓𝐨𝐩 𝐑𝐚𝐧𝐤: " + istop_lvl)
        time.sleep(10)
        msg = ctx.message
        await msg.delete()

@client.command(pass_context=True)
async def isworth(ctx):
    channel = ctx.message.channel
    channel_updates = client.get_channel(606184739166093337)
    istop_channel = client.get_channel(606202968701665310)
    if channel == channel_updates:
        istop_lvl = ctx.message.content.replace('.isworth', '')
        await istop_channel.edit(name="💰 𝐈𝐬 𝐖𝐨𝐫𝐭𝐡: " + istop_lvl)
        time.sleep(10)
        msg = ctx.message
        await msg.delete()


@client.command(pass_context=True)
async def setup(ctx):
    guild = ctx.message.guild
    await ctx.guild.create_category(":bar_chart: Spawner Counts :bar_chart:")
    await guild.create_voice_channel('GoldBlock ZP: ')
    await guild.create_voice_channel('Emmy IGS: ')
    await guild.create_voice_channel('GoldIngot ZP:')
    await guild.create_voice_channel('IGS: ')
    await guild.create_voice_channel('ZP: ')

@client.command(pass_context=True)
async def ign(ctx):
    channel_updates = client.get_channel(606184739166093337)
    channel = ctx.message.channel
    if channel == channel_updates:
        member = ctx.message.author
        ign_nick = ctx.message.content.replace('.ign', '')
        guild = ctx.guild
        await guild.create_role(name= ign_nick)
        role = discord.utils.get(member.guild.roles, name=ign_nick)
        await client.add_roles(member, role)
    else:
        await client.send("Please use the #updates channel for this command!")


@client.command(pass_context=True)
async def emigs(ctx):
    channel_updates = client.get_channel(606184739166093337)
    channel_2 = ctx.message.channel
    igs_channel = client.get_channel(606185822013620225)
    if channel_2 == channel_updates:
        message_igs = ctx.message.content.replace('.emigs ', '')
        await igs_channel.edit(name="𝐄𝐦𝐦𝐲 𝐈𝐆𝐒: " + message_igs)
        time.sleep(5)
        msg = ctx.message
        await msg.delete()
    else:
        await channel_2.send('Please use the #updates Channel!')


@client.command(pass_context=True)
async def gbzp(ctx):
    channel_2 = ctx.message.channel
    spawner_channel = client.get_channel(606184739166093337)
    emigs_channel = client.get_channel(606185821480943617)
    if channel_2 == spawner_channel:
        message_igs = ctx.message.content.replace('.gbzp ', '')
        await emigs_channel.edit(name="𝐆𝐨𝐥𝐝𝐁𝐥𝐨𝐜𝐤 𝐙𝐏: " + message_igs)
        time.sleep(5)
        msg = ctx.message
        await msg.delete()
    else:
        await channel_2.send("Please use the #updates Channel!")


@client.command(pass_context=True)
async def igs(ctx):
    channel_2 = ctx.message.channel
    spawner_channel = client.get_channel(606184739166093337)
    igs_channel = client.get_channel(606185823657918622)
    if channel_2 == spawner_channel:
        message_igs = ctx.message.content.replace('.igs ', '')
        await igs_channel.edit(name="𝐈𝐆𝐒: " + message_igs)
        time.sleep(5)
        msg = ctx.message
        await msg.delete()
    else:
        await channel_2.send("Please use the #updates Channel!")

@client.command(pass_context=True)
async def zp(ctx):
    channel_2 = ctx.message.channel
    spawner_channel = client.get_channel(606184739166093337)
    zp_channel = client.get_channel(606185825595817984)
    if channel_2 == spawner_channel:
        message_igs = ctx.message.content.replace('.zp ', '')
        await zp_channel.edit(name="𝐙𝐏: " + message_igs)
        time.sleep(5)
        msg = ctx.message
        await msg.delete()
    else:
        await channel_2.send("Please use the #updates Channel!")


@client.command(pass_context=True)
async def gizp(ctx):
    channel_2 = ctx.message.channel
    spawner_channel = client.get_channel(606184739166093337)
    gizp_channel = client.get_channel(606185823058264069)
    if channel_2 == spawner_channel:
        message_igs = ctx.message.content.replace('.gizp ', '')
        await gizp_channel.edit(name="𝐆𝐨𝐥𝐝𝐈𝐧𝐠𝐨𝐭 𝐙𝐏: " + message_igs)
        time.sleep(5)
        msg = ctx.message
        await msg.delete()
    else:
        await channel_2.send("Please use the #updates Channel!")


@client.command(pass_context = True)
async def clear(ctx, amount = 100):
    channel = ctx.message.channel
    messages = []
    if amount < 2:
        await channel.send('You must delete atlesast 2 messages!')
    else:
        async for message in channel.history(limit = int(amount)):
            messages.append(message)
        await channel.delete_messages(messages)
        await channel.send('Messages Deleted  :white_check_mark: ')
        time.sleep(3)
        async for message in channel.history(limit = int(1)):
            messages.append(message)
        await message.delete()


url = "https://www.youtube.com/channel/UCpxak_b7Du_WDsNh_obiixQ"
req = Request(url)
page = urlopen(req).read()
soup = BeautifulSoup(page, 'html.parser')
spans = soup.find('div', {"id" : "content"})
lines = spans.get_text()
live = "Live now"


async def vxniilive():
    url = "https://www.youtube.com/channel/UCpxak_b7Du_WDsNh_obiixQ"
    req = Request(url)
    page = urlopen(req).read()
    soup = BeautifulSoup(page, 'html.parser')
    spans = soup.find('div', {"id": "content"})
    lines = spans.get_text()
    live = "Live now"
    while live in lines:
        vxnii = client.get_channel(662231539756564493)
        await vxnii.edit(name="tylerlv3: Live on YT")
        await vxniilive()
    else:
        vxnii = client.get_channel(662231539756564493)
        await vxnii.edit(name="tylerlv3: Not live")
        await vxniilive()


async def shawnlive():
    url = "https://www.youtube.com/channel/UCJAfPdnOvdVILbJdbfcPy2Q"
    req = Request(url)
    page = urlopen(req).read()
    soup = BeautifulSoup(page, 'html.parser')
    spans = soup.find('div', {"id": "content"})
    lines = spans.get_text()
    live = "Live now"
    while live in lines:
        shawn = client.get_channel(662236638801559572)
        await shawn.edit(name="CocBoyJb: live on YT")
        await shawnlive()
    else:
        shawn = client.get_channel(662236638801559572)
        await shawn.edit(name="CocBoyJb: Not live")
        await shawnlive()


client.run(TOKEN)
