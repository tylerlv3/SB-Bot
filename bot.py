import discord
from discord.ext import commands
import time
from bs4 import BeautifulSoup as soup
import os

from urllib.request import  Request, urlopen


TOKEN = 'NjA1OTU0MDQwMjc4NTQ4NTEw.XUEDDg.DPAg8PAZkIB4bVEazwFI0dkkMns'
client = commands.Bot(command_prefix='.')
client.remove_command('help')
client.remove_command('play')

channel_updates = client.get_channel(629484048888233987)


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.command(pass_context=True)
async def istop(ctx):
    channel = ctx.message.channel
    istop_channel = client.get_channel(629487594643783680)
    if channel == channel_updates:
        istop_lvl = ctx.message.content.replace('.istop', '')
        await istop_channel.edit(name="🔝 𝐈𝐬 𝐓𝐨𝐩 𝐑𝐚𝐧𝐤: " + istop_lvl)
        time.sleep(10)
        msg = ctx.message
        await msg.delete()

@client.command(pass_context=True)
async def isworth(ctx):
    channel = ctx.message.channel
    istop_channel = client.get_channel(629487841172520980)
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
    await guild.create_voice_channel('Emmy IGS: ')
    await guild.create_voice_channel('Coal IGS: ')
    await guild.create_voice_channel('IGS:')
    await guild.create_voice_channel('Mutant Cows: ')
    await guild.create_voice_channel('Iron Cows: ')
    await guild.create_voice_channel('Cows: ')

@client.command(pass_context=True)
async def ign(ctx):
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
    channel_updates = client.get_channel(629484048888233987)
    channel_2 = ctx.message.channel
    spawner_channel = client.get_channel(629483443201376257)
    if channel_2 == channel_updates:
        message_igs = ctx.message.content.replace('.emigs ', '')
        await spawner_channel.edit(name="𝐄𝐦𝐦𝐲 𝐈𝐆𝐒: " + message_igs)
        time.sleep(5)
        msg = ctx.message
        await msg.delete()
    else:
        await channel_2.send('Please use the #updates Channel!')


@client.command(pass_context=True)
async def cigs(ctx):
    channel_updates = client.get_channel(629484048888233987)
    channel_2 = ctx.message.channel
    spawner_channel = client.get_channel(629483443885047818)
    if channel_2 == channel_updates:
        message_igs = ctx.message.content.replace('.cigs ', '')
        await spawner_channel.edit(name="𝐂𝐨𝐚𝐥 𝐈𝐆𝐒: " + message_igs)
        time.sleep(5)
        msg = ctx.message
        await msg.delete()
    else:
        await channel_2.send("Please use the #updates Channel!")


@client.command(pass_context=True)
async def igs(ctx):
    channel_updates = client.get_channel(629484048888233987)
    channel_2 = ctx.message.channel
    spawner_channel = client.get_channel(629483443977322500)
    if channel_2 == channel_updates:
        message_igs = ctx.message.content.replace('.igs ', '')
        await spawner_channel.edit(name="𝐈𝐆𝐒: " + message_igs)
        time.sleep(5)
        msg = ctx.message
        await msg.delete()
    else:
        await channel_2.send("Please use the #updates Channel!")

@client.command(pass_context=True)
async def mcows(ctx):
    channel_updates = client.get_channel(629484048888233987)
    channel_2 = ctx.message.channel
    spawner_channel = client.get_channel(629483445147533312)
    if channel_2 == channel_updates:
        message_igs = ctx.message.content.replace('.mcows ', '')
        await spawner_channel.edit(name="𝐌𝐮𝐭𝐚𝐧𝐭 𝐂𝐨𝐰𝐬: " + message_igs)
        time.sleep(5)
        msg = ctx.message
        await msg.delete()
    else:
        await channel_2.send("Please use the #updates Channel!")


@client.command(pass_context=True)
async def icows(ctx):
    channel_updates = client.get_channel(629484048888233987)
    channel_2 = ctx.message.channel
    spawner_channel = client.get_channel(629483445407711243)
    if channel_2 == channel_updates:
        message_igs = ctx.message.content.replace('.icows ', '')
        await spawner_channel.edit(name="𝐈𝐫𝐨𝐧 𝐂𝐨𝐰𝐬: " + message_igs)
        time.sleep(5)
        msg = ctx.message
        await msg.delete()
    else:
        await channel_2.send("Please use the #updates Channel!")@client.command(pass_context=True)
        
@client.command(pass_context=True)
async def cows(ctx):
    channel_updates = client.get_channel(629484048888233987)
    channel_2 = ctx.message.channel
    spawner_channel = client.get_channel(629483445667627028)
    if channel_2 == channel_updates:
        message_igs = ctx.message.content.replace('.cows ', '')
        await spawner_channel.edit(name="𝐂𝐨𝐰𝐬: " + message_igs)
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

client.run(str(os.environ.get('BOT_TOKEN')))

