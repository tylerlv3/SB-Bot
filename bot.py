import discord
from discord.ext import commands
import time
from bs4 import BeautifulSoup as soup

from urllib.request import  Request, urlopen


TOKEN = 'NjA1OTU0MDQwMjc4NTQ4NTEw.XUEDDg.DPAg8PAZkIB4bVEazwFI0dkkMns'
client = commands.Bot(command_prefix='.')
client.remove_command('help')
client.remove_command('play')

channel_updates = client.get_channel(606184739166093337)


@client.event
async def on_ready():
    pcc = client.get_channel(606204142293352468)
    await pcc.edit(name="🙋‍ Players: " + aml_2)
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

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
async def clear(ctx, amount = 50):
    channel = ctx.message.channel
    messages = []
    if amount < 2:
        await client.send('You must delete atlesast 2 messages!')
        async for message in client.logs_from(channel, limit = int(amount)):
            messages.append(message)
            await client.delete_messages(messages)
            await client.say('Messages Deleted.')

url="https://minecraftlist.com/servers/pvpwars.net"
req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})

web_byte = urlopen(req).read()

webpage = web_byte.decode('utf-8')
page_souped = soup(webpage, "html.parser")
bc_price = page_souped.find("div", {
    "class": "fl w-100 w-34-ns border-box ph2 ph3-ns mb3"
})


player_count = bc_price.get_text()


pcc = client.get_channel(606204142293352468)
player_count_clean = player_count.replace("There's room for 404 more players.", '' )



url_2="https://minecraftlist.com/servers/pvpwars.net"
req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})

web_byte = urlopen(req).read()

webpage = web_byte.decode('utf-8')
page_souped = soup(webpage, "html.parser")
bc_price_2 = page_souped.find("div", {
    "class": "fl w-100 w-34-ns border-box ph2 ph3-ns mb3"
})
bc_price_3 = bc_price_2.find("p", {
    "class": "f4 f2-ns ma0 mb2"
})
aml = bc_price_3.get_text()
aml_2 = aml.strip()
client.run(TOKEN)

