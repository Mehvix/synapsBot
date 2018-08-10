#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import math
import time
import random
import asyncio
import curtime
import discord
import datetime
import settings
from discord.ext import commands

# Resets uptime settings
seconds = 0
minutes = 0
hours = 0
days = 0

# Cogs being used
extensions = ['admin', 'karma', 'basic', 'notifications', 'verified', 'createpoll']

# Defines Client
client = commands.Bot(description="synapsBot", command_prefix='.')


# TODO New Commands
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
> Cool down
> Hearthstone cards (import hearthstone)
> Give XP for voice channel usage
> Remind me in x minutes
> save console to file
> GUI
> dont down these files
> .invite @user (dm user)
> change bot avatar every hour/launch 
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

# How to get custom values
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
You need the following values. They are custom for every server. You can get them by typing in any text channel the 
desired value with a "\" in front of it. I.E. "\@Member" or "\:upvote:"
For your token go to https://discordapp.com/developers/applications/me, creating a new app, and getting the token by 
clicking "reveal".
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

'''''
Make sure to change this to either 'test' or 'main'
'''''
settings.set_server("main")

ban_message = 0


def get_json(file_path):
    with open(file_path, 'r') as fp:
        return json.load(fp)


async def timer():
    await client.wait_until_ready()
    global seconds
    seconds = 0
    global minutes
    minutes = 0
    global hours
    hours = 0
    global days
    days = 0
    while not client.is_closed:
        await asyncio.sleep(1)
        seconds += 1
        if seconds == 60:
            seconds = 0
            minutes += 1
            file_name = os.path.basename(sys.argv[0])  # Gets file name
            r = random.randint(1, 3)
            if r == 1:
                await client.change_presence(game=discord.Game(name="Live for {0}".format(curtime.uptime()),
                                                               url="https://twitch.tv/mehvix", type=1))
            if r == 2:
                await client.change_presence(game=discord.Game(name="Version {}".format(file_name[10:-3]),
                                                               url="https://twitch.tv/mehvix", type=1))
            if r == 3:
                await client.change_presence(
                    game=discord.Game(name="Created by Mehvix#7172", url="https://twitch.tv/mehvix",
                                      type=1))
        elif minutes == 60:
            minutes = 0
            hours += 1
        elif hours == 24:
            hours = 0
            days += 1


@client.event
async def on_ready():
    users = len(set(client.get_all_members()))
    channels = len([c for c in client.get_all_channels()])
    file_name = os.path.basename(sys.argv[0])  # Gets file name

    r = random.randint(2, 3)
    if r == 2:
        await client.change_presence(game=discord.Game(name="Version {}".format(file_name[10:-3]),
                                                       url="https://twitch.tv/mehvix", type=1))
    if r == 3:
        await client.change_presence(game=discord.Game(name="Created by Mehvix#7172", url="https://twitch.tv/mehvix",
                                                       type=1))
    server_list = list(client.servers)

    print("============================================================")
    print("                                      ____        __\n   _______  ______  ____ _____  _____/ __ )____  / /_")
    print("  / ___/ / / / __ \/ __ `/ __ \/ ___/ /_/ / __ \/ __/\n /__  / /_/ / / / / /_/ / /_/ /__  / /_/ / /_/ / /_")
    print("/____/\__, /_/ /_/\__,_/ .___/____/_____/\____/\__/\n     /____/           /_/\n")
    print("• Discord Version:           {}".format(discord.__version__))
    print("• Python Version:            {}".format(sys.version))
    print("• Start Time:                {}".format(curtime.get_time()))
    print("• Client Name:               {}".format(client.user))
    print("• Client ID:                 {}".format(client.user.id))
    print("• Channels:                  {}".format(channels))
    print("• Users:                     {}".format(users))
    print("• Connected to " + str(len(client.servers)) + " server(s):")
    for x in range(len(server_list)):
        print("     > " + server_list[x - 1].name)
    print("============================================================")


@client.event
async def on_resumed():
    print("{}: Resumed".format(curtime.get_time()))


@client.event
async def on_message(message):
    # Message author variables
    user_id = message.author.id
    user_name = message.author

    # ".Accept" code
    try:
        role = discord.utils.get(message.server.roles, name=settings.member_role_name)
        if settings.member_role_id not in [role.id for role in message.author.roles]:
            if message.content.upper().startswith(".ACCEPT"):
                await client.add_roles(user_name, role)
                await asyncio.sleep(1)
                await client.delete_message(message)
                await client.send_message(discord.Object(id=settings.notification_channel),
                                          "<@{}> is now a Member :ok_hand:".format(user_id))
                print("{0}: {1} joined the server (.accept)".format(curtime.get_time(), user_name))
            else:
                await asyncio.sleep(.1)
                await client.delete_message(message)
                print("{0}: DIDN'T type '.accept'".format(curtime.get_time(), user_name))
    except AttributeError:
        print("{}: Couldn't find user roles. It's probably a webhook or a message via DM's".format(curtime.get_time()))


@client.command()
async def load(extension_name: str):
    try:
        client.load_extension(extension_name)
        print("LOADED {}".format(extension_name))
    except (AttributeError, ImportError) as error:
        await print("```py\n{}: {}\n```".format(type(error).__name__, str(error)))
        return
    print("{} loaded.".format(extension_name))


@client.command()
async def unload(extension_name: str):
    client.unload_extension(extension_name)
    print("{} unloaded.".format(extension_name))


if __name__ == "__main__":
    for extension in extensions:
        try:
            client.load_extension(extension)
        except Exception as e:
            exc = '{}: {}'.format(type(e).__name__, e)
            print('Failed to load extension {}\n{}'.format(extension, exc))

    client.loop.create_task(timer())
    client.run(settings.token)
