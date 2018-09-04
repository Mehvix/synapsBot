# coding=utf-8

import os
import sys
import json
import time
import karma
import curtime
import discord
import settings
from discord.ext import commands
from datetime import datetime, timedelta


class AdminRW:
    def __init__(self, client):
        self.client = client

    print("Loading Admin_ext...")f


def setup(client):
    client.add_cog(AdminRW(client))
