#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import json
import discord
from discord.ext import commands

Client = discord.Client()
client = commands.Bot(command_prefix=".")


def get_json(file_path):
    with open(file_path, 'r') as fp:
        return json.load(fp)


def server(server):
    global token
    global upvote_emoji
    global downvote_emoji
    global notification_channel
    global member_role_id
    global member_role_name
    global shut_up_role
    global admin_role_name
    global verified_role_id
    global admin_role_id
    global verified_role_name
    global pokemon_channel
    global mute_role_id
    global mute_role_name
    global embed_color
    embed_color = 0x1abc9c

    if server == "test":
        jsontoken = get_json('tokens.json')
        token = jsontoken.get("test")
        upvote_emoji = ":upvote:414204250642579488"
        downvote_emoji = ":downvote:414204250948894721"
        notification_channel = "414974032048553984"
        member_role_id = "414683704737267712"
        member_role_name = "Member 🔸"
        shut_up_role = "414237651504332800"
        admin_role_name = "Admin 💠"
        admin_role_id = "439175903600181269"
        verified_role_name = "Verified 🔰"
        verified_role_id = "439191092991229992"
        pokemon_channel = "439198154324181002"  # N/A
        mute_role_id = "445059188973109259"
        mute_role_name = "Text Muted"
        return
    if server == "main":
        print("Using MAIN account")
        jsontoken = get_json('tokens.json')
        token = jsontoken.get("main")
        upvote_emoji = ":upvote:412119803034075157"
        downvote_emoji = ":downvote:412119802904313858"
        notification_channel = "412075980094570506"
        member_role_id = "312693233329373194"
        member_role_name = "Member 🔸"
        admin_role_name = "Admin 💠"
        admin_role_id = "266701171002048513"
        shut_up_role = "414245504537591810"
        verified_role_name = "Verified 🔰"
        verified_role_id = "366739104203014145"
        pokemon_channel = "439198154324181002"
        mute_role_id = "363900817805148160"
        mute_role_name = "Text Muted"
    else:
        sys.exit("No Server (main/test)")
