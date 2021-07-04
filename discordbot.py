import discord
import os
import json
import random as rand
import time
from discord import embeds
from discord.colour import Color
from discord.ext import commands

client = commands.Bot(command_prefix = '.')
token = '************************************'
os.chdir('C:\Storage A\BOT')

#-------------------------- LEVEL --------------------------------------
lv1 = 1000
lv2 = 2500
lv3 = 5000
lv4 = 7000
lv5 = 10000

#-------------------------- ITEMS FIELD --------------------------------
dirt = 1
stone = 2
coal = 400

#-------------------------- ITEMS MOUNTAIN -----------------------------
coal = 4
gold = 8
emerald = 10


@client.event
async def on_ready():
    print(f"Connected succesfully as {client.user}")

@client.command()
async def balance(ctx):
    await open_account(ctx.author)
    user = ctx.author
    users = await get_data()

    level_amt = users[str(user.id)]['level']
    xp_amt = users[str(user.id)]['xp']
    dirt_amt = users[str(user.id)]['dirt']
    stone_amt = users[str(user.id)]['stone']
    wallet_amt = users[str(user.id)]['wallet']

    em = discord.Embed(title = f'{ctx.author.name} balance', color=0x00ff00)
    em.add_field(name="Level", value=level_amt, inline=True)
    em.add_field(name="XP", value='{}/{}'.format(xp_amt,lv1), inline=True)
    em.add_field(name="Coins", value=wallet_amt, inline=True)
    em.add_field(name="Dirt", value=dirt_amt, inline=False)
    em.add_field(name="Stone", value=stone_amt, inline=False)
    em.set_footer(text="made by @alvinabner")
    await ctx.send(embed=em)

@client.command()
async def balance(ctx):
    await open_account(ctx.author)
    user = ctx.author
    users = await get_data()

    level_amt = users[str(user.id)]['level']
    xp_amt = users[str(user.id)]['xp']
    dirt_amt = users[str(user.id)]['dirt']
    stone_amt = users[str(user.id)]['stone']
    wallet_amt = users[str(user.id)]['wallet']

    em = discord.Embed(title = f'{ctx.author.name} balance', color=0x00ff00)
    em.add_field(name="Level", value=level_amt, inline=True)
    em.add_field(name="XP", value='{}/{}'.format(xp_amt,lv1), inline=True)
    em.add_field(name="Coins", value=wallet_amt, inline=True)
    em.add_field(name="Dirt", value=dirt_amt, inline=False)
    em.add_field(name="Stone", value=stone_amt, inline=False)
    em.set_footer(text="made by @alvinabner")
    await ctx.send(embed=em)

@client.command()
async def mine(ctx):
    await open_account(ctx.author)
    user = ctx.author
    users = await get_data()
    earnings1 = rand.randrange(6,16)
    earnings2 = rand.randrange(1,11)

    x = rand.randrange(1,4)
    em = discord.Embed(title = f'{ctx.author.name} has mined!', color=0x00ff00)
    earn1 = earnings1
    earn2 = earnings2
    if x == 1:
        xptotal = earn1
        em.add_field(name = f'You got', value=f'{earn1} Dirt\n+{xptotal} XP', inline=False)
    elif x == 2:
        xptotal = earn1 + (earn2*2)
        em.add_field(name = f'You got', value=f'{earnings1} Dirt\n{earnings2} Stone\n+{xptotal} XP', inline=False)
    elif x == 3:
        xptotal = earn2*2
        em.add_field(name = f'You got', value=f'{earnings2} Stone\n+{xptotal} XP', inline=False)
    await ctx.send(embed=em)

    users[str(user.id)]['dirt'] += earnings1
    users[str(user.id)]['stone'] += earnings2
    users[str(user.id)]['xp'] += xptotal

    with open('data.json', 'w') as f:
        json.dump(users,f)

async def open_account(user):
    users = await get_data()
    with open('data.json', 'r') as f:
        users = json.load(f)

    if str(user.id) in users:
        return False
    else:
        users[str(user.id)] = {}
        users[str(user.id)]['level'] = 1
        users[str(user.id)]['xp'] = 0
        users[str(user.id)]['wallet'] = 0
        users[str(user.id)]['dirt'] = 0
        users[str(user.id)]['stone'] = 0

    with open('data.json', 'w') as f:
        json.dump(users, f)
    return True

async def get_data():
    with open('data.json', 'r') as f:
        users = json.load(f)
    return users



@client.command()
async def sellall(ctx):
    await open_account(ctx.author)
    user = ctx.author
    users = await get_data()

    wallet_amt = (users[str(user.id)]['dirt']*1) + (users[str(user.id)]['stone']*2)

    em = discord.Embed(title = f'{ctx.author.name} balance', color=0x00ff00)
    em.add_field(name="You sold all your inventory!", value='You got ${}'.format(wallet_amt), inline=True)
    await ctx.send(embed=em)

    users[str(user.id)]['wallet'] += wallet_amt
    users[str(user.id)]['dirt'] = 0
    users[str(user.id)]['stone'] = 0

    with open('data.json', 'w') as f:
        json.dump(users,f)

async def open_account(user):
    users = await get_data()
    with open('data.json', 'r') as f:
        users = json.load(f)

    if str(user.id) in users:
        return False
    else:
        users[str(user.id)] = {}
        users[str(user.id)]['level'] = 1
        users[str(user.id)]['xp'] = 0
        users[str(user.id)]['wallet'] = 0
        users[str(user.id)]['dirt'] = 0
        users[str(user.id)]['stone'] = 0

    with open('data.json', 'w') as f:
        json.dump(users, f)
    return True

async def get_data():
    with open('data.json', 'r') as f:
        users = json.load(f)
    return users

client.run(token)
