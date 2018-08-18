#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
This is just for reference when creating cogs
"""

import discord
from discord.ext import commands


class __COG__:
    def __init__(self, client):
        self.client = client

    print("Loading __COG__...")

    async def on_message(self, message):
        # Message author variables
        user_id = message.author.id
        user_name = message.author


def setup(client):
    client.add_cog(__COG__(client))
