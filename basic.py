#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import time
import random
import curtime
import aiohttp
import asyncio
import discord
import settings
from discord.ext import commands

clock_emoji = ["🕐", "🕑", "🕒", "🕓", "🕔", "🕕", "🕖", "🕗", "🕘", "🕙", "🕚", "🕛"]


class Basic:
    def __init__(self, client):
        self.client = client

    print("Loading Basic...")

    async def on_message(self, message):
        # Message author variables
        user_id = message.author.id
        user_name = message.author

        if message.content.upper().startswith(".TIME"):
            print("{0}: {1} requested the time".format(curtime.get_time(), user_name))
            await self.client.send_message(
                message.channel, "I think it's `{}` {}".format(curtime.get_time(), random.choice(clock_emoji)))

        try:
            if settings.shut_up_role in [role.id for role in message.author.roles]:
                print("{0}: Told {1} to shaddup".format(curtime.get_time(), user_name))
                await self.client.send_message(message.channel, "Shut up <@{}>".format(user_id))
        except (IndexError, AttributeError):
            print("{}: Couldn't find user roles. It's probably a webhook or a message via DM's (Basic)".format(
                curtime.get_time()))

        if message.content.upper().startswith(".ABOUT"):
            file_name = os.path.basename(sys.argv[0])  # Gets file name

            print("{0}: {1} requested '.ABOUT'".format(curtime.get_time(), user_name))
            embed = discord.Embed(title="Github", url="https://github.com/Mehvix/synapsBot", color=settings.embed_color)
            embed.set_author(name="About:", url="https://steamcommunity.com/id/Mehvix/")
            embed.set_thumbnail(url="https://goo.gl/FCddaV")
            embed.add_field(name="Creator:", value="Mehvix#7172", inline=True)
            embed.add_field(name="File Version:", value=file_name[10:-3])
            embed.add_field(name="Python Version:", value=sys.version.split()[0])
            embed.add_field(name="Discord.py Version:", value=discord.__version__)
            embed.add_field(name="Client Version:", value=settings.get_version())
            await self.client.send_message(message.channel, embed=embed)

        if message.content.upper().startswith(".HELP"):
            if message.content.upper().startswith(".HELP BASIC"):
                embed = discord.Embed(title="Basic Commands", description="Everyone can use these commands.",
                                      color=settings.embed_color)
                embed.add_field(name=".time", value="Returns the time", inline=False)
                embed.add_field(name=".about", value="Gives info about the bot", inline=False)
                embed.add_field(name=".ping", value="Pong!", inline=False)
                embed.set_footer(text="You can also try `.help verified`, `.help admin`, & `.help karma`")
                await self.client.send_message(message.channel, embed=embed)
                return
            if message.content.upper().startswith(".HELP VERIFIED"):
                embed = discord.Embed(title="Verified Commands",
                                      description="Only Verified members can use these commands.",
                                      color=settings.embed_color)
                embed.add_field(name=".ud word", value="Urban Dictionary's definition of 'word'", inline=False)
                embed.add_field(name=".8ball +question", value="200% accurate answers", inline=False)
                embed.add_field(name=".version", value="What version the bot is running", inline=False)
                embed.add_field(name=".uptime", value="How long the bot has been online", inline=False)
                embed.add_field(name=".bear", value="Random bear gif", inline=False)
                embed.add_field(name=".sam", value="Random Sam picture", inline=False)
                embed.add_field(name=".apu", value="Random Apu picture", inline=False)
                embed.add_field(name=".serverinfo", value="Information about the server", inline=False)
                embed.add_field(name=".emotes", value="All custom emotes the server uses", inline=False)
                embed.add_field(name=".beta", value="Gain access to the beta testing server", inline=False)
                embed.add_field(name=".whois +@name", value="Information about a user", inline=False)
                embed.add_field(name=".banlist", value="Lists all members who are banned from the server", inline=False)
                embed.add_field(name=".createinvite", value="Creates a invite that lasts forever and is unique",
                                inline=False)
                embed.add_field(name=".roulette", value="Gamble your karma", inline=False)
                embed.add_field(name=".karma", value="Your karma", inline=False)
                embed.add_field(name=".karma @name", value="(@Name's) karma", inline=False)
                embed.add_field(name=".level", value="Your level", inline=False)
                embed.add_field(name=".level @name", value="(@Name's) level", inline=False)
                embed.set_footer(text="You can also try `.help basic`, `.help admin`, & `.help karma`")
                await self.client.send_message(message.channel, embed=embed)
                return
            if message.content.upper().startswith(".HELP ADMIN"):
                embed = discord.Embed(title="Admin Commands", description="Only Admins can use these commands.",
                                      color=settings.embed_color)
                embed.add_field(name=".serverrules", value="Returns the rules of the server", inline=False)
                embed.add_field(name=".givekarma", value="Abuse of this will get your admin revoked", inline=False)
                embed.add_field(name=".mute @name", value="Adds muted role to @name", inline=False)
                embed.add_field(name=".unmute @name", value="Removes the muted role of @name", inline=False)
                embed.add_field(name=".banword +word", value="Adds(word) to list of banned words", inline=False)
                embed.add_field(name=".ban @name", value="Bans (name)", inline=False)
                embed.add_field(name=".unban @name", value="Unbans (name)", inline=False)
                embed.add_field(name=".kick @name", value="Kicks (@name)", inline=False)
                embed.add_field(name=".clear +number", value="Clears (number) amount of messages", inline=False)
                embed.set_footer(text="You can also try `.help verified`, `.help admin`, & `.help karma`")
                await self.client.send_message(message.channel, embed=embed)
                return
            if message.content.upper().startswith(".HELP KARMA"):
                embed = discord.Embed(title="Karma Info", color=settings.embed_color)
                embed.add_field(name="How to get karma:", value="You get 1 karma for every message in the server, "
                                                                "and 5 karma for each upvote emote someone gives your "
                                                                "message/image. For each 100 karma you get you level "
                                                                "up once which will change your color in the server. "
                                                                "You can also gamble it via the .roulette command",
                                inline=False)
                embed.set_footer(text="You can also try `.help verified`, `.help admin`, & `.help basic`")
                await self.client.send_message(message.channel, embed=embed)
                return
            else:
                print("{0}: {1} requested '.HELP'".format(curtime.get_time(), user_name))
                embed = discord.Embed(title="Help Commands", color=settings.embed_color)
                embed.add_field(name=".help basic", value="Commands everyone can use.", inline=False)
                embed.add_field(name=".help verified", value="Commands only verified members can use.", inline=False)
                embed.add_field(name=".help admin", value="Commands only admins can use.", inline=False)
                await self.client.send_message(message.channel, embed=embed)

        if message.content.upper().startswith(".MENTION"):
            if not message.raw_mentions:
                await self.client.send_message(message.channel, "You need to `@` a user")
            else:
                await self.client.send_message(message.channel, "You mentioned: <@{}>".format(message.raw_mentions[0]))


def setup(client):
    client.add_cog(Basic(client))
