#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
  'forwarding.py' is port of a port from another bot:
  Original:   https://github.com/jacobcheatley/dankbot
  Import:     https://github.com/aikaterna/aikaterna-cogs/blob/master/away/away.py
"""


import discord
import settings
from discord.ext import commands


class Forwarding:
    def __init__(self, client):
        self.client = client

    print("Loading Forwarding...")

    async def on_message(self, message):
        if not message.channel.is_private or message.channel.user.id == "196355904503939073":
            return

        embed = discord.Embed(color=settings.embed_color)
        if message.author == self.client.user:
            embed.title = 'Sent PM to {}#{} ({}).'.format(message.channel.user.name, message.channel.user.discriminator,
                                                          message.channel.user.id)
        else:
            embed.set_author(name=message.author,
                             icon_url=message.author.avatar_url or message.author.default_avatar_url)
            embed.title = '{} messaged me:'.format(message.channel.user.id)
        embed.description = message.content
        embed.timestamp = message.timestamp

        user = await self.client.get_user_info(196355904503939073)
        await self.client.send_message(user, embed=embed)


def setup(client):
    client.add_cog(Forwarding(client))

