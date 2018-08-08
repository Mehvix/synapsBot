#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
import string
import asyncio
import discord
import curtime
import settings
from discord.ext import commands

clock_emoji = ["🕐", "🕑", "🕒", "🕓", "🕔", "🕕", "🕖", "🕗", "🕘", "🕙", "🕚", "🕛"]
vote_phase = 0


class Createpoll:
    def __init__(self, client):
        self.client = client

    print("Loading Createpoll...")

    async def on_message(self, message):
        # Message author variables
        user_id = message.author.id
        user_name = message.author

        # Poll System
        if message.content.upper().startswith(".CREATEPOLL"):
            global vote_phase
            if vote_phase != 1:
                vote_phase += 1
                print("{0}: {1} created a poll".format(curtime.get_time(), user_name))
                await asyncio.sleep(.1)
                await self.client.delete_message(message)

                title_embed = discord.Embed(title="\u200b", color=settings.embed_color)
                title_embed.set_author(
                    name="Generating a poll for {0} {1}".format(user_name, random.choice(clock_emoji)))
                title_embed.add_field(name="\u200b", value="\u200b", inline=False)
                title_embed.add_field(name="Question", value="What would you like the title to be?",
                                      inline=False)
                title_message = await self.client.send_message(message.channel, embed=title_embed)

                # Title
                title = await self.client.wait_for_message(
                    timeout=120, author=message.author, channel=message.channel)

                try:
                    poll_title = title.content
                    print("{0}: Set title to {1}".format(curtime.get_time(), poll_title))
                    await asyncio.sleep(.1)
                    await self.client.delete_message(title)
                except AttributeError:
                    await self.client.send_message(
                        message.channel, "<@{}> didn't respond fast enough, so the poll was cancelled".format(
                            message.author.id))
                    return

                options_embed = discord.Embed(title="\u200b", color=settings.embed_color)
                options_embed.set_author(name="Generating a poll for {0} {1}"
                                         .format(user_name, random.choice(clock_emoji)))
                options_embed.add_field(name="Title:", value=str(poll_title), inline=False)
                options_embed.add_field(name="\u200b", value="\u200b", inline=False)
                options_embed.add_field(
                    name="Question", value="How many options do you want their to be? (No more than 10)",
                    inline=False)
                await asyncio.sleep(.1)
                await self.client.delete_message(title_message)
                options_message = await self.client.send_message(message.channel, embed=options_embed)

                # Number of Options
                options = await self.client.wait_for_message(
                    timeout=120, author=message.author, channel=message.channel)

                try:
                    poll_options = int(options.content)
                    print("{0}: Number of options set to {1}".format(curtime.get_time(), poll_options))
                    await asyncio.sleep(.1)
                    await self.client.delete_message(options)
                except ValueError:
                    await self.client.send_message(
                        message.channel, "You can only use **whole** numbers, no decimals!")
                    return
                except AttributeError:
                    await self.client.send_message(
                        message.channel, "<@{}> didn't respond fast enough, so the poll was cancelled".format(
                            message.author.id))
                    return

                # Option debugging
                if poll_options <= 1:
                    await self.client.send_message(message.channel, "Sorry, You can't have 1 option")
                    return
                if poll_options > 10:
                    await self.client.send_message(message.channel, "Sorry, You can't have more than 10 options!")
                    return

                one_embed = discord.Embed(title="\u200b", color=settings.embed_color)
                one_embed.set_author(name="Generating a poll for {0} {1}"
                                     .format(user_name, random.choice(clock_emoji)))
                one_embed.add_field(name="Title:", value=str(poll_title), inline=False)
                one_embed.add_field(name="Number of Options:", value=str(poll_options), inline=False)
                one_embed.add_field(name="\u200b", value="\u200b", inline=False)
                one_embed.add_field(
                    name="Question", value="What should Option 🇦 be?",
                    inline=False)
                await asyncio.sleep(.1)
                await self.client.delete_message(options_message)
                one_message = await self.client.send_message(message.channel, embed=one_embed)

                # Gets Option 1
                option_1 = await self.client.wait_for_message(timeout=120, author=message.author,
                                                              channel=message.channel)
                try:
                    poll_option_1 = option_1.content
                    print("{0}: Option 1 set to {1}".format(curtime.get_time(), poll_option_1))
                    await asyncio.sleep(.1)
                    await self.client.delete_message(option_1)
                    # await self.client.delete_message(bot_opt1)

                except AttributeError:
                    await self.client.send_message(
                        message.channel,
                        "<@{}> DIDN'T respond fast enough, so the poll was cancelled".format(
                            message.author.id))
                    return

                two_embed = discord.Embed(title="\u200b", color=settings.embed_color)
                two_embed.set_author(name="Generating a poll for {0} {1}".format(user_name,
                                                                                 random.choice(
                                                                                     clock_emoji)))
                two_embed.add_field(name="Title:", value=str(poll_title), inline=False)
                two_embed.add_field(name="Number of Options:", value=str(poll_options), inline=False)
                two_embed.add_field(name="🇦:", value=str(poll_option_1), inline=True)
                two_embed.add_field(name="\u200b", value="\u200b", inline=False)
                two_embed.add_field(
                    name="Question", value="What should Option 🇧 be?",
                    inline=False)
                await asyncio.sleep(.1)
                await self.client.delete_message(one_message)
                two_message = await self.client.send_message(message.channel, embed=two_embed)

                # Gets Option 2
                option_2 = await self.client.wait_for_message(
                    timeout=120, author=message.author, channel=message.channel)

                try:
                    poll_option_2 = option_2.content
                    print("{0}: Option 2 set to {1}".format(curtime.get_time(), poll_option_2))
                    await asyncio.sleep(.1)
                    await self.client.delete_message(option_2)

                except AttributeError:
                    await self.client.send_message(
                        message.channel,
                        "<@{}> DIDN'T respond fast enough, so the poll was cancelled".format(
                            message.author.id))
                    return

                if poll_options >= 3:

                    three_embed = discord.Embed(title="\u200b", color=settings.embed_color)
                    three_embed.set_author(
                        name="Generating a poll for {0} {1}".format(user_name, random.choice(clock_emoji)))
                    three_embed.add_field(name="Title:", value=str(poll_title), inline=False)
                    three_embed.add_field(name="Number of Options:", value=str(poll_options), inline=False)
                    three_embed.add_field(name=" A:", value=str(poll_option_1), inline=True)
                    three_embed.add_field(name=" 🇧:", value=str(poll_option_2), inline=True)
                    three_embed.add_field(name="\u200b", value="\u200b", inline=False)
                    three_embed.add_field(
                        name="Question", value="What should Option 🇨 be called?",
                        inline=False)
                    await asyncio.sleep(.1)
                    await self.client.delete_message(two_message)
                    three_message = await self.client.send_message(message.channel, embed=three_embed)

                    # Option 3
                    option_3 = await self.client.wait_for_message(
                        timeout=120, author=message.author, channel=message.channel)

                    try:
                        poll_option_3 = option_3.content
                        print("{0}: Option 3 set to {1}".format(curtime.get_time(), poll_option_3))
                        await asyncio.sleep(.1)
                        await self.client.delete_message(option_3)

                    except AttributeError:
                        await self.client.send_message(
                            message.channel,
                            "<@{}> DIDN'T respond fast enough, so the poll was cancelled".format(
                                message.author.id))
                        return

                    if poll_options >= 4:
                        four_embed = discord.Embed(title="\u200b", color=settings.embed_color)
                        four_embed.set_author(
                            name="Generating a poll for {0} {1}".format(user_name, random.choice(clock_emoji)))
                        four_embed.add_field(name="Title:", value=str(poll_title), inline=False)
                        four_embed.add_field(name="Number of Options:", value=str(poll_options), inline=False)
                        four_embed.add_field(name=" 🇦:", value=str(poll_option_1), inline=True)
                        four_embed.add_field(name=" 🇧:", value=str(poll_option_2), inline=True)
                        four_embed.add_field(name=" 🇨:", value=str(poll_option_3), inline=True)
                        four_embed.add_field(name="\u200b", value="\u200b", inline=False)
                        four_embed.add_field(
                            name="Question", value="What should Option 🇩 be called?",
                            inline=False)
                        await asyncio.sleep(.1)
                        await self.client.delete_message(three_message)
                        four_message = await self.client.send_message(message.channel, embed=four_embed)

                        # Option 4
                        option_4 = await self.client.wait_for_message(timeout=120, author=message.author,
                                                                      channel=message.channel)

                        try:
                            poll_option_4 = option_4.content
                            print("{0}: Option 4 set to {1}".format(curtime.get_time(), poll_option_4))
                            await asyncio.sleep(.1)
                            await self.client.delete_message(option_4)

                        except AttributeError:
                            await self.client.send_message(
                                message.channel,
                                "<@{}> DIDN'T respond fast enough, so the poll was cancelled".format(
                                    message.author.id))
                            return

                        if poll_options >= 5:
                            five_embed = discord.Embed(title="\u200b", color=settings.embed_color)
                            five_embed.set_author(
                                name="Generating a poll for {0} {1}".format(user_name,
                                                                            random.choice(clock_emoji)))
                            five_embed.add_field(name="Title:", value=str(poll_title), inline=False)
                            five_embed.add_field(name="Number of Options:", value=str(poll_options),
                                                 inline=False)
                            five_embed.add_field(name=" 🇦:", value=str(poll_option_1), inline=True)
                            five_embed.add_field(name=" 🇧:", value=str(poll_option_2), inline=True)
                            five_embed.add_field(name=" 🇨:", value=str(poll_option_3), inline=True)
                            five_embed.add_field(name=" 🇩:", value=str(poll_option_4), inline=True)
                            five_embed.add_field(name="\u200b", value="\u200b", inline=False)
                            five_embed.add_field(
                                name="Question", value="What should Option 🇪 be called?",
                                inline=False)
                            await asyncio.sleep(.1)
                            await self.client.delete_message(four_message)
                            five_message = await self.client.send_message(message.channel, embed=five_embed)

                            # Option 5
                            option_5 = await self.client.wait_for_message(
                                timeout=120, author=message.author, channel=message.channel)

                            try:
                                poll_option_5 = option_5.content
                                print("{0}: Option 5 set to {1}".format(curtime.get_time(), poll_option_5))
                                await asyncio.sleep(.1)
                                await self.client.delete_message(option_5)

                            except AttributeError:
                                await self.client.send_message(
                                    message.channel,
                                    "<@{}> DIDN'T respond fast enough, so the poll was cancelled".format(
                                        message.author.id))
                                return

                            if poll_options >= 6:
                                six_embed = discord.Embed(title="\u200b", color=settings.embed_color)
                                six_embed.set_author(
                                    name="Generating a poll for {0} {1}".format(user_name,
                                                                                random.choice(clock_emoji)))
                                six_embed.add_field(name="Title:", value=str(poll_title), inline=False)
                                six_embed.add_field(name="Number of Options:", value=str(poll_options),
                                                    inline=False)
                                six_embed.add_field(name=" 🇦:", value=str(poll_option_1), inline=True)
                                six_embed.add_field(name=" 🇧:", value=str(poll_option_2), inline=True)
                                six_embed.add_field(name=" 🇨:", value=str(poll_option_3), inline=True)
                                six_embed.add_field(name=" 🇩:", value=str(poll_option_4), inline=True)
                                six_embed.add_field(name=" 🇪:", value=str(poll_option_5), inline=True)
                                six_embed.add_field(name="\u200b", value="\u200b", inline=True)
                                six_embed.add_field(
                                    name="Question", value="What should Option 🇫 be called?",
                                    inline=False)
                                await asyncio.sleep(.1)
                                await self.client.delete_message(five_message)
                                six_message = await self.client.send_message(message.channel, embed=six_embed)

                                # Option 6
                                option_6 = await self.client.wait_for_message(
                                    timeout=120, author=message.author, channel=message.channel)

                                try:
                                    poll_option_6 = option_6.content
                                    print("{0}: Option 🇫 set to {1}".format(curtime.get_time(), poll_option_6))
                                    await asyncio.sleep(.1)
                                    await self.client.delete_message(option_6)

                                except AttributeError:
                                    await self.client.send_message(
                                        message.channel,
                                        "<@{}> DIDN'T respond fast enough, so the poll was cancelled".format
                                        (message.author.id))
                                    return

                                if poll_options >= 7:
                                    seven_embed = discord.Embed(title="\u200b", color=settings.embed_color)
                                    seven_embed.set_author(
                                        name="Generating a poll for {0} {1}".format(user_name,
                                                                                    random.choice(clock_emoji)))
                                    seven_embed.add_field(name="Title:", value=str(poll_title), inline=False)
                                    seven_embed.add_field(name="Number of Options:", value=str(poll_options),
                                                          inline=False)
                                    seven_embed.add_field(name=" 🇦:", value=str(poll_option_1), inline=True)
                                    seven_embed.add_field(name=" 🇧:", value=str(poll_option_2), inline=True)
                                    seven_embed.add_field(name=" 🇨:", value=str(poll_option_3), inline=True)
                                    seven_embed.add_field(name=" 🇩:", value=str(poll_option_4), inline=True)
                                    seven_embed.add_field(name=" 🇪:", value=str(poll_option_5), inline=True)
                                    seven_embed.add_field(name=" 🇫:", value=str(poll_option_6), inline=True)
                                    seven_embed.add_field(name="\u200b", value="\u200b", inline=True)
                                    seven_embed.add_field(name="Question", value="What should Option 🇬 be called?",
                                                          inline=False)
                                    await asyncio.sleep(.1)
                                    await self.client.delete_message(six_message)
                                    seven_message = await self.client.send_message(message.channel, embed=seven_embed)

                                    # Option 7
                                    option_7 = await self.client.wait_for_message(
                                        timeout=120, author=message.author, channel=message.channel)

                                    try:
                                        poll_option_7 = option_7.content
                                        print("{0}: Option 🇬 set to {1}".format(curtime.get_time(), poll_option_7))
                                        await asyncio.sleep(.1)
                                        await self.client.delete_message(option_7)

                                    except AttributeError:
                                        await self.client.send_message(
                                            message.channel,
                                            "<@{}> DIDN'T respond fast enough, so the poll was cancelled".format
                                            (message.author.id))
                                        return

                                    if poll_options >= 8:
                                        eight_embed = discord.Embed(title="\u200b", color=settings.embed_color)
                                        eight_embed.set_author(
                                            name="Generating a poll for {0} {1}".format(user_name,
                                                                                        random.choice(clock_emoji)))
                                        eight_embed.add_field(name="Title:", value=str(poll_title), inline=False)
                                        eight_embed.add_field(name="Number of Options:", value=str(poll_options),
                                                              inline=False)
                                        eight_embed.add_field(name=" 🇦:", value=str(poll_option_1), inline=True)
                                        eight_embed.add_field(name=" 🇧:", value=str(poll_option_2), inline=True)
                                        eight_embed.add_field(name=" 🇨:", value=str(poll_option_3), inline=True)
                                        eight_embed.add_field(name=" 🇩:", value=str(poll_option_4), inline=True)
                                        eight_embed.add_field(name=" 🇪:", value=str(poll_option_5), inline=True)
                                        eight_embed.add_field(name=" 🇫:", value=str(poll_option_6), inline=True)
                                        eight_embed.add_field(name=" 🇬:", value=str(poll_option_7), inline=True)
                                        eight_embed.add_field(name="\u200b", value="\u200b", inline=True)
                                        eight_embed.add_field(
                                            name="Question", value="What should Option 🇭 be called?",
                                            inline=False)
                                        await asyncio.sleep(.1)
                                        await self.client.delete_message(seven_message)
                                        eight_message = await self.client.send_message(message.channel,
                                                                                       embed=eight_embed)

                                        # Option 8
                                        option_8 = await self.client.wait_for_message(
                                            timeout=120, author=message.author, channel=message.channel)

                                        try:
                                            poll_option_8 = option_8.content
                                            print("{0}: Option 🇬 set to {1}".format(curtime.get_time(), poll_option_8))
                                            await asyncio.sleep(.1)
                                            await self.client.delete_message(option_8)

                                        except AttributeError:
                                            await self.client.send_message(
                                                message.channel,
                                                "<@{}> DIDN'T respond fast enough, so the poll was cancelled".format
                                                (message.author.id))
                                            return

                                        if poll_options >= 9:
                                            nine_embed = discord.Embed(title="\u200b", color=settings.embed_color)
                                            nine_embed.set_author(
                                                name="Generating a poll for {0} {1}".format(user_name,
                                                                                            random.choice(
                                                                                                clock_emoji)))
                                            nine_embed.add_field(name="Title:", value=str(poll_title), inline=False)
                                            nine_embed.add_field(name="Number of Options:", value=str(poll_options),
                                                                 inline=False)
                                            nine_embed.add_field(name=" 🇦:", value=str(poll_option_1), inline=True)
                                            nine_embed.add_field(name=" 🇧:", value=str(poll_option_2), inline=True)
                                            nine_embed.add_field(name=" 🇨:", value=str(poll_option_3), inline=True)
                                            nine_embed.add_field(name=" 🇩:", value=str(poll_option_4), inline=True)
                                            nine_embed.add_field(name=" 🇪:", value=str(poll_option_5), inline=True)
                                            nine_embed.add_field(name=" 🇫:", value=str(poll_option_6), inline=True)
                                            nine_embed.add_field(name=" 🇬:", value=str(poll_option_7), inline=True)
                                            nine_embed.add_field(name=" 🇭:", value=str(poll_option_8), inline=True)
                                            nine_embed.add_field(name="\u200b", value="\u200b", inline=True)
                                            nine_embed.add_field(name="Question",
                                                                 value="What should Option 🇮 be called?", inline=False)
                                            await asyncio.sleep(.1)
                                            await self.client.delete_message(eight_message)
                                            nine_message = await self.client.send_message(message.channel,
                                                                                          embed=nine_embed)

                                            # Option 9
                                            option_9 = await self.client.wait_for_message(
                                                timeout=120, author=message.author, channel=message.channel)

                                            try:
                                                poll_option_9 = option_9.content
                                                print("{0}: Option 🇮 set to {1}".format(curtime.get_time(),
                                                                                         poll_option_9))
                                                await asyncio.sleep(.1)
                                                await self.client.delete_message(option_9)

                                            except AttributeError:
                                                await self.client.send_message(
                                                    message.channel,
                                                    "<@{}> DIDN'T respond fast enough, so the poll was cancelled".format
                                                    (message.author.id))
                                                return

                                            if poll_options >= 10:
                                                ten_embed = discord.Embed(title="\u200b", color=settings.embed_color)
                                                ten_embed.set_author(
                                                    name="Generating a poll for {0} {1}".format(user_name,
                                                                                                random.choice(
                                                                                                    clock_emoji)))
                                                ten_embed.add_field(name="Title:", value=str(poll_title), inline=False)
                                                ten_embed.add_field(name="Number of Options:", value=str(poll_options),
                                                                    inline=False)
                                                ten_embed.add_field(name=" 🇦:", value=str(poll_option_1), inline=True)
                                                ten_embed.add_field(name=" 🇧:", value=str(poll_option_2), inline=True)
                                                ten_embed.add_field(name=" 🇨:", value=str(poll_option_3), inline=True)
                                                ten_embed.add_field(name=" 🇩:", value=str(poll_option_4), inline=True)
                                                ten_embed.add_field(name=" 🇪:", value=str(poll_option_5), inline=True)
                                                ten_embed.add_field(name=" 🇫:", value=str(poll_option_6), inline=True)
                                                ten_embed.add_field(name=" 🇬:", value=str(poll_option_7), inline=True)
                                                ten_embed.add_field(name=" 🇭:", value=str(poll_option_8), inline=True)
                                                ten_embed.add_field(name=" 🇮:", value=str(poll_option_9), inline=True)
                                                ten_embed.add_field(name="\u200b", value="\u200b", inline=True)
                                                ten_embed.add_field(name="Question",
                                                                    value="What should Option 🇯 be called?",
                                                                    inline=False)
                                                await asyncio.sleep(.1)
                                                await self.client.delete_message(nine_message)
                                                ten_message = await self.client.send_message(message.channel,
                                                                                             embed=ten_embed)

                                                # Option 10
                                                option_10 = await self.client.wait_for_message(
                                                    timeout=120, author=message.author, channel=message.channel)

                                                try:
                                                    poll_option_10 = option_10.content
                                                    print(
                                                        "{0}: Option 🇯 set to {1}".format(curtime.get_time(),
                                                                                           poll_option_10))
                                                    await asyncio.sleep(.1)
                                                    await self.client.delete_message(option_10)

                                                except AttributeError:
                                                    await self.client.send_message(message.channel,
                                                                                   "<@{}> DIDN'T respond fast enough, so the"
                                                                                   " poll was cancelled".format(
                                                                                       message.author.id))
                                                    return

                                                await asyncio.sleep(.1)
                                                await self.client.delete_message(ten_message)

                        else:
                            await asyncio.sleep(.1)
                            await self.client.delete_message(four_message)
                    else:
                        await asyncio.sleep(.1)
                        await self.client.delete_message(three_message)
                else:
                    await asyncio.sleep(.1)
                    await self.client.delete_message(two_message)

                embed = discord.Embed(
                    title=string.capwords(poll_title),
                    description="Created by `{}`".format(user_name), color=settings.embed_color)
                embed.set_thumbnail(
                    url="https://png.icons8.com/metro/1600/poll-topic.png")
                embed.add_field(
                    name=" 🇦:", value=string.capwords(poll_option_1), inline=True)
                embed.add_field(
                    name=" 🇧:", value=string.capwords(poll_option_2), inline=True)
                if poll_options >= 3:
                    embed.add_field(
                        name=" 🇨:", value=string.capwords(poll_option_3), inline=True)
                    if poll_options >= 4:
                        embed.add_field(
                            name=" 🇩:", value=string.capwords(poll_option_4), inline=True)
                        if poll_options >= 5:
                            embed.add_field(
                                name=" 🇪:", value=string.capwords(poll_option_5), inline=True)
                            if poll_options >= 6:
                                embed.add_field(
                                    name=" 🇫:", value=string.capwords(poll_option_6),
                                    inline=True)
                                if poll_options >= 7:
                                    embed.add_field(
                                        name=" 🇬:", value=string.capwords(poll_option_7),
                                        inline=True)
                                    if poll_options >= 8:
                                        embed.add_field(
                                            name=" 🇭:", value=string.capwords(poll_option_8),
                                            inline=True)
                                        if poll_options >= 9:
                                            embed.add_field(
                                                name=" 🇮:", value=string.capwords(poll_option_9),
                                                inline=True)
                                            if poll_options >= 10:
                                                embed.add_field(
                                                    name=" 🇯:", value=string.capwords(poll_option_10),
                                                    inline=True)
                poll_message = await self.client.send_message(message.channel, embed=embed)

                await self.client.add_reaction(poll_message, "🇦")
                await asyncio.sleep(.1)
                await self.client.add_reaction(poll_message, "🇧")
                if poll_options >= 3:
                    await asyncio.sleep(.1)
                    await self.client.add_reaction(poll_message, "🇨")
                    if poll_options >= 4:
                        await asyncio.sleep(.1)
                        await self.client.add_reaction(poll_message, "🇩")
                        if poll_options >= 5:
                            await asyncio.sleep(.1)
                            await self.client.add_reaction(poll_message, "🇪")
                            if poll_options >= 6:
                                await asyncio.sleep(.1)
                                await self.client.add_reaction(poll_message, "🇫")
                                if poll_options >= 7:
                                    await asyncio.sleep(.1)
                                    await self.client.add_reaction(poll_message, "🇬")
                                    if poll_options >= 8:
                                        await asyncio.sleep(.1)
                                        await self.client.add_reaction(poll_message, "🇭")
                                        if poll_options >= 9:
                                            await asyncio.sleep(.1)
                                            await self.client.add_reaction(poll_message, "🇮")
                                            if poll_options >= 10:
                                                await asyncio.sleep(.1)
                                                await self.client.add_reaction(poll_message, "🇯")
                vote_phase -= 1
            else:
                await self.client.send_message(message.channel, "Sorry, another vote is taking place right now!")


def setup(client):
    client.add_cog(Createpoll(client))
