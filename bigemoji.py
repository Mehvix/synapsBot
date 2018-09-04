#!/usr/bin/env python
# -*- coding: utf-8 -*-


import discord
import aiohttp
import asyncio

from discord.ext import commands


class Bigemoji:
    def __init__(self, client):
        self.client = client
        self.session = aiohttp.ClientSession()


    print("Loading Bigemoji...")

    async def on_message(self, message):
        # Message author variables
        user_id = message.author.id
        user_name = message.author


def setup(client):
    client.add_cog(Bigemoji(client))
