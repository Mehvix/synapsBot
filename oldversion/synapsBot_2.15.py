#!/usr/bin/env python
# -*- coding: utf-8 -*-
import asyncio
import datetime
import json
import os
import random
import string
import sys
import math
import discord
from discord.ext import commands
from urbandictionary_top import udtop

# TODO New Commands
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
 #  jerma pirate song                                                                                                #
 #  Mute user                                                                                                        #
 #  ban user                                                                                                         #
 #  kick user                                                                                                        #
 #  Cool down                                                                                                        #
 #  Hearthstone cards (import hearthstone)                                                                           #
 #  delete messages                                                                                                  #
 #  Create invite                                                                                                    #
 #  Invite info                                                                                                      #
 #  Server invites / request (send owner of server DM and option to accept/decline user to server)                   #
 #  Give XP for voice channel usage                                                                                  #
 #  Remind me (x) x == time                                                                                          #
 #  save console to file                                                                                             #
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# How to get custom values
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
You need the following values. They are custom for every server. You can get them by typing in any text channel the 
desired value with a "\" in front of it. I.E. "\@Member" or "\:upvote:"
For your token go to https://discordapp.com/developers/applications/me, creating a new app, and getting the token by 
clicking "reveal".
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


def get_json(file_path):
    with open(file_path, 'r') as fp:
        return json.load(fp)


acc_name = "test"
jsontoken = 0

if acc_name == "test":
    print("Using TEST account")
    jsontoken = get_json('./test_token.json')
    token = jsontoken.get("token")
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

    # Number Emojis (because unicode is hard)
    one_emote = ":onev2:442817606961987585"
    two_emote = ":twov2:442817607020838913"
    three_emote = ":threev2:442817607301726208"
    four_emote = ":fourv2:442817606957924383"
    five_emote = ":fivev2:442817607188348938"
    six_emote = ":sixv2:442817607196868629"
if acc_name == "main":
    print("Using MAIN account")
    jsontoken = get_json('./main_token.json')
    token = jsontoken.get("token")
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

    # Number Emojis (because unicode is hard)
    one_emote = ":one2:442836971161649152"
    two_emote = ":two2:442836971145134080"
    three_emote = ":three2:442836970935156738"
    four_emote = ":four2:442836971145003025"
    five_emote = ":five2:442836971153522688"
    six_emote = ":six2:442836970843013131"

if jsontoken == 0:
    print("WOAH!!! You need a token to go online. Use 'Main' or 'Test")
    exit(0)

print("Token being used: {}".format(jsontoken.get("token")))
print("Connecting...")


# For embed messages
embed_color = 0x1abc9c

description = "synapsBot - A person Discord bot by Mehvix#7172"
footer_text = "synapsBot"
Client = discord.Client()
client = commands.Bot(command_prefix=".")

# Resets uptime settings
seconds = 0
minutes = 0
hours = 0
days = 0

# Resets vote variables
vote_phase = 0
vote_1 = 0
vote_2 = 0
vote_3 = 0
vote_4 = 0
vote_5 = 0
vote_6 = 0

# For deleting/kicking code not messaging twice for bans
ban_message = 0

# Decides if startup is during AM or PM ours (yea damn 'murica time)
if datetime.datetime.now().hour > 12:
    cur_hour = datetime.datetime.now().hour - 12
    am_or_pm = "PM"
else:
    cur_hour = datetime.datetime.now().hour
    am_or_pm = "AM"

# Puts "0" in front of number time
if datetime.datetime.now().minute < 10:
    cur_min = "0{}".format(datetime.datetime.now().minute)
else:
    cur_min = datetime.datetime.now().minute

if datetime.datetime.now().second < 10:
    cur_sec = "0{}".format(datetime.datetime.now().second)
else:
    cur_sec = datetime.datetime.now().second

# Selects random clock emoji for '.uptime' command
clock_emoji = ["🕐", "🕑", "🕒", "🕓", "🕔", "🕕", "🕖", "🕗", "🕘", "🕙", "🕚", "🕛"]  # Use random.choice(clock_emoji)

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


@client.event
async def on_ready():
    users = len(set(client.get_all_members()))
    channels = len([c for c in client.get_all_channels()])
    file_name = os.path.basename(sys.argv[0])  # Gets file name

    r = random.randint(3, 3)
    if r == 1:
        await client.change_presence(game=discord.Game(name="Live for {0}:{1}:00".format(hours, minutes),
                                                       url="https://twitch.tv/mehvix", type=1))
    if r == 2:
        await client.change_presence(game=discord.Game(name="Version {}".format(file_name[10:-3]),
                                                       url="https://twitch.tv/mehvix", type=1))
    if r == 3:
        await client.change_presence(game=discord.Game(name="Created by Mehvix#7172", url="https://twitch.tv/mehvix",
                                                       type=1))
    server_list = list(client.servers)

    print("============================================================")
    print("                                      ____        __")
    print("   _______  ______  ____ _____  _____/ __ )____  / /_")
    print("  / ___/ / / / __ \/ __ `/ __ \/ ___/ /_/ / __ \/ __/")
    print(" /__  / /_/ / / / / /_/ / /_/ /__  / /_/ / /_/ / /_")
    print("/____/\__, /_/ /_/\__,_/ .___/____/_____/\____/\__/")
    print("     /____/           /_/\n")
    print("• Version:                   {}".format(discord.__version__))
    print("• Start Time:                {0}:{1}:{2} {3}".format(cur_hour, cur_min, cur_sec, am_or_pm))
    print("• Client Name:               {}".format(client.user))
    print("• Client ID:                 {}".format(client.user.id))
    print("• Channels:                  {}".format(channels))
    print("• Users:                     {}\n".format(users))
    print("• Connected to " + str(len(client.servers)) + " server(s):")
    for x in range(len(server_list)):
        print("     > " + server_list[x - 1].name)
    print("============================================================")


# Tbh I have no idea what this does. If you know hmu on discord @ Mehvix#7172 ;)
@client.event
async def on_resumed():
    print("{0}:{1}:{2}: Resumed ".format(datetime.datetime.now().hour, datetime.datetime.now().minute,
                                         datetime.datetime.now().second))


# When a user joins the server
@client.event
async def on_member_join(member):
    print("{0}:{1}:{2}: {3} joined".format(datetime.datetime.now().hour, datetime.datetime.now().minute, datetime.
                                           datetime.now().second, member))
    await client.send_message(discord.Object(id=notification_channel), "<@{}> joined the server :tada:"
                              .format(member.id))


# When a user is banned from the server
@client.event
async def on_member_ban(member):
    global ban_message
    ban_message += 1
    print("{0}:{1}:{2}: {3} was banned".format(datetime.datetime.now().hour, datetime.datetime.now().minute,
                                               datetime.datetime.now().second, member))
    await client.send_message(discord.Object(id=notification_channel),
                              "<@{}> was either **banned** :hammer:".format(member.id))
    await client.send_message(discord.Object(id=notification_channel),
                              "`NOTE:` You can check who banned them in the server audit log. :thumbsup: ")


# When a user is kicked or leaves the server
@client.event
async def on_member_remove(member):
    global ban_message
    if ban_message == 1:
        print("Canceled kick message")
        ban_message = 0
    else:
        print("{0}:{1}:{2}: {3} left".format(datetime.datetime.now().hour, datetime.datetime.now().minute,
                                             datetime.datetime.now().second, member))
        await client.send_message(discord.Object(id=notification_channel),
                                  "<@{}> was either kicked or left the server :frowning2:".format(member.id))
        ban_message = 0


# This is for the upvote/downvote system
@client.event
async def on_reaction_add(reaction, user):
    emoji_used = str(reaction.emoji)

    formted_up = "<{}>".format(upvote_emoji)
    formted_down = "<{}>".format(downvote_emoji)
    formated_one = "<{}>".format(one_emote)
    formated_two = "<{}>".format(two_emote)
    formated_three = "<{}>".format(three_emote)
    formated_four = "<{}>".format(four_emote)
    formated_five = "<{}>".format(five_emote)
    formated_six = "<{}>".format(six_emote)

    fulltime = "{0}:{1}:{2} {3}".format(new_cur_hour, new_cur_min, new_cur_sec, new_am_or_pm)

    print("{0}: {1} reacted with {2} to {3}'s message"
          .format(fulltime, user, emoji_used, reaction.message.author))

    if emoji_used == formated_one:
        global vote_1
        vote_1 += 1
        print("{0}:{1}:{2}: {3} voted for #1".format(fulltime, user, emoji_used, reaction.message.author))

    if emoji_used == formated_two:
        global vote_2
        vote_2 += 1
        print("{0}: {1} voted for #2".format(fulltime, user, emoji_used, reaction.message.author))

    if emoji_used == formated_three:
        global vote_3
        vote_3 += 1
        print("{0}: {1} voted for #3".format(fulltime, user, emoji_used, reaction.message.author))
        global vote_4

    if emoji_used == formated_four:
        global vote_4
        vote_4 += 1
        print("{0}: {1} voted for #4".format(fulltime, user, emoji_used, reaction.message.author))

    if emoji_used == formated_five:
        global vote_5
        vote_5 += 1
        print("{0}: {1} voted for #5".format(fulltime, user, emoji_used, reaction.message.author))

    if emoji_used == formated_six:
        global vote_6
        vote_6 += 1
        print("{0}: {1} voted for #6".format(fulltime, user, emoji_used, reaction.message.author))

    if reaction.message.channel.id != pokemon_channel:
        if emoji_used == formted_up:  # If emote is the upvote emote
            if reaction.message.author.id == user.id:
                print("{0}: {1} upvoted there own link. NO CHANGE"
                      .format(fulltime, user))
            else:
                user_add_karma(reaction.user_id, 5)
                print("{0}: ADDED 5 karma to {1} for a UPVOTE from {2}"
                      .format(fulltime, reaction.message.author, user))

        # If emote is the downvote emote
        if emoji_used == formted_down:
            if reaction.message.author.id == user.id:
                print("{0}: {1} downvoted there post. NO CHANGE"
                      .format(fulltime, user))
            else:
                user_add_karma(reaction.user_id, -5)
                print("{0}: REMOVED 5 karma to {1} for a DOWNVOTE from {1}"
                      .format(fulltime, reaction.message.author, user))
    else:
        print("{0}: Didn't change {1}'s karma because they're in the Pokemon Channel!"
              .format(fulltime, user))


# This is more stuff for the upvote/downvote system
@client.event
async def on_reaction_remove(reaction, user):
    emoji_used = str(reaction.emoji)

    formated_up = "<{}>".format(upvote_emoji)
    formated_down = "<{}>".format(downvote_emoji)
    formated_one = "<{}>".format(one_emote)
    formated_two = "<{}>".format(two_emote)
    formated_three = "<{}>".format(three_emote)
    formated_four = "<{}>".format(four_emote)
    formated_five = "<{}>".format(five_emote)
    formated_six = "<{}>".format(six_emote)

    fulltime = "{0}:{1}:{2} {3}".format(new_cur_hour, new_cur_min, new_cur_sec, new_am_or_pm)

    if emoji_used == formated_one:
        global vote_1
        vote_1 -= 1
        print("{0}: {1} removed their vote for #1".format(fulltime, user))

    if emoji_used == formated_two:
        global vote_2
        vote_2 -= 1
        print("{0}: {1} removed their vote for #2".format(fulltime, user))

    if emoji_used == formated_three:
        global vote_3
        vote_3 -= 1
        print("{0}: {1} removed their vote for #3".format(fulltime, user))

    if emoji_used == formated_four:
        global vote_4
        vote_4 -= 1
        print("{0}: {1} removed their vote for #4".format(fulltime, user))

    if emoji_used == formated_five:
        global vote_5
        vote_5 -= 1
        print("{0}: {1} removed their vote for #5".format(fulltime, user))

    if emoji_used == formated_six:
        global vote_6
        vote_6 -= 1
        print("{0}: {1} removed their vote for #6".format(fulltime, user))

    if reaction.message.channel.id != pokemon_channel:
        if emoji_used == formated_up:
            if reaction.user_id == user.id:
                print("{0}: {1} removed their upvote to their post. NO CHANGE".format(fulltime, user.id))
            else:
                user_add_karma(reaction.user_id, -5)
                print("{0}: REMOVED 5 karma from {0} because {1} removed there UPVOTE"
                      .format(fulltime, reaction.message.author, user))

        # If emote is the downvote emote
        if emoji_used == formated_down:
            if reaction.user_id == user.id:
                print("{0}: {1} removed their downvote to there own link. NO CHANGE".format(fulltime, user))
            else:
                user_add_karma(reaction.user_id, 5)
                print("{0}: RE-ADDED 5 karma to {1} for removal of downvote reaction from {2}"
                      .format(fulltime, reaction.message.author, user))
    else:
        print("{0}: Didn't change {1}'s karma because it was in the Pokemon Channel!"
              .format(fulltime, user))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    # Message author variables
    user_id = message.author.id
    user_name = message.author

    author_level = get_level(user_id)
    author_karma = get_karma(user_id)

    # Decides if startup is during AM or PM ours (yea damn 'murican time)
    if datetime.datetime.now().hour > 12:
        new_cur_hour = datetime.datetime.now().hour - 12
        new_am_or_pm = "PM"
    else:
        new_cur_hour = datetime.datetime.now().hour
        new_am_or_pm = "AM"

    # Puts "0" in front of number time
    if datetime.datetime.now().minute < 10:
        new_cur_min = "0{}".format(datetime.datetime.now().minute)
    else:
        new_cur_min = datetime.datetime.now().minute

    if datetime.datetime.now().second < 10:
        new_cur_sec = "0{}".format(datetime.datetime.now().second)
    else:
        new_cur_sec = datetime.datetime.now().second
    fulltime = "{0}:{1}:{2} {3}".format(new_cur_hour, new_cur_min, new_cur_sec, new_am_or_pm)

    # Because @xpoes#9244 spammed the shit out of our pokemon channel
    if message.channel.id == pokemon_channel:
        print("{0}: DIDN'T give karma to {1} for message '{2}' because they sent a message in the Pokemon channel"
              .format(fulltime, message.author, message.content))
    else:
        user_add_karma(user_id, 1)
        print("{0}: ADDED 1 karma to {0} for a message '{2}' in {3}"
              .format(fulltime, user_name, message.content, message.channel.id))

    # Checks Karma / Level
    new_level = author_level + 1
    if author_karma >= 100 * new_level:
        try:
            role_name = "Level {}".format(new_level)
            level_role = discord.utils.get(message.server.roles, name=role_name)
            set_level(user_id, new_level)
            try:
                await client.add_roles(message.author, level_role)
                await client.send_message(message.channel, "Congrats, <@{0}>! You're now level `{1}`.  :tada: ".format(
                    user_id, new_level))
                print("{0}: {1} leveled up to {2}".format(fulltime, user_id, get_level(user_id)))
            except AttributeError:
                print("{0}: {1} leveled up to {2}, but the server doesn't have that role the level name!"
                      .format(fulltime, user_id, new_level))
        except AttributeError:
            print("{0}: {1} leveled up to {2}, but the server doesn't have that role the level name!"
                  .format(fulltime, user_id, new_level))

    if message.content.upper().startswith(".TIME"):
        print("{0}: {1} requested the time".format(fulltime, user_name))
        await client.send_message(message.channel, "I think it's `{0}:{1}:{2} {3}` {4}"
                                  .format(new_cur_hour, new_cur_min, new_cur_sec, new_am_or_pm,
                                          random.choice(clock_emoji)))

    # Upvote Code
    if "HTTP" in message.content.upper():
        try:
            await client.add_reaction(message, upvote_emoji)
        except AttributeError:
            print("{0}: User has not role! (Probably a webhook)".format(fulltime))

    # "Shut Up" code
    if shut_up_role in [role.id for role in message.author.roles]:
        print("{0}: Told {1} to shaddup".format(fulltime, user_name))
        await client.send_message(message.channel, "Shut up <@{}>".format(user_id))

    # Ping Command
    if message.content.upper().startswith(".PING"):
        print("{0}: {1} requested 'PING'".format(fulltime, user_name))
        await client.send_message(message.channel, "Pong! :ping_pong:")

    # About Command
    if message.content.upper().startswith(".ABOUT"):
        print("{0}: {1} requested '.ABOUT'".format(fulltime, user_name))
        embed = discord.Embed(title="Github", url="https://github.com/Mehvix/synaps-bot", color=embed_color)
        embed.set_author(name="About:", url="https://steamcommunity.com/id/Mehvix/",
                         icon_url="https://steamcdn-a.akamaihd.net/steamcommunity/public/images/avatars/08/080527004088"
                                  "e8e461d6fc9a4df248dfd3fa2dc8_full.jpg")
        embed.set_thumbnail(url="https://goo.gl/FCddaV")
        embed.add_field(name="Creator:", value="\u200b", inline=True)
        embed.add_field(name="Mehvix#7172", value="\u200b", inline=True)
        await client.send_message(message.channel, embed=embed)

    # TODO Update this
    # Help Command
    if message.content.upper().startswith(".HELP"):
        print("{0}: {1} requested '.HELP'".format(fulltime, user_name))
        embed = discord.Embed(title="Commands:", color=embed_color)
        embed.add_field(name=".help", value="This command.", inline=False)
        embed.add_field(name=".ping", value="Play Ping-Pong with the bot.", inline=False)
        embed.add_field(name=".uptime", value="Returns however long the bot has been online.", inline=False)
        embed.add_field(name=".8ball +question", value="Returns the true answer to a question.", inline=False)
        embed.add_field(name=".about", value="Returns info on the bot.", inline=False)
        embed.add_field(name=".karma", value="Returns your karma amount.", inline=False)
        embed.add_field(name=".karma @name", value="Returns (name's) karma amount.", inline=False)
        embed.add_field(name=".ud +word", value="Returns (word) definition on Urban Dictionary.", inline=False)
        embed.add_field(name=".serverrules (admin)", value="Outputs the Server Rules.", inline=False)
        await client.send_message(message.channel, embed=embed)

    if "bot?" in message.content:
        print(message.author.bot)

    if "send bot" in message.content:
        await client.send_message(message.channel, "bot?")

    # ".Accept" code
    role = discord.utils.get(message.server.roles, name=member_role_name)
    if message.author.bot is True:
        pass
    else:
        if member_role_id not in [role.id for role in message.author.roles]:
            if message.content.upper().startswith(".ACCEPT"):
                await client.add_roles(user_name, role)
                await client.delete_message(message)
                await client.send_message(discord.Object(id=notification_channel),
                                          "<@{}> is now a Member :ok_hand:".format(user_id))
                print("{0}: {1} joined the server (.accept)".format(fulltime, user_name))
            else:
                await client.delete_message(message)
                print("{0}: didn't type '.accept'".format(fulltime, user_name))

    # Verified Code
    words = [".UD", ".8BALL", ".UPTIME", ".LEVEL", ".BEAR", ".KARMA", ".CREATEPOLL", ".SAM", ".BETA", ".SERVERINFO",
             ".VERSION", ".USER", ".WHOIS", ".LOAD"]
    for word in words:
        if message.content.upper().startswith(word):
            if verified_role_id in [role.id for role in message.author.roles]:
                print("{0}: {1} activated a verified command".format(fulltime, user_name))

                # UD Code
                if message.content.upper().startswith(".UD"):
                    target_def = message.content[4:]
                    target_def_link_format = target_def.replace(" ", "%20")

                    if "MAGGIE" in message.content.upper():
                        print("{0}: {1}  requested the UD for Maggie".format(fulltime, user_name))
                        embed = discord.Embed(title="Definition Page", url="https://goo.gl/j2DX9N", color=embed_color)
                        embed.set_author(name="Definition for Maggie", url="https://goo.gl/j2DX9N")
                        embed.set_footer(text="Girl with YUUUG milkers. Doesnt need a coat")
                        await client.send_message(message.channel, embed=embed)
                    else:
                        try:
                            term = udtop(target_def)
                            print("{0}  requested the UD for {1}".format(user_name, target_def))
                            embed = discord.Embed(title="Definition Page",
                                                  url="https://www.urbandictionary.com/define.php?term={}"
                                                  .format(target_def.replace(" ", "%20")), color=embed_color)
                            embed.set_author(name="Definition for {}".format(string.capwords(target_def)),
                                             url="https://www.urbandictionary.com/define.php?term={}"
                                             .format(target_def))
                            embed.add_field(name="Definition", value=term.definition[:2000], inline=False)
                            embed.add_field(name="Example", value=term.example, inline=True)
                            await client.send_message(message.channel, embed=embed)
                        except AttributeError:
                            await client.send_message(message.channel, "Sorry, that word doesnt have a definition :( . "
                                                                       "You can add your own here: ")
                            await client.send_message(message.channel, "https://www.urbandictionary.com/add.php?word="
                                                      + target_def_link_format)

                # 8Ball Code
                elif message.content.upper().startswith(".8BALL"):
                    print("{0}: {1} requested '.8BALL'".format(fulltime, user_name))

                    def get_answer(answer_number):
                        if answer_number == 1:
                            return "It is certain"
                        elif answer_number == 2:
                            return "It is decidedly so"
                        elif answer_number == 3:
                            return "Yes"
                        elif answer_number == 4:
                            return "Reply hazy try again"
                        elif answer_number == 5:
                            return "Ask again later"
                        elif answer_number == 6:
                            return "Concentrate and ask again"
                        elif answer_number == 7:
                            return "My reply is **no**"
                        elif answer_number == 8:
                            return "Outlook not so good"
                        elif answer_number == 9:
                            return "Very doubtful"
                    r = random.randint(1, 9)
                    fortune = get_answer(r)
                    await client.send_message(message.channel, fortune)

                # Version Game
                file_name = os.path.basename(sys.argv[0])  # Gets file name
                if message.content.upper().startswith(".VERSION"):
                    print("{0}: {1} requested '.VERSION'".format(fulltime, user_name))
                    await client.send_message(message.channel, "The bot is currently running version `{}`"
                                              .format(file_name[10:-3]))

                # Uptime Code
                if message.content.upper().startswith(".UPTIME"):
                    print("{0}: {1} requested '.UPTIME'".format(fulltime, user_name))
                    if days >= 1:
                        await client.send_message(message.channel,
                                                  "The bot has been live since `{4):{5}:{6} {7}` for `{0}` day(s), "
                                                  "`{1}` hours, `{2}` minute(s), and `{3}` second(s)! {8}"
                                                  .format(days, hours, minutes, seconds, cur_hour, cur_min, cur_sec,
                                                          am_or_pm, random.choice(clock_emoji)))
                    elif hours >= 1:
                        await client.send_message(message.channel,
                                                  "The bot has been live since `{3}:{4}:{5} {6}` for `{0}` hour(s), "
                                                  "`{1}` minute(s), and `{2}` second(s)! {7}"
                                                  .format(hours, minutes, seconds, cur_hour, cur_min, cur_sec,
                                                          am_or_pm, random.choice(clock_emoji)))
                    elif minutes >= 1:
                        await client.send_message(message.channel,
                                                  "The bot has been live since `{2}:{3}:{4} {5}` for `{0}` minutes, "
                                                  "`{1}` seconds {6}"
                                                  .format(minutes, seconds, cur_hour, cur_min, cur_sec, am_or_pm,
                                                          random.choice(clock_emoji)))
                    else:
                        await client.send_message(message.channel, "The bot has been live since `{1}:{2}:{3} {4}` for "
                                                                   "`{0}` seconds {5}"
                                                  .format(seconds, cur_hour, cur_min, cur_sec, am_or_pm,
                                                          random.choice(clock_emoji)))

                # Leveling
                if message.content.upper().startswith(".LEVEL"):
                    level_target = message.content[6:]
                    if level_target == "":
                        user_level_req = user_id
                    else:
                        if not message.raw_mentions:
                            await client.send_message(message.channel, "You need to `@` a user")
                            break
                        else:
                            user_level_req = message.content[10:-1]
                    print("{0}: {1} requested {2}'s level".format(fulltime, user_name, user_level_req))
                    await client.send_message(message.channel, "<@{0}> is level `{1}`"
                                              .format(user_level_req, get_level(user_level_req)))

                # Gets random bear picture
                if message.content.upper().startswith(".BEAR"):
                    if message.channel.id == notification_channel:
                        await client.send_message(message.channel, "Sorry, that command is banned in <#{}>"
                                                  .format(notification_channel))
                    else:
                        print("{0} sent a bear in {1} (banned in {2})".format(user_name, message.channel,
                                                                              notification_channel))
                        fp = random.choice(os.listdir("bears"))
                        await client.send_file(message.channel, "bears/{}".format(fp))

                # Gets random Sam picture
                if message.content.upper().startswith(".SAM"):
                    if message.channel.id == notification_channel:
                        await client.send_message(message.channel, "Sorry, that command is banned in <#{}>"
                                                  .format(notification_channel))
                    else:
                        print("{0} sent a sam in {1} (banned in {2})".format(user_name, message.channel,
                                                                             notification_channel))
                        fp = random.choice(os.listdir("sams"))
                        await client.send_file(message.channel, "sams/{}".format(fp))

                # Server Info
                if message.content.upper().startswith(".SERVERINFO"):
                    print("{0}: {1} requested '.SERVER'".format(fulltime, user_name))
                    online = 0
                    for i in message.server.members:
                        if str(i.status) == "online" or str(i.status) == "idle" or str(i.status) == "dnd":
                            online += 1

                    role_count = len(message.server.roles)
                    emoji_count = len(message.server.emojis)
                    server_created_time = message.server.created_at

                    print("{0}: {1} activated the SERVER command".format(user_name, fulltime))
                    em = discord.Embed(color=embed_color)
                    em.add_field(name="Name:", value=message.server.name)
                    em.add_field(name="Owner:", value=message.server.owner, inline=False)
                    em.add_field(name="Members:", value=message.server.member_count)
                    em.add_field(name="Currently Online:", value=online)
                    # em.add_field(name="Text Channels", value=str(channel_count))
                    em.add_field(name="Region:", value=message.server.region)
                    em.add_field(name="Verification Level:", value=str(message.server.verification_level).capitalize())
                    em.add_field(name="Highest ranking role:", value=message.server.role_hierarchy[0])
                    em.add_field(name="Number of roles:", value=str(role_count))
                    em.add_field(name="Number of custom emotes:", value=str(emoji_count))
                    em.add_field(name="Created At:", value=str(server_created_time)[:10])
                    em.add_field(name="Default Channel:", value=message.server.default_channel)
                    em.add_field(name="AFK Time:", value=message.server.afk_timeout)
                    em.add_field(name="AFK Channel:", value=message.server.afk_channel)
                    em.add_field(name="Voice Client:", value=message.server.voice_client)
                    if message.server.icon_url is None:
                        print("There is no server URL!")
                    else:
                        em.set_thumbnail(url=message.server.icon_url)
                    em.set_author(name="Server Info")
                    em.set_footer(text="Server ID: {}".format(message.server.id))
                    await client.send_message(message.channel, embed=em)

                # Gives link to beta testing server
                if message.content.upper().startswith(".BETA"):
                    print("{0}: {1} activated the BETA command".format(user_name, fulltime))
                    user = await client.get_user_info(user_id)
                    await client.send_message(message.channel, "Hey <@!196355904503939073>, <@{}> wants beta access. "
                                                               "Type `.allow` to send them an invite".format(user_id))
                    msg = await client.wait_for_message(content=".allow")
                    if msg is None:
                        await client.send_message(message.channel, "<@!196355904503939073> didn't respond in time :(. "
                                                                   "Please try another time.")
                    else:
                        if msg.author.id == "196355904503939073":
                            await client.send_message(user, "You've been accepted! https://discord.gg/wjPwUJx")
                            await client.send_message(message.channel, "<@!196355904503939073> just accepted <@{}>"
                                                      .format(user_id))
                            # await client.send_message(message.channel, "https://discord.gg/wjPwUJx")
                        else:
                            await client.send_message(message.channel, "You can't do that!")

                # Karma System
                if message.content.upper().startswith(".KARMA"):
                    karma_target = message.content[6:]
                    if karma_target == "":
                        user_req = user_id
                    else:
                        if not message.raw_mentions:
                            await client.send_message(message.channel, "You need to `@` a user")
                            break
                        else:
                            user_req = message.content[10:-1]

                    await client.send_message(
                        message.channel, "<@{0}> has `{1}` karma".format(user_req, get_karma(user_req)))

                # TODO
                # Remove str() from update printing
                # Fix poll_time_reformat

                # Poll System
                if message.content.upper().startswith(".CREATEPOLL"):
                    global vote_phase
                    if vote_phase != 1:
                        vote_phase += 1
                        print("{0}: {1} created a poll".format(fulltime, user_name))
                        await client.delete_message(message)

                        embed = discord.Embed(title="\u200b", color=embed_color)
                        embed.set_author(name="Generating a poll for {0} {1}"
                                         .format(user_name, random.choice(clock_emoji)))
                        embed.add_field(name="\u200b", value="\u200b", inline=False)
                        embed.add_field(name="Question", value="How long should this pole go on in minutes "
                                                               "(no more than 60)", inline=False)

                        msg = await client.send_message(message.channel, embed=embed)

                        # Time
                        # time_bot = await client.send_message(
                        #     message.channel, "How long should this pole go on in minutes (no more than 60)")
                        time1 = await client.wait_for_message(
                            timeout=120, author=message.author, channel=message.channel)

                        try:
                            poll_time_raw = float(time1.content)
                            poll_time_reformat = float(str(poll_time_raw).replace(".", ""))

                            print("Time set to {}".format(poll_time_raw))
                            await client.delete_message(time1)
                            # await client.delete_message(time_bot)
                        except ValueError:
                            await client.send_message(message.channel, "You didn't reply a number!")
                            break
                        except AttributeError:
                            await client.send_message(
                                message.channel, "<@{}> didn't respond fast enough, so the poll was cancelled".format(
                                    message.author.id))
                            break

                        if poll_time_raw < .5:
                            await client.send_message(
                                message.channel, "Sorry, you can't have a less than `30` second poll")
                            break

                        if poll_time_raw > 60:
                            await client.send_message(
                                message.channel, "Sorry, you can't have more than a `60` minute poll")
                            break

                        title_embed = discord.Embed(title="\u200b", color=embed_color)
                        title_embed.set_author(name="Generating a poll for {0} {1}".format(user_name,
                                                                                           random.choice(clock_emoji)))
                        title_embed.add_field(name="Length:", value=poll_time_reformat, inline=True)
                        title_embed.add_field(name="\u200b", value="\u200b", inline=False)
                        title_embed.add_field(name="Question", value="What would you like the title to be?",
                                              inline=False)
                        await client.edit_message(msg, embed=title_embed)

                        # Title
                        title = await client.wait_for_message(
                            timeout=120, author=message.author, channel=message.channel)

                        try:
                            poll_title = title.content
                            print("Set title to {}".format(poll_title))
                            await client.delete_message(title)
                        #    await client.delete_message(title_bot)
                        except AttributeError:
                            await client.send_message(
                                message.channel, "<@{}> didn't respond fast enough, so the poll was cancelled".format(
                                    message.author.id))
                            break

                        options_embed = discord.Embed(title="\u200b", color=embed_color)
                        options_embed.set_author(name="Generating a poll for {0} {1}".format(user_name,
                                                                                           random.choice(clock_emoji)))
                        options_embed.add_field(name="Length:", value=poll_time_reformat, inline=True)
                        options_embed.add_field(name="Title:", value=str(poll_title), inline=True)
                        options_embed.add_field(name="\u200b", value="\u200b", inline=False)
                        options_embed.add_field(
                            name="Question", value="How many options do you want their to be? (No more than 6)",
                            inline=False)
                        await client.edit_message(msg, embed=options_embed)

                        # Number of Options
                        # num_bot = await client.send_message(
                        #     message.channel, "How many options do you want their to be? (No more than 6)")
                        options = await client.wait_for_message(
                            timeout=120, author=message.author, channel=message.channel)

                        try:
                            poll_options = int(options.content)
                            print("Number of options set to {}".format(poll_options))
                            # await client.delete_message(num_bot)
                            await client.delete_message(options)
                        except ValueError:
                            await client.send_message(
                                message.channel, "You can only use **whole** numbers, no decimals!")
                            break
                        except AttributeError:
                            await client.send_message(
                                message.channel, "<@{}> didn't respond fast enough, so the poll was cancelled".format(
                                    message.author.id))
                            break

                        # Option debugging
                        if poll_options <= 1:
                            await client.send_message(message.channel, "Sorry, You can't have 1 option")
                            break
                        if poll_options > 6:
                            await client.send_message(message.channel, "Sorry, You can't have more than 6 options!")
                            break

                        one_embed = discord.Embed(title="\u200b", color=embed_color)
                        one_embed.set_author(name="Generating a poll for {0} {1}".format(user_name,
                                                                                             random.choice(
                                                                                                 clock_emoji)))
                        one_embed.add_field(name="Length:", value=str(poll_time_reformat), inline=True)
                        one_embed.add_field(name="Title:", value=str(poll_title), inline=True)
                        one_embed.add_field(name="Number of Options:", value=str(poll_options), inline=True)
                        one_embed.add_field(name="\u200b", value="\u200b", inline=False)
                        one_embed.add_field(
                            name="Question", value="What should option one be called?",
                            inline=False)
                        await client.edit_message(msg, embed=one_embed)

                        # Gets Option 1
                        # bot_opt1 = await client.send_message(
                        #     message.channel, "What would you like option `one` to be called?")
                        option_1 = await client.wait_for_message(timeout=120, author=message.author,
                                                                 channel=message.channel)
                        try:
                            poll_option_1 = option_1.content
                            print("Option 1 set to {}".format(poll_option_1))
                            await client.delete_message(option_1)
                            # await client.delete_message(bot_opt1)

                        except AttributeError:
                            await client.send_message(
                                message.channel,
                                "<@{}> didn't respond fast enough, so the poll was cancelled".format(
                                    message.author.id))
                            break

                        two_embed = discord.Embed(title="\u200b", color=embed_color)
                        two_embed.set_author(name="Generating a poll for {0} {1}".format(user_name,
                                                                                         random.choice(
                                                                                             clock_emoji)))
                        two_embed.add_field(name="Length:", value=str(poll_time_reformat), inline=True)
                        two_embed.add_field(name="Title:", value=str(poll_title), inline=True)
                        two_embed.add_field(name="Number of Options:", value=str(poll_options), inline=True)
                        two_embed.add_field(name="Option 1:", value=str(poll_option_1), inline=True)
                        two_embed.add_field(name="\u200b", value="\u200b", inline=False)
                        two_embed.add_field(
                            name="Question", value="What should option two be called?",
                            inline=False)
                        await client.edit_message(msg, embed=two_embed)

                        # Gets Option 2
                        # bot_opt2 = await client.send_message(
                        #     message.channel, "What would you like option `two` to be called?")
                        option_2 = await client.wait_for_message(
                            timeout=120, author=message.author, channel=message.channel)

                        try:
                            poll_option_2 = option_2.content
                            print("Option 2 set to {}".format(poll_option_2))
                            # await client.delete_message(bot_opt2)
                            await client.delete_message(option_2)

                        except AttributeError:
                            await client.send_message(
                                message.channel,
                                "<@{}> didn't respond fast enough, so the poll was cancelled".format(
                                    message.author.id))
                            break

                        if poll_options >= 3:

                            three_embed = discord.Embed(title="\u200b", color=embed_color)
                            three_embed.set_author(
                                name="Generating a poll for {0} {1}".format(user_name, random.choice(clock_emoji)))
                            three_embed.add_field(name="Length:", value=str(poll_time_reformat), inline=True)
                            three_embed.add_field(name="Title:", value=str(poll_title), inline=True)
                            three_embed.add_field(name="Number of Options:", value=str(poll_options), inline=True)
                            three_embed.add_field(name="Option 1:", value=str(poll_option_1), inline=True)
                            three_embed.add_field(name="Option 2:", value=str(poll_option_2), inline=True)
                            three_embed.add_field(name="\u200b", value="\u200b", inline=False)
                            three_embed.add_field(
                                name="Question", value="What should option three be called?",
                                inline=False)
                            await client.edit_message(msg, embed=three_embed)

                            # Option 3
                            # bot_opt3 = await client.send_message(
                            #     message.channel, "What would you like option `three` to be called?")
                            option_3 = await client.wait_for_message(
                                timeout=120, author=message.author, channel=message.channel)

                            try:
                                poll_option_3 = option_3.content
                                print("Option 3 set to {}".format(poll_option_3))
                                # await client.delete_message(bot_opt3)
                                await client.delete_message(option_3)

                            except AttributeError:
                                await client.send_message(
                                    message.channel,
                                    "<@{}> didn't respond fast enough, so the poll was cancelled".format(
                                        message.author.id))
                                break

                            if poll_options >= 4:
                                four_embed = discord.Embed(title="\u200b", color=embed_color)
                                four_embed.set_author(
                                    name="Generating a poll for {0} {1}".format(user_name, random.choice(clock_emoji)))
                                four_embed.add_field(name="Length:", value=str(poll_time_reformat), inline=True)
                                four_embed.add_field(name="Title:", value=str(poll_title), inline=True)
                                four_embed.add_field(name="Number of Options:", value=str(poll_options), inline=True)
                                four_embed.add_field(name="Option 1:", value=str(poll_option_1), inline=True)
                                four_embed.add_field(name="Option 2:", value=str(poll_option_2), inline=True)
                                four_embed.add_field(name="Option 3:", value=str(poll_option_3), inline=True)
                                four_embed.add_field(name="\u200b", value="\u200b", inline=False)
                                four_embed.add_field(
                                    name="Question", value="What should option four be called?",
                                    inline=False)
                                await client.edit_message(msg, embed=four_embed)

                                # Option 4
                                # bot_opt4 = await client.send_message(
                                #     message.channel, "What would you like option `four` to be called?")
                                option_4 = await client.wait_for_message(timeout=120, author=message.author,
                                                                         channel=message.channel)

                                try:
                                    poll_option_4 = option_4.content
                                    print("Option 4 set to {}".format(poll_option_4))
                                #    await client.delete_message(bot_opt4)
                                    await client.delete_message(option_4)

                                except AttributeError:
                                    await client.send_message(
                                        message.channel,
                                        "<@{}> didn't respond fast enough, so the poll was cancelled".format(
                                            message.author.id))
                                    break

                                if poll_options >= 5:
                                    five_embed = discord.Embed(title="\u200b", color=embed_color)
                                    five_embed.set_author(
                                        name="Generating a poll for {0} {1}".format(user_name,
                                                                                    random.choice(clock_emoji)))
                                    five_embed.add_field(name="Length:", value=str(poll_time_reformat), inline=True)
                                    five_embed.add_field(name="Title:", value=str(poll_title), inline=True)
                                    five_embed.add_field(name="Number of Options:", value=str(poll_options),
                                                         inline=True)
                                    five_embed.add_field(name="Option 1:", value=str(poll_option_1), inline=True)
                                    five_embed.add_field(name="Option 2:", value=str(poll_option_2), inline=True)
                                    five_embed.add_field(name="Option 3:", value=str(poll_option_3), inline=True)
                                    five_embed.add_field(name="Option 4:", value=str(poll_option_4), inline=True)
                                    five_embed.add_field(name="\u200b", value="\u200b", inline=False)
                                    five_embed.add_field(
                                        name="Question", value="What should option five be called?",
                                        inline=False)
                                    await client.edit_message(msg, embed=five_embed)

                                    # Option 5
                                    # bot_opt5 = await client.send_message(
                                    #     message.channel, "What would you like option `five` to be called?")
                                    option_5 = await client.wait_for_message(
                                        timeout=120, author=message.author, channel=message.channel)

                                    try:
                                        poll_option_5 = option_5.content
                                        print("Option 5 set to {}".format(poll_option_5))
                                    #   await client.delete_message(bot_opt5)
                                        await client.delete_message(option_5)

                                    except AttributeError:
                                        await client.send_message(
                                            message.channel,
                                            "<@{}> didn't respond fast enough, so the poll was cancelled".format(
                                                message.author.id))
                                        break

                                    if poll_options == 6:
                                        six_embed = discord.Embed(title="\u200b", color=embed_color)
                                        six_embed.set_author(
                                            name="Generating a poll for {0} {1}".format(user_name,
                                                                                        random.choice(clock_emoji)))
                                        six_embed.add_field(name="Length:", value=str(poll_time_reformat), inline=True)
                                        six_embed.add_field(name="Title:", value=str(poll_title), inline=True)
                                        six_embed.add_field(name="Number of Options:", value=str(poll_options),
                                                            inline=True)
                                        six_embed.add_field(name="Option 1:", value=str(poll_option_1), inline=True)
                                        six_embed.add_field(name="Option 2:", value=str(poll_option_2), inline=True)
                                        six_embed.add_field(name="Option 3:", value=str(poll_option_3), inline=True)
                                        six_embed.add_field(name="Option 4:", value=str(poll_option_4), inline=True)
                                        six_embed.add_field(name="Option 5:", value=str(poll_option_5), inline=True)
                                        six_embed.add_field(name="\u200b", value="\u200b", inline=False)
                                        six_embed.add_field(
                                            name="Question", value="What should option six be called?",
                                            inline=False)
                                        await client.edit_message(msg, embed=six_embed)

                                        # Option 6
                                        # bot_opt6 = await client.send_message(
                                        #     message.channel, "What would you like option `six` to be called?")
                                        option_6 = await client.wait_for_message(
                                            timeout=120, author=message.author, channel=message.channel)

                                        try:
                                            poll_option_6 = option_6.content
                                            print("Option 6 set to {}".format(poll_option_6))
                                        #    await client.delete_message(bot_opt6)
                                            await client.delete_message(option_6)

                                            await client.delete_message(msg)

                                        except AttributeError:
                                            await client.send_message(
                                                message.channel,
                                                "<@{}> didn't respond fast enough, so the poll was cancelled".format
                                                (message.author.id))
                                            break
                                else:
                                    await client.delete_message(msg)
                            else:
                                await client.delete_message(msg)
                        else:
                            await client.delete_message(msg)
                        embed = discord.Embed(
                            title=string.capwords(poll_title),
                            description="Created by: {}".format(user_name), color=embed_color)
                        embed.set_thumbnail(
                            url="https://png.icons8.com/metro/1600/poll-topic.png")
                        embed.add_field(
                            name="1️⃣  Option 1:", value=string.capwords(poll_option_1), inline=True)
                        embed.add_field(
                            name="2️⃣  Option 2:", value=string.capwords(poll_option_2), inline=True)
                        if poll_options >= 3:
                            embed.add_field(
                                name="3️⃣  Option 3:", value=string.capwords(poll_option_3), inline=True)
                            if poll_options >= 4:
                                embed.add_field(
                                    name="4️⃣  Option 4:", value=string.capwords(poll_option_4), inline=True)
                                if poll_options >= 5:
                                    embed.add_field(
                                        name="5️⃣  Option 5:", value=string.capwords(poll_option_5), inline=True)
                                    if poll_options == 6:
                                        embed.add_field(
                                            name="6️⃣  Option 6:", value=string.capwords(poll_option_6),
                                            inline=True)
                        embed.set_footer(
                            text="I'll announce the winners {0} minutes ⏰".format(poll_time_reformat))
                        poll_message = await client.send_message(message.channel, embed=embed)

                        await client.add_reaction(poll_message, one_emote)
                        await client.add_reaction(poll_message, two_emote)
                        if poll_options >= 3:
                            await client.add_reaction(poll_message, three_emote)
                            if poll_options >= 4:
                                await client.add_reaction(poll_message, four_emote)
                                if poll_options >= 5:
                                    await client.add_reaction(poll_message, five_emote)
                                    if poll_options == 6:
                                        await client.add_reaction(poll_message, six_emote)

                        time_in_min = float(poll_time_raw * 60)
                        await asyncio.sleep(time_in_min)
                        await client.send_message(
                            message.channel, "Option `{}` won the vote! :tada:".format(
                                max(vote_1, vote_2, vote_3, vote_4, vote_5, vote_6)))
                        vote_1 = 0
                        vote_2 = 0
                        vote_3 = 0
                        vote_4 = 0
                        vote_5 = 0
                        vote_6 = 0
                        vote_phase -= 1
                    else:
                        await client.send_message(message.channel, "Sorry, another vote is taking place right now!")

                if message.content.upper().startswith(".LOAD"):
                    msg = await client.send_message(message.channel, clock_emoji[11])
                    i = 0
                    while i < 12:
                        await asyncio.sleep(1)
                        if i == 0:
                            await client.edit_message(msg, clock_emoji[0])
                        if i == 1:
                            await client.edit_message(msg, clock_emoji[1])
                        if i == 2:
                            await client.edit_message(msg, clock_emoji[2])
                        if i == 3:
                            await client.edit_message(msg, clock_emoji[3])
                        if i == 4:
                            await client.edit_message(msg, clock_emoji[4])
                        if i == 5:
                            await client.edit_message(msg, clock_emoji[5])
                        if i == 6:
                            await client.edit_message(msg, clock_emoji[6])
                        if i == 7:
                            await client.edit_message(msg, clock_emoji[7])
                        if i == 8:
                            await client.edit_message(msg, clock_emoji[8])
                        if i == 9:
                            await client.edit_message(msg, clock_emoji[9])
                        if i == 10:
                            await client.edit_message(msg, clock_emoji[10])
                        if i == 11:
                            await client.edit_message(msg, clock_emoji[11])
                            i = 0
                        i += 1

                # Who-is command
                # Assistance from https://gist.github.com/Grewoss/c0601832982a99f59cc73510f7841fe4
                if message.content.upper().startswith(".WHOIS"):
                    print("{0}: {1} requested '.WHOIS'".format(fulltime, user_name))
                    user = message.mentions[0]
                    full_user_name = "{}#{}".format(user.name, user.discriminator)
                    if message.content[7:] is None:
                        await client.send_message(message.channel, "You forgot to '@' a user!")
                    else:
                        try:
                            user_join_date = str(user.joined_at).split('.', 1)[0]
                            user_created_at_date = str(user.created_at).split('.', 1)[0]

                            embed = discord.Embed(title="Username:", description=full_user_name, color=embed_color)
                            embed.set_author(name="User Info")
                            embed.add_field(name="Joined the server at:", value=user_join_date[:10])
                            embed.add_field(name="User Created at:", value=user_created_at_date[:10])
                            embed.add_field(name="User ID:", value=user.id)
                            embed.add_field(name="User Status:", value=user.status)
                            embed.add_field(name="User Game:", value=user.game)
                            embed.add_field(name="User Custom Name:", value=user.nick)
                            embed.add_field(name="User Color:", value=user.color)
                            embed.add_field(name="User Top Role (Level):", value=user.top_role)
                            embed.set_thumbnail(url=user.avatar_url)
                            await client.send_message(message.channel, embed=embed)
                        except IndexError:
                            print("{0}: {1} requested '.WHOIS' but they didn't exist".format(fulltime, user_name))
                            await client.send_message(message.channel, "Sorry, but I couldn't find that user")
                        finally:
                            pass

            else:
                # If user isn't Verified
                print("{0}: {1} requested for a verified command but doesn't have verified".format(fulltime, user_name))
                if verified_role_id not in [role.id for role in message.author.roles]:
                    await client.send_message(message.channel,
                                              "Sorry, <@{0}>. You have to be {1} to use that command! Just put `[TS]` "
                                              "in front of your steam name and send <@196355904503939073> a link to "
                                              "your account.".format(user_id, verified_role_name))

    # Admin Commands
    words = [".BAN", ".KICK", ".SERVERRULES", ".MUTE", ".UNMUTE", ".POKER"]
    for word in words:
        if message.content.upper().startswith(word):
            if admin_role_id in [role.id for role in message.author.roles]:
                print("{0}: {1} activated an admin command".format(fulltime, user_name))

                if message.content.upper().startswith(".SERVERRULES"):
                    print("{0}: {1} requested '.SEVERRULES'".format(fulltime, user_name))
                    await client.delete_message(message)
                    embed = discord.Embed(title="Synaps Rules and Info",
                                          url="https://steamcommunity.com/groups/team_synaps", color=embed_color)
                    embed.set_thumbnail(url="https://goo.gl/ibJU2z")
                    embed.add_field(name="📜 Rules 1.)", value="No spamming.", inline=True)
                    embed.add_field(name="👙 Rules 2.)", value="No NSFW in Discussion.", inline=True)
                    embed.add_field(name="🎵 Rules 3.)", value="Please keep music requests in the music que channel.",
                                    inline=True)
                    embed.add_field(name="🔰 Getting Verified:",
                                    value="Just add '[TS]' to your steam name and DM a Admin.", inline=True)
                    embed.add_field(
                        name="🔸 Getting Member:",
                        value="Read the rules above and type '.accept' in here. If for whatever reason it doesnt work, "
                              "contact  an {}.".format(admin_role_name), inline=True)
                    await client.send_message(message.channel, embed=embed)
                    await client.send_message(message.channel, "**Team Synaps Links**")
                    await client.send_message(message.channel, "• http://steamcommunity.com/groups/team_synaps")
                    await client.send_message(
                        message.channel, "• https://socialclub.rockstargames.com/crew/team_synaps")
                    await client.send_message(message.channel, "• https://blizzard.com/invite/XKp33F07e)")

                # TODO
                role = discord.utils.get(message.server.roles, name=mute_role_name)
                if message.content.upper().startswith(".MUTE"):
                    mute_target_id = int(message.content[8:-1])
                    mute_target_name = discord.Server.get_member(user_id=mute_target_id)
                    await client.add_roles(mute_target_name, role)
                    print("{0}: {1} muted {2}".format(fulltime, user_name, mute_target))
                    await client.send_message(message.channel, "<@{0}> muted <@{1}> :zipper_mouth:"
                                              .format(user_id, mute_target))

                # TODO
                if message.content.upper().startswith(".BAN"):
                    ban_target = message.content[7:-1]

                    print("ban target = {}".format(discord.Server.get_member(ban_target)))
                    if not message.raw_mentions:
                        await client.send_message(message.channel, "You need to `@` a user")
                    else:
                        print(discord.Server.get_member(ban_target))
                        await client.ban(member=server.get_member(ban_target))

            else:
                if admin_role_id not in [role.id for role in message.author.roles]:
                    print("{0}: {1} requested '.SEVERRULES' but wasn't an admin".format(fulltime, user_name))
                    await client.send_message(message.channel,
                                              "Sorry, <@{}>. Only {}'s have permission to use this"
                                              .format(user_id, admin_role_name))

    if message.content.startswith("This is an automated message to spawn Pokémon."):
        print("{0}: {1} sent the pokemon spam message".format(fulltime, user_name))
        await client.delete_message(message)

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


async def uptime():
    await client.wait_until_ready()
    global seconds
    seconds = 0
    global minutes
    minutes = 0
    global hours
    hours = 0
    global days
    days = 0
    while not client.is_closed:
        await asyncio.sleep(1)
        seconds += 1
        if seconds == 60:
            seconds = 0
            minutes += 1
        elif minutes == 60:
            minutes = 0
            hours += 1
        elif hours == 24:
            hours = 0
            days += 1


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


client.loop.create_task(uptime())

client.run(token)