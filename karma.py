#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import re
import sys
import json
import discord
import curtime
import settings
from discord.ext import commands


class Karma:
    def __init__(self, client):
        self.client = client

    print("Loading Karma...")

    async def on_reaction_add(self, reaction, user):
        emoji_used = str(reaction.emoji)
        formated_up = "<{}>".format(settings.upvote_emoji)
        formated_down = "<{}>".format(settings.downvote_emoji)

        print("{0}: {1} reacted with {2} to {3}'s message"
              .format(curtime.get_time(), user, emoji_used, reaction.message.author))

        if reaction.message.channel.id != settings.pokemon_channel:
            if emoji_used == formated_up:  # If emote is the upvote emote
                if reaction.message.author.id == user.id:
                    print("{0}: {1} upvoted there own link. NO CHANGE".format(curtime.get_time(), user))
                else:
                    try:
                        user_add_karma(reaction.message.author.id, 5)
                        print("{0}: ADDED 5 karma to {1} for a UPVOTE from {2}"
                              .format(curtime.get_time(), reaction.message.author, user))
                    except AttributeError:
                        print("{0}: User doesn't exist! (Probably a webhook)".format(curtime.get_time()))

            # If emote is the downvote emote
            if emoji_used == formated_down:
                if reaction.message.author.id == user.id:
                    print("{0}: {1} downvoted there post. NO CHANGE"
                          .format(curtime.get_time(), user))
                else:
                    try:
                        user_add_karma(reaction.message.author.id, -5)
                        print("{0}: REMOVED 5 karma from {1} for a DOWNVOTE from {2}"
                              .format(curtime.get_time(), reaction.message.author, user))
                    except AttributeError:
                        print("{0}: User doesn't exist! (Probably a webhook)".format(curtime.get_time()))
        else:
            print("{0}: DIDN'T change {1}'s karma because they're in the Pokemon Channel!"
                  .format(curtime.get_time(), user))


    async def on_reaction_remove(self, reaction, user):
        emoji_used = str(reaction.emoji)
        formated_up = "<{}>".format(settings.upvote_emoji)
        formated_down = "<{}>".format(settings.downvote_emoji)

        if reaction.message.channel.id != settings.pokemon_channel:
            if emoji_used == formated_up:
                if reaction.message.author.id == user.id:
                    print("{0}: {1} REMOVED their upvote to their post. NO CHANGE".format(curtime.get_time(), user.id))
                else:
                    try:
                        user_add_karma(reaction.message.author.id, -5)
                        print("{0}: REMOVED 5 karma from {0} because {1} REMOVED there UPVOTE"
                              .format(curtime.get_time(), reaction.message.author, user))
                    except AttributeError:
                        print("{0}: User doesn't exist! (Probably a webhook)".format(curtime.get_time()))

            # If emote is the downvote emote
            if emoji_used == formated_down:
                if reaction.message.author.id == user.id:
                    print("{0}: {1} REMOVED their downvote to there own link. NO CHANGE".format(curtime.get_time(),
                                                                                                user))
                else:
                    try:
                        user_add_karma(reaction.message.author.id, 5)
                        print("{0}: RE-ADDED 5 karma to {1} for removal of downvote reaction from {2}"
                              .format(curtime.get_time(), reaction.message.author, user))
                    except AttributeError:
                        print("{0}: User doesn't exist! (Probably a webhook)".format(curtime.get_time()))
        else:
            print("{0}: DIDN'T change {1}'s karma because it was in the Pokemon Channel!"
                  .format(curtime.get_time(), user))

    async def on_message(self, message):
        # Message author variables
        user_id = message.author.id
        user_name = message.author

        try:
            author_level = get_level(user_id)
            author_karma = get_karma(user_id)
        except:
            author_level = None
            author_karma = None
            pass  # User just joined

        # Because @xpoes#9244 spams the shit out of our pokemon channel
        if message.channel.id == settings.pokemon_channel:
            print("{0}: DIDN'T give karma to {1} for message '{2}' because they sent a message in the Pokemon channel"
                  .format(curtime.get_time(), message.author, message.content))
        else:
            user_add_karma(user_id, 1)
            try:
                print("{0}: ADDED 1 karma to {1} for a message '{2}' in {3}"
                      .format(curtime.get_time(), user_name, message.content, message.channel))
            except:
                pass

        # Finds if message is a link or a file attachment (PDF, image, etc.)
        regex = re.compile(
            r'^(?:http|ftp)s?://'  # http:// or https://
            r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'  # domain...
            r'localhost|'  # localhost...
            r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # ...or ip
            r'(?::\d+)?'  # optional port
            r'(?:/?|[/?]\S+)$', re.IGNORECASE)
        if re.match(regex, message.content) is not None:
            await self.client.add_reaction(message, settings.upvote_emoji)

        # Adds upvote to images / uploads
        if message.attachments:
            await self.client.add_reaction(message, settings.upvote_emoji)

        if message.content.upper().startswith(".KARMA"):
            karma_target = message.content[7:]
            if karma_target == "":
                user_req = user_id
            else:
                if not message.raw_mentions:
                    await self.client.send_message(message.channel, "You need to `@` a user")
                    return
                else:
                    user_req = message.raw_mentions[0]
            print("{0}: {1} requested {2}'s level".format(curtime.get_time(), user_name, user_req))

            try:
                await self.client.send_message(
                    message.channel, "<@{0}> has `{1}` karma".format(user_req, get_karma(user_req)))
            except KeyError:
                await self.client.send_message(
                    message.channel, "<@{0}> has `0` karma".format(user_req))

        # Leveling
        if message.content.upper().startswith(".LEVEL"):
            level_target = message.content[7:]
            if level_target == "":
                user_level_req = user_id
            else:
                if not message.raw_mentions:
                    await self.client.send_message(message.channel, "You need to `@` a user")
                    return
                else:
                    user_level_req = message.raw_mentions[0]
            print("{0}: {1} requested {2}'s level".format(curtime.get_time(), user_name, user_level_req))
            await self.client.send_message(message.channel, "<@{0}> is level `{1}`".format(user_level_req,
                                                                                           get_level(user_level_req)))

        # Checks Karma / Level
        new_level = author_level + 1
        if author_karma >= 100 * new_level:
            role_name = "Level {}".format(new_level)
            level_role = discord.utils.get(message.server.roles, name=role_name)

            old_role = "Level {}".format(new_level - 1)
            old_level_role = discord.utils.get(message.server.roles, name=old_role)

            set_level(user_id, new_level)

            try:
                await self.client.remove_roles(message.author, old_level_role)
                await self.client.add_roles(message.author, level_role)
            except AttributeError:
                role = await self.client.create_role(message.server, name="Level" + new_level)
                await self.client.add_roles(message.author, role)

                user = await self.client.get_user_info(message.server.owner)
                await self.client.send_message(user, "The bot manually created a role for <@{}> when they leveled up".
                                               format(user_id))
            if message.channel.id != settings.canvas_channel or user_id != self.client.user.id:
                await self.client.send_message(message.channel, "Congrats, <@{0}>! You're now level `{1}`.  :tada: "
                                               .format(user_id, new_level))
            print("{0}: {1} leveled up to {2}".format(curtime.get_time(), user_name, get_level(user_id)))


def user_add_karma(user_id: int, karma: int):
    if os.path.isfile("users.json"):
        try:
            with open('users.json', 'r') as fp:
                users = json.load(fp)
            users[user_id]['karma'] += karma
            with open('users.json', 'w') as fp:
                json.dump(users, fp, sort_keys=True, indent=4)
        except KeyError:
            with open('users.json', 'r') as fp:
                users = json.load(fp)
            users[user_id] = {}
            users[user_id]['karma'] = karma
            with open('users.json', 'w') as fp:
                json.dump(users, fp, sort_keys=True, indent=4)
    else:
        users = {user_id: {}}
        users[user_id]['karma'] = karma
        with open('users.json', 'w') as fp:
            json.dump(users, fp, sort_keys=True, indent=4)


def get_karma(user_id: int):
    if os.path.isfile('users.json'):
        with open('users.json', 'r') as fp:
            users = json.load(fp)
        return users[user_id]['karma']

    else:
        return 0


def set_level(user_id: int, level: int):
    if os.path.isfile('users.json'):
        with open('users.json', 'r') as fp:
            users = json.load(fp)
        users[user_id]["level"] = level
        with open('users.json', 'w') as fp:
            json.dump(users, fp, sort_keys=True, indent=4)


def get_level(user_id: int):
    if os.path.isfile('users.json'):
        try:
            with open('users.json', 'r') as fp:
                users = json.load(fp)
            return users[user_id]['level']
        except KeyError:
            return 0


def setup(client):
    client.add_cog(Karma(client))
