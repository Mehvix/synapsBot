#!/usr/bin/env python
# -*- coding: utf-8 -*-

import discord
from discord.ext import commands


class Verified:
    def __init__(self, client):
        self.client = client

    print("Loading Verified...")

    async def on_message(self, message):
        # Message author variables
        user_id = message.author.id
        user_name = message.author


def setup(client):
    client.add_cog(Verified(client))
