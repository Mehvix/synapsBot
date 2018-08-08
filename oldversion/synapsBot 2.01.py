import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import os
import sys


Client = discord.Client()
client = commands.Bot(command_prefix=".")


@client.event
async def on_ready():
    file_name = os.path.basename(sys.argv[0])
    await client.change_presence(game=discord.Game(name='Version {}'.format(file_name[10:])))
    servers = list(client.servers)
    print('==============================')
    print('• Client Name: {}'.format(client.user.name))
    print('• Client ID:   {}'.format(client.user.id))
    print(' ')
    print('• Connected to ' + str(len(client.servers)) + ' server(s):')
    for x in range(len(servers)):
        print('> ' + servers[x-1].name)
    print('==============================')


@client.event
async def on_resumed():
    print("Resumed.")


@client.event
async def on_message(message):
    user_id = message.author.id
    user_auth = message.author

    # ".accept" code
    role = discord.utils.get(message.server.roles, name="Member 🔸")
    if '312693233329373194' not in [role.id for role in message.author.roles]:
        if message.content.upper().startswith('.ACCEPT'):
            await client.add_roles(message.author, role)
            await client.delete_message(message)
            await client.send_message(discord.Object(id="412075980094570506"), "<@{}> just joined!".format(user_id))
        else:
            await client.delete_message(message)

    # "Shut Up" code
    if '414245504537591810' in [role.id for role in message.author.roles]:
        await client.send_message(message.channel, "Shut up <@{}>".format(user_id))


@client.event
async def on_reaction_add(message):
    if message.content.upper()('HTTP'):
        await client.add_reaction(message, 'upvote:412119803034075157, downvote:412119802904313858')
        await client.wait_for_reaction(['upvote:412119803034075157', 'downvote:412119802904313858'])


client.run("TOKEN")
