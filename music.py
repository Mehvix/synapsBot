#!/usr/bin/env python
# -*- coding: utf-8 -*-

import discord
import youtube_dl
from itertools import *
from discord.ext import commands

# Music bot setting(s)
players = {}
queues = {}


class Music:
    def __init__(self, client):
        self.client = client

    print("Loading Music...")

    if not discord.opus.is_loaded():
        # the 'opus' library here is opus.dll on windows
        # or libopus.so on linux in the current directory
        # you should replace this with the location the
        # opus library is located in and with the proper filename.
        # note that on windows this DLL is automatically provided for you
        discord.opus.load_opus('opus')

    async def on_message(self, message):
        server = message.server

        # Join VC (test)
        if message.content.upper().startswith(".VOICETEST"):
            if self.client.is_voice_connected(server):
                pass
            else:
                try:
                    voice = await self.client.join_voice_channel(message.author.voice.voice_channel)
                    voice_client = self.client.voice_client_in(server)

                    try:
                        player = voice.create_ffmpeg_player('media/jerma.mp3')
                        player.start()
                        players[server.id] = player
                        await self.client.send_message(message.channel,
                                                       "Joining `{}`".format(voice_client.channel.name))

                    except UnboundLocalError:
                        await self.client.send_message(
                            message.channel, "I am already playing in `{}`".format(voice_client.channel.name))

                except discord.InvalidArgument:
                    await self.client.send_message(message.channel, "You aren't in a voice channel")
                    return

        if message.content.upper().startswith(".PLAY"):
            if self.client.is_voice_connected(server):
                pass
            else:
                try:
                    voice = await self.client.join_voice_channel(message.author.voice.voice_channel)
                except discord.InvalidArgument:
                    await self.client.send_message(message.channel, "You aren't in a voice channel")
                    return

            url = message.content.split
            url = url()[1]
            voice_client = self.client.voice_client_in(server)
            player = await voice_client.create_ytdl_player(url)
            players[server.id] = player
            player.start()

        if message.content.upper().startswith(".PAUSE"):
            server_id = message.server.id
            players[server_id].pause()

        if message.content.upper().startswith(".STOP"):
            server_id = message.server.id
            players[server_id].stop()

        if message.content.upper().startswith(".RESUME"):
            server_id = message.server.id
            players[server_id].resume()

        if message.content.upper().startswith(".QUEUE"):
            url = message.content.split
            url = url()[1]

            voice.client = self.client.voice_client_in(server)
            player = await voice.client.create_ytdl_player(url, after=lambda: check_queue(sever.id))

            if server.id in queues:
                queues[server.id].append(player)
            else:
                queues[server.id] = [player]

            await self.client.send_message(message.channel, "Video added to que!")

        if message.content.upper().startswith(".LEAVE"):
            for x in self.client.voice_clients:
                if x.server == server:
                    voice_client = self.client.voice_client_in(server)
                    await self.client.send_message(message.channel, "Leaving {}".format(voice_client.channel.name))
                    return await x.disconnect()
            await self.client.send_message(message.channel, "I am not connected to any voice channel on this server.")


def setup(client):
    client.add_cog(Music(client))
