import discord
from discord.ext import commands
import time
from bs4 import BeautifulSoup
from urllib.request import  Request, urlopen
import sched
import threading

TOKEN = 'NjYyODU4NjAxNDA4MzY0NTY4.XhAG6g.gNF6vy6N6rfV_WTNUVVDw636agg'
client = commands.Bot(command_prefix='.')

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    channel = client.get_channel(662860176130441247)
    userChannel = message.channel
    messages = []
    if userChannel == channel:
        if message.author == client.user:
            pass
        else:
            if message.content == "GetVerified2020":
                await message.delete()
                user = message.author
                id = user.id
                embed3 = discord.Embed(title="Paid User Log", description= str(user) + "Has Successfully Verified Payment (ID: " + str(id) + " )", color=0xff0000)
                logs = str(user) + " Has Successfully Logged in (ID: " + str(id) + " )"
                paid = discord.utils.get(user.guild.roles, name="• Paid Users")
                verif = discord.utils.get(user.guild.roles, name="• Verified Users")
                await user.add_roles(paid)
                embed1 = discord.Embed(title="Welcome to Exotic Menu Services!", color=0x00ff00)
                await channel.send(embed=embed1)
                async for message in channel.history(limit=int(1)):
                    messages.append(message)
                logChan = client.get_channel(662898981134663690)
                await logChan.send(embed=embed3)
                time.sleep(4)
                await channel.delete_messages(messages)
                try:
                    await user.remove_roles(verif)
                except:
                    return
            else:
                if message.content == ".setup":
                    channel = client.get_channel(662860176130441247)
                    embed = discord.Embed(title="Payment Verification", description="To receive the Paid Users role in the discord and verify your payment for the menu please enter the password provided by your seller.", color=0xff0000)
                    async for message in channel.history(limit=int(1)):
                        messages.append(message)
                    await message.delete()
                    await channel.send(embed=embed)
                else:
                    embed2 = discord.Embed(title="Incorrect. Please Purchase to get verified.", color=0xff0000)
                    await channel.send(embed=embed2)
                    async for message in channel.history(limit=int(2)):
                        messages.append(message)
                    time.sleep(4)
                    await channel.delete_messages(messages)

    else:
        pass


client.run(TOKEN)
