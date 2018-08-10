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


class Admin:
    def __init__(self, client):
        self.client = client

    print("Loading Admin...")

    async def on_message(self, message):
        if message.author == self.client.user:
            return

        # Message author variables
        user_id = message.author.id
        user_name = message.author
        server = message.server

        # Banned Words
        banned_words = settings.get_json("banned_words.json")

        if any(word in message.content.upper() for word in banned_words):
            karma.user_add_karma(user_id, -50)
            await self.client.delete_message(message)
            dm_id = await self.client.get_user_info(user_id)
            await self.client.send_message(dm_id, "Sorry, but you used a word / phrase that is banned!\nYou can see wha"
                                                  "t is banned via the `.banwordlist` command.")
            return
        try:
            if message.author.server_permissions.administrator:
                if message.content.upper().startswith(".SERVERRULES"):
                    await self.client.delete_message(message)
                    embed = discord.Embed(title="Synaps Rules and Info",
                                          url="https://steamcommunity.com/groups/team_synaps",
                                          color=settings.embed_color)
                    embed.set_thumbnail(url="https://goo.gl/ibJU2z")
                    embed.add_field(name="📜 Rules 1.)", value="No spamming.", inline=True)
                    embed.add_field(name="👙 Rules 2.)", value="No NSFW in Discussion.", inline=True)
                    embed.add_field(name="🎵 Rules 3.)", value="No music requests in any channel but the music channel",
                                    inline=True)
                    embed.add_field(name="🔰 Getting Verified:",
                                    value="Add `[Synaps]` to your steam name and DM a Admin.", inline=True)
                    embed.add_field(
                        name="🔸 Getting Member *(How to get access to other channels)*:",
                        value="Read the rules above and type `.accept` in this channel. If for whatever reason it "
                              "doesn't work, contact an {}.".format(settings.admin_role_name), inline=True)
                    await self.client.send_message(message.channel, embed=embed)

                if message.content.upper().startswith(".GIVEKARMA"):
                    if not message.raw_mentions:
                        await self.client.send_message(
                            message.channel,
                            "You need to `@` a user and give an amount. Example: `.givekarma @Mehvix#7172 10`")
                    else:
                        try:
                            target = message.content.split(" ")
                            target_user = target[1]
                            target_amount = target[2]
                            target_user = target_user[2:-1]
                            karma.user_add_karma(target_user, int(target_amount))
                            await self.client.send_message(message.channel,
                                                           "You gave <@{}> `{}` karma. They now have a total of `{}` "
                                                           "karma".format(target_user, target_amount, karma.get_karma(
                                                               target_user)))
                        except IndexError:
                            await self.client.send_message(
                                message.channel, "You either didn't correctly `@` a user or enter in a amount.")

                if message.content.upper().startswith(".MUTE"):
                    role = discord.utils.get(message.server.roles, name=settings.mute_role_name)
                    if not message.raw_mentions:
                        await self.client.send_message(message.channel, "You need to `@` a user")
                    else:
                        mute_target = message.content[8:-1]
                        person = await self.client.get_user_info(mute_target)
                        print("{0}: {1} muted {2}".format(curtime.get_time(), user_name, person.name))
                        await self.client.add_roles(message.mentions[0], role)
                        await self.client.send_message(
                            message.channel, "<@{0}> muted <@{1}>".format(message.author.id, mute_target))

                if message.content.upper().startswith(".UNMUTE"):
                    role = discord.utils.get(message.server.roles, name=settings.mute_role_name)
                    if not message.raw_mentions:
                        await self.client.send_message(message.channel, "You need to `@` a user")
                    else:
                        unmute_target = message.content[10:-1]
                        person = await self.client.get_user_info(unmute_target)
                        print("{0}: {1} unmuted {2}".format(curtime.get_time(), user_name, person.name))
                        await self.client.remove_roles(message.mentions[0], role)
                        await self.client.send_message(
                            message.channel, "<@{0}> unmuted <@{1}>".format(message.author.id, unmute_target))

                if message.content.upper().startswith(".BAN"):
                    if message.content.upper().startswith(".BANWORD "):
                        word = message.content[9:]
                        word = word.upper()
                        fp = "banned_words.json"
                        banned_words = settings.get_json(fp)
                        banned_words.insert(0, word)
                        with open(fp, 'w') as outfile:
                            json.dump(banned_words, outfile)
                        await self.client.send_message(
                            message.channel, "The word / sentence `{}` was banned. The full list of banned words can be"
                                             " found via `.bannedwords`".format(word))
                    if message.content.upper().startswith(".BANLIST"):
                        pass
                    if message.content.upper().startswith(".BANNEDWORDS"):
                        pass
                    else:
                        if not message.raw_mentions:
                            await self.client.send_message(message.channel, "You need to `@` a user")
                        else:
                            ban_target = message.content[7:-1]
                            print("{0}: {1} banned {2}".format(curtime.get_time(), user_name, ban_target))
                            await self.client.ban(member=server.get_member(ban_target), delete_message_days=0)

                if message.content.upper().startswith(".KICK"):
                    kick_target = message.content[8:-1]
                    print("{0}: {1} kicked {2}".format(curtime.get_time(), user_name, kick_target))
                    if not message.raw_mentions:
                        await self.client.send_message(message.channel, "You need to `@` a user")
                    else:
                        print("{0}: {1} kicked {2}".format(curtime.get_time(), user_name, kick_target))
                        await self.client.kick(member=server.get_member(kick_target))

                if message.content.upper().startswith(".UNBAN"):
                    if not message.raw_mentions:
                        await self.client.send_message(message.channel, "You need to `@` a user")
                    else:
                        unban_target = message.content[9:-1]
                        print("{0}: {1} unbanned {2}".format(curtime.get_time(), user_name, unban_target))
                        banned = await self.client.get_user_info(unban_target)
                        await self.client.unban(message.server, banned)
                        await self.client.send_message(message.channel,
                                                       "<@{}> was unbanned :tada:".format(unban_target))

                if message.content.upper().startswith(".CLEAR "):
                    channel = message.channel
                    amount = message.content[7:]

                    messages = []
                    try:
                        async for message in self.client.logs_from(channel, limit=int(amount) + 1):
                            messages.append(message)
                        await self.client.delete_messages(messages)
                        await self.client.send_message(channel, "<@{}> deleted `{}` messages".format(user_id, amount))
                    except discord.HTTPException:
                        await self.client.send_message(
                            channel, "You can only bulk delete messages that are less than 14 days old.")
                    except ValueError:
                        await self.client.send_message(channel,
                                                       "You need to give a number between `2` and `99`")
                    except discord.ClientException:
                        await self.client.send_message(channel,
                                                       "You need to give a number between `2` and `99`")
        except AttributeError:
            print("{}: Couldn't find user roles. It's probably a webhook or a message via DM's".
                  format(curtime.get_time()))


def setup(client):
    client.add_cog(Admin(client))
