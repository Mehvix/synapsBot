#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import discord
from discord.ext import commands


class Hearthstone:
    def __init__(self, client):
        self.client = client

    print("Loading Hearthstone...")

    async def on_message(self, message):
        # Message author variables
        user_id = message.author.id
        user_name = message.author

        if message.content.upper().startswith(".HS SETTINGS"):
            with open('hssettings.json', 'r') as fp:
                settings = json.load(fp)

                lang = settings["lang"]
            search = "https://api.hearthstonejson.com/v1/25770/{}/cards.collectible.json".format(lang)
            async with self.session.get(search) as r:
                result = await r.json()


        #if message.content.upper().startswith(".DECODE "):
        #    deckstring = message.content[8:]
        #    deck = hearthstone.deckstrings.Deck()
        #    deck = deckstrings.Deck().from_deckstring(deckstring)
        #    print(deck)


def setup(client):
    client.add_cog(Hearthstone(client))
