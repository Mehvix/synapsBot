#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import discord
import settings
from discord.ext import commands


class Typeracer:
    def __init__(self, client):
        self.client = client
        self.session = self.client.http.session

    print("Loading Typeracer...")

    async def on_message(self, message):
        # Message author variables
        user_id = message.author.id
        user_name = message.author

        if message.content.upper().startswith(".TR "):
            user = message.content[4:]
            search = "https://data.typeracer.com/users?id=tr:{}".format(user)
            async with self.session.get(search) as r:
                result = await r.json()
            try:
                embed = discord.Embed(description="[Add {0} on Typeracer]("
                                                  "https://data.typeracer.com/pit/friend_request?user={0})".format(user)
                                      , color=settings.embed_color)
                embed.set_author(name="{}'s Type Racer Stats:".format(user))
                embed.add_field(name="Name:", value=result["name"] + " " + result["lastName"], inline=True)
                embed.add_field(name="Country:", value=str(result["country"]).upper(), inline=True)
                embed.add_field(name="Points:", value=str(result["tstats"]["points"])[:10], inline=True)
                embed.add_field(name="Level:", value=result["tstats"]["level"], inline=True)
                embed.add_field(name="Games Won:", value=result["tstats"]["gamesWon"], inline=True)
                embed.add_field(name="Best WPM:", value=str(result["tstats"]["bestGameWpm"])[:10], inline=True)
                embed.add_field(name="Average WPM:", value=str(result["tstats"]["wpm"])[:10], inline=True)
                # embed.add_field(name="Recent WPM:", value=str(result["tstats"]["recentScores"]), inline=True)
                embed.add_field(name="Average Recent WPM:", value=str(result["tstats"]["recentAvgWpm"])[:10],
                                inline=True)
                embed.set_thumbnail(url="https://data.typeracer.com/public/images/avatars/{}".format(result["avatar"]))

                await self.client.send_message(message.channel, embed=embed)
            except TypeError:
                await self.client.send_message(message.channel, "That user doesn't exist :(")


def setup(client):
    client.add_cog(Typeracer(client))
