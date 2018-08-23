#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import discord
import asyncio
import settings
from discord.ext import commands

red = ":red:481329772102942740"
orange = ":orange:481329772232704010"
yellow = ":yellow:481329771754553345"
green = ":green:481329615491563520"
blue = ":blue:481329615483437057"
indigo = ":indigo:481329772153012225"
violet = ":violet:481329771809210369"
white = ":white:481329771700289538"

emoji_color = ""


class Canvas:
    def __init__(self, client):
        self.client = client

    print("Loading Canvas...")

    async def on_message(self, message):
        if message.channel.id == settings.canvas_channel:
            if message.content.upper() == ".DRAW BLANK":
                if message.author.server_permissions.administrator:

                    await self.client.delete_message(message)
                    global emoji_color, line_content, a, b, c, d, e, f, g, h, i, j

                    a = await self.client.send_message(message.channel, "🇦 <{0}> <{0}> <{0}> <{0}> <{0}> <{0}> <{0}> <{0}> <{0}> <{0}>".format(white))
                    b = await self.client.send_message(message.channel, "🇧 <{0}> <{0}> <{0}> <{0}> <{0}> <{0}> <{0}> <{0}> <{0}> <{0}>".format(white))
                    c = await self.client.send_message(message.channel, "🇨 <{0}> <{0}> <{0}> <{0}> <{0}> <{0}> <{0}> <{0}> <{0}> <{0}>".format(white))
                    d = await self.client.send_message(message.channel, "🇩 <{0}> <{0}> <{0}> <{0}> <{0}> <{0}> <{0}> <{0}> <{0}> <{0}>".format(white))
                    e = await self.client.send_message(message.channel, "🇪 <{0}> <{0}> <{0}> <{0}> <{0}> <{0}> <{0}> <{0}> <{0}> <{0}>".format(white))
                    f = await self.client.send_message(message.channel, "🇫 <{0}> <{0}> <{0}> <{0}> <{0}> <{0}> <{0}> <{0}> <{0}> <{0}>".format(white))
                    g = await self.client.send_message(message.channel, "🇬 <{0}> <{0}> <{0}> <{0}> <{0}> <{0}> <{0}> <{0}> <{0}> <{0}>".format(white))
                    h = await self.client.send_message(message.channel, "🇭 <{0}> <{0}> <{0}> <{0}> <{0}> <{0}> <{0}> <{0}> <{0}> <{0}>".format(white))
                    i = await self.client.send_message(message.channel, "🇮 <{0}> <{0}> <{0}> <{0}> <{0}> <{0}> <{0}> <{0}> <{0}> <{0}>".format(white))
                    j = await self.client.send_message(message.channel, "🇯 <{0}> <{0}> <{0}> <{0}> <{0}> <{0}> <{0}> <{0}> <{0}> <{0}>".format(white))
                    await self.client.send_message(message.channel, ":black_large_square: :zero: :one: :two: :three: :four: :five: :six: :seven: :eight: :nine:")
                    await self.client.send_message(message.channel, "**Colors:**\n<{}> = Red\n<{}> = Orange\n<{}> = Yellow\n<{}> = Green\n<{}> = Blue\n<{}> = Indigo\n<{}> = Violet\n<{}> = White".format(red, orange, yellow, green, blue, indigo, violet, white))
                    return

            if message.content.upper() == ".DRAW SAVED":
                if message.author.server_permissions.administrator:

                    await self.client.delete_message(message)

                    with open('canvas.json') as fp:
                        content = json.load(fp)

                    a = await self.client.send_message(message.channel, "{}".format(" ".join(content['a'])))
                    b = await self.client.send_message(message.channel, "{}".format(" ".join(content['b'])))
                    c = await self.client.send_message(message.channel, "{}".format(" ".join(content['c'])))
                    d = await self.client.send_message(message.channel, "{}".format(" ".join(content['d'])))
                    e = await self.client.send_message(message.channel, "{}".format(" ".join(content['e'])))
                    f = await self.client.send_message(message.channel, "{}".format(" ".join(content['f'])))
                    g = await self.client.send_message(message.channel, "{}".format(" ".join(content['g'])))
                    h = await self.client.send_message(message.channel, "{}".format(" ".join(content['h'])))
                    i = await self.client.send_message(message.channel, "{}".format(" ".join(content['i'])))
                    j = await self.client.send_message(message.channel, "{}".format(" ".join(content['j'])))
                    await self.client.send_message(message.channel,
                                                   ":black_large_square: :zero: :one: :two: :three: :four: :five: :six: :seven: :eight: :nine:")
                    await self.client.send_message(message.channel,
                                                   "**Colors:**\n<{}> = Red\n<{}> = Orange\n<{}> = Yellow\n<{}> = Green\n<{}> = Blue\n<{}> = Indigo\n<{}> = Violet\n<{}> = White".format(
                                                       red, orange, yellow, green, blue, indigo, violet, white))
                    return

            if message.content.upper().startswith(".DRAW "):
                args = str(message.content).split(" ")

                pos = args[1]
                color = args[2]

                posy = pos[0]  # A
                posx = int(pos[1]) + 1  # 4

                print("COLOR:" + color)
                print("POSX: {}".format(posx))
                print("POSY: {}".format(posy))

                if color.lower() == "red":
                    emoji_color = red
                if color.lower() == "white":
                    emoji_color = white
                if color.lower() == "orange":
                    emoji_color = orange
                if color.lower() == "yellow":
                    emoji_color = yellow
                if color.lower() == "green":
                    emoji_color = green
                if color.lower() == "blue":
                    emoji_color = blue
                if color.lower() == "indigo":
                    emoji_color = indigo
                if color.lower() == "violet":
                    emoji_color = violet
                if emoji_color == "":
                    user = await self.client.get_user_info(user_id)
                    await self.client.send_message(user, "Your message was incorrectly formatted! It should look like `.draw a3 red` or .`draw g0 blue`")
                    return

                with open('canvas.json') as fp:
                    content = json.load(fp)

                try:
                    if posy.lower() == "a":
                        line_content = content['a']
                        line = a
                    if posy.lower() == "b":
                        line_content = content['b']
                        line = b
                    if posy.lower() == "c":
                        line_content = content['c']
                        line = c
                    if posy.lower() == "d":
                        line_content = content['d']
                        line = d
                    if posy.lower() == "e":
                        line_content = content['e']
                        line = e
                    if posy.lower() == "f":
                        line_content = content['f']
                        line = f
                    if posy.lower() == "g":
                        line_content = content['g']
                        line = g
                    if posy.lower() == "h":
                        line_content = content['h']
                        line = h
                    if posy.lower() == "i":
                        line_content = content['i']
                        line = i
                    if posy.lower() == "j":
                        line_content = content['j']
                        line = j
                except NameError as e:
                    messages = []
                    with open('canvas.json') as fp:
                        content = json.load(fp)
                    async for message in self.client.logs_from(message.channel, limit=30):
                        messages.append(message)
                    await self.client.delete_messages(messages)

                    await self.client.send_message(message.channel, "ERROR: `{}`\nReloading Canvas...".format(e))

                    embed = discord.Embed(title="Canvas Help:", color=settings.embed_color)
                    embed.add_field(name=".draw [LETTER][NUMBER] [COLOR]",
                                    value="Paints tile in row [letter] and line [number] to color [color]",
                                    inline=False)
                    embed.add_field(name="Example:", value=".draw a3 red", inline=False)
                    embed.set_footer(text="You can also try `.help verified`, `.help admin`, & `.help basic`")
                    await self.client.send_message(message.channel, embed=embed)

                    a = await self.client.send_message(message.channel, "{}".format(" ".join(content['a'])))
                    b = await self.client.send_message(message.channel, "{}".format(" ".join(content['b'])))
                    c = await self.client.send_message(message.channel, "{}".format(" ".join(content['c'])))
                    d = await self.client.send_message(message.channel, "{}".format(" ".join(content['d'])))
                    e = await self.client.send_message(message.channel, "{}".format(" ".join(content['e'])))
                    f = await self.client.send_message(message.channel, "{}".format(" ".join(content['f'])))
                    g = await self.client.send_message(message.channel, "{}".format(" ".join(content['g'])))
                    h = await self.client.send_message(message.channel, "{}".format(" ".join(content['h'])))
                    i = await self.client.send_message(message.channel, "{}".format(" ".join(content['i'])))
                    j = await self.client.send_message(message.channel, "{}".format(" ".join(content['j'])))
                    await self.client.send_message(message.channel,
                                                   ":black_large_square: :zero: :one: :two: :three: :four: :five: :six: :seven: :eight: :nine:")
                    await self.client.send_message(message.channel,
                                                   "**Colors:**\n<{}> = Red\n<{}> = Orange\n<{}> = Yellow\n<{}> = Green\n<{}> = Blue\n<{}> = Indigo\n<{}> = Violet\n<{}> = White".format(
                                                       red, orange, yellow, green, blue, indigo, violet, white))
                    return

                if not line_content:
                    user = await self.client.get_user_info(user_id)
                    await self.client.send_message(user, "Your message was incorrectly formatted! It should look like `.draw a3 red` or .`draw g0 blue`")
                    return

                old_content = line_content
                print("Old content: {}".format(old_content))

                place = int(posx)
                print("Place: {}".format(place))

                emote = str(emoji_color)
                print("Emote: " + emote)

                new_content = list(old_content)
                del new_content[int(posx)]
                print("A {}".format(new_content))
                new_content.insert(int(posx), "<{}>".format(str(emoji_color)))
                print("B {}".format(new_content))

                with open('canvas.json', 'r') as fp:
                    content = json.load(fp)
                content[posy.lower()] = new_content
                with open('canvas.json', 'w') as fp:
                    json.dump(content, fp, sort_keys=True, indent=4)

                await self.client.edit_message(line, "{}".format(" ".join(new_content)))

                await self.client.delete_message(message)

                return
            else:
                if message.author.id == self.client.user.id:
                    pass
                else:
                    await self.client.delete_message(message)
                    user = await self.client.get_user_info(message.author.id)
                    await self.client.send_message(user, "Your message was incorrectly formatted! It should look like `.draw a3 red` or .`draw g0 blue`")


def setup(client):
    client.add_cog(Canvas(client))
