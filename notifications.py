#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import curtime
import discord
import settings
from discord.ext import commands

ban_message = 0


class Notifications:
    def __init__(self, client):
        self.client = client

    print("Loading Notifications...")

    async def on_member_join(self, member):
        member_created_at_date = str(member.created_at).split('.', 1)[0]
        avatar = member.avatar_url if member.avatar else member.default_avatar_url

        print("{0}: {1} joined".format(curtime.get_time(), member.name))
        embed = discord.Embed(color=settings.embed_color)
        embed.set_author(name="{} joined the server!".format(member.name))
        embed.add_field(name="Username:", value="{}#{}".format(member.name, member.discriminator), inline=False)
        embed.add_field(name="Time Joined:", value=curtime.get_time(), inline=False)
        embed.add_field(name="Account Created at:", value=member_created_at_date, inline=False)
        embed.add_field(name="User Avatar URL", value=member.avatar_url)
        embed.set_thumbnail(url=avatar)

        await self.client.send_message(
            discord.Object(id=settings.notification_channel), embed=embed)

    async def on_member_ban(self, member):
        global ban_message
        ban_message += 1
        print('{0}: {1} was banned'.format(curtime.get_time(), member))
        await self.client.send_message(
            discord.Object(id=settings.notification_channel), "<@{}> was **banned** :hammer: \nYou can find out who "
                                                              "banned them by checking the audit log".format(member.id))

    async def on_member_unban(self, member):
        print("{0}: {1} was unbanned".format(curtime.get_time(), member))
        await self.client.send_message(discord.Object(id=settings.settings.notification_channel),
                                       "<@{}> was **unbanned** :hammer: \nYou can find out who unbanned them by checkin"
                                       "g the audit log".format(member.id))

    async def on_member_remove(self, member):
        global ban_message
        if ban_message == 1:
            print("{}: Canceled kick message".format(curtime.get_time()))
            ban_message = 0
        else:
            print("{0}: {1} left or was kicked".format(curtime.get_time(), member))
            await self.client.send_message(
                discord.Object(id=settings.notification_channel), "<@{}> was either kicked or left the server "
                                                                  ":frowning2:".format(member.id))
            ban_message = 0


def setup(client):
    client.add_cog(Notifications(client))
