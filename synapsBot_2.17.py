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
>  jerma pirate song
>  gambling and poker (casino games)
>  ban list
>  Mute user
>  Cool down
>  Hearthstone cards (import hearthstone)
>  delete messages
>  Create invite
>  Invite info
>  Give XP for voice channel usage
>  Remind me (x) x == time
>  save console to file
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


def get_time():
    # Decides if startup is during AM or PM ours (yea damn 'murica time)
    if datetime.datetime.now().hour > 13:
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

    return "{0}:{1}:{2} {3}".format(cur_hour, cur_min, cur_sec, am_or_pm)


acc_name = "main"
jsontoken = 0

if acc_name == "test":
    print("Using TEST account")
    jsontoken = get_json('C:/Users/maxla/PycharmProjects/synapsBot remastered/test_token.json')
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
    jsontoken = get_json('C:/Users/maxla/PycharmProjects/synapsBot remastered/main_token.json')
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

# For deleting/kicking code not messaging twice for bans
ban_message = 0

# Selects random clock emoji for '.uptime' command
clock_emoji = ["🕐", "🕑", "🕒", "🕓", "🕔", "🕕", "🕖", "🕗", "🕘", "🕙", "🕚", "🕛"]  # Use random.choice(clock_emoji)


# Roulette Settings
roulette_red = {1, 3, 5, 7, 9, 12, 14, 16, 18, 21, 23, 25, 27, 30, 32, 34, 36}
roulette_black = {2, 4, 6, 8, 10, 11, 13, 15, 17, 19, 20, 22, 24, 26, 28, 29, 31, 33, 35}
roulette_green = 0
roulette_even = {2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36}
roulette_odd = {1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35}

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


@client.event
async def on_ready():
    users = len(set(client.get_all_members()))
    channels = len([c for c in client.get_all_channels()])
    file_name = os.path.basename(sys.argv[0])  # Gets file name

    r = random.randint(1, 3)
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
    print("• Start Time:                {}".format(get_time()))
    print("• Client Name:               {}".format(client.user))
    print("• Client ID:                 {}".format(client.user.id))
    print("• Channels:                  {}".format(channels))
    print("• Users:                     {}\n".format(users))
    print("• Connected to " + str(len(client.servers)) + " server(s):")
    for x in range(len(server_list)):
        print("     > " + server_list[x - 1].name)
    print("============================================================")


# Tbh I have no idea what resumed is. If you know hmu on discord @ Mehvix#7172
@client.event
async def on_resumed():
    print("{}: Resumed ".format(get_time()))


# When a user joins the server
@client.event
async def on_member_join(member):
    print("{0}: {1} joined".format(get_time(), member))
    await client.send_message(discord.Object(id=notification_channel), "<@{}> joined the server :tada:"
                              .format(member.id))


# When a user is banned from the server
@client.event
async def on_member_ban(member):
    global ban_message
    ban_message += 1
    print("{}: Someone was banned".format(get_time()))
    await client.send_message(discord.Object(id=notification_channel),
                              "<@{}> was **banned** :hammer:".format(member.id))
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
        print("{0}: {1} left or was kicked".format(get_time(), member))
        await client.send_message(discord.Object(id=notification_channel),
                                  "<@{}> was either kicked or left the server :frowning2:".format(member.id))
        ban_message = 0


# This is for the upvote/downvote system
@client.event
async def on_reaction_add(reaction, user):
    emoji_used = str(reaction.emoji)
    formated_up = "<{}>".format(upvote_emoji)
    formated_down = "<{}>".format(downvote_emoji)

    print("{0}: {1} reacted with {2} to {3}'s message"
          .format(get_time(), user, emoji_used, reaction.message.author))

    if reaction.message.channel.id != pokemon_channel:
        if emoji_used == formated_up:  # If emote is the upvote emote
            if reaction.message.author.id == user.id:
                print("{0}: {1} upvoted there own link. NO CHANGE"
                      .format(get_time(), user))
            else:
                user_add_karma(reaction.message.author.id, 5)
                print("{0}: ADDED 5 karma to {1} for a UPVOTE from {2}"
                      .format(get_time(), reaction.message.author, user))

        # If emote is the downvote emote
        if emoji_used == formated_down:
            if reaction.message.author.id == user.id:
                print("{0}: {1} downvoted there post. NO CHANGE"
                      .format(get_time(), user))
            else:
                user_add_karma(reaction.message.author.id, -5)
                print("{0}: REMOVED 5 karma to {1} for a DOWNVOTE from {1}"
                      .format(get_time(), reaction.message.author, user))
    else:
        print("{0}: DIDN'T change {1}'s karma because they're in the Pokemon Channel!"
              .format(get_time(), user))


# This is more stuff for the upvote/downvote system
@client.event
async def on_reaction_remove(reaction, user):
    emoji_used = str(reaction.emoji)
    formated_up = "<{}>".format(upvote_emoji)
    formated_down = "<{}>".format(downvote_emoji)

    if reaction.message.channel.id != pokemon_channel:
        if emoji_used == formated_up:
            if reaction.message.author.id == user.id:
                print("{0}: {1} REMOVED their upvote to their post. NO CHANGE".format(get_time(), user.id))
            else:
                user_add_karma(reaction.message.author.id, -5)
                print("{0}: REMOVED 5 karma from {0} because {1} REMOVED there UPVOTE"
                      .format(get_time(), reaction.message.author, user))

        # If emote is the downvote emote
        if emoji_used == formated_down:
            if reaction.message.author.id == user.id:
                print("{0}: {1} REMOVED their downvote to there own link. NO CHANGE".format(get_time(), user))
            else:
                user_add_karma(reaction.message.author.id, 5)
                print("{0}: RE-ADDED 5 karma to {1} for removal of downvote reaction from {2}"
                      .format(get_time(), reaction.message.author, user))
    else:
        print("{0}: DIDN'T change {1}'s karma because it was in the Pokemon Channel!"
              .format(get_time(), user))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    # Message author variables
    user_id = message.author.id
    user_name = message.author

    author_level = get_level(user_id)
    author_karma = get_karma(user_id)

    # Because @xpoes#9244 spams the shit out of our pokemon channel
    if message.channel.id == pokemon_channel:
        print("{0}: DIDN'T give karma to {1} for message '{2}' because they sent a message in the Pokemon channel"
              .format(get_time(), message.author, message.content))
    else:
        user_add_karma(user_id, 1)
        print("{0}: ADDED 1 karma to {1} for a message '{2}' in {3}"
              .format(get_time(), user_name, message.content, message.channel))

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
                print("{0}: {1} leveled up to {2}".format(get_time(), user_id, get_level(user_id)))
            except AttributeError:
                print("{0}: {1} leveled up to {2}, but the server doesn't have that role the level name!"
                      .format(get_time(), user_id, new_level))
        except AttributeError:
            print("{0}: {1} leveled up to {2}, but the server doesn't have that role the level name!"
                  .format(get_time(), user_id, new_level))

    if message.content.upper().startswith(".TIME"):
        print("{0}: {1} requested the time".format(get_time(), user_name))
        await client.send_message(message.channel, "I think it's `{0}:{1}:{2} {3}` {4}"
                                  .format(new_cur_hour, new_cur_min, new_cur_sec, new_am_or_pm,
                                          random.choice(clock_emoji)))

    # Upvote Code
    if "HTTP" in message.content.upper():
        try:
            await client.add_reaction(message, upvote_emoji)
        except AttributeError:
            print("{0}: User has not role! (Probably a webhook)".format(get_time()))

    # "Shut Up" code
    if shut_up_role in [role.id for role in message.author.roles]:
        print("{0}: Told {1} to shaddup".format(get_time(), user_name))
        await client.send_message(message.channel, "Shut up <@{}>".format(user_id))

    # Ping Command
    if message.content.upper().startswith(".PING"):
        print("{0}: {1} requested 'PING'".format(get_time(), user_name))
        await client.send_message(message.channel, "Pong! :ping_pong:")

    # About Command
    if message.content.upper().startswith(".ABOUT"):
        print("{0}: {1} requested '.ABOUT'".format(get_time(), user_name))
        embed = discord.Embed(title="Github", url="https://github.com/Mehvix/synapsBot", color=embed_color)
        embed.set_author(name="About:", url="https://steamcommunity.com/id/Mehvix/",
                         icon_url="https://steamcdn-a.akamaihd.net/steamcommunity/public/images/avatars/08/080527004088"
                                  "e8e461d6fc9a4df248dfd3fa2dc8_full.jpg")
        embed.set_thumbnail(url="https://goo.gl/FCddaV")
        embed.add_field(name="Creator:", value="\u200b", inline=True)
        embed.add_field(name="Mehvix#7172", value="\u200b", inline=True)
        await client.send_message(message.channel, embed=embed)

    # Help Command
    if message.content.upper().startswith(".HELP"):
        print("{0}: {1} requested '.HELP'".format(get_time(), user_name))
        embed = discord.Embed(title="Commands:", color=embed_color)
        embed.add_field(name=".help", value="This command.", inline=False)
        embed.add_field(name=".ping", value="Play Ping-Pong with the bot.", inline=False)
        embed.add_field(name=".about", value="Returns info on the bot.", inline=False)
        embed.add_field(name=".ud +word", value="Returns (word)'s definition on Urban Dictionary.", inline=False)
        embed.add_field(name=".8ball", value="Shake the 8-ball.", inline=False)
        embed.add_field(name=".uptime", value="Returns how long the bot has been online.", inline=False)
        embed.add_field(name=".karma", value="Returns your karma.", inline=False)
        embed.add_field(name=".karma @name", value="Returns (name)'s karma.", inline=False)
        embed.add_field(name=".level", value="Returns your level.", inline=False)
        embed.add_field(name=".level @name", value="Returns (name)'s level.", inline=False)
        embed.add_field(name=".sam", value="Gives you a picture of Sammy.", inline=False)
        embed.add_field(name=".bear", value="Uploads a gif of a bear.", inline=False)
        embed.add_field(name=".sam", value="Gives you a picture of Sammy.", inline=False)
        embed.add_field(name=".beta", value="Ask's Mehvix for access to beta server.", inline=False)
        embed.add_field(name=".serverinfo", value="For finding server statistics.", inline=False)
        embed.add_field(name=".version", value="Find the bot's version", inline=False)
        embed.add_field(name=".whois", value="Gets someone's account info", inline=False)
        embed.add_field(name=".createpoll", value="Self explanatory", inline=False)
        embed.add_field(name=".serverrules (admin)", value="Outputs the Server Rules.", inline=False)
        embed.add_field(name=".roulette {BET}", value="Gamble your karma.", inline=False)
        embed.add_field(name=".roulette help", value="Self-explanatory", inline=False)
        await client.send_message(message.channel, embed=embed)

    # ".Accept" code
    role = discord.utils.get(message.server.roles, name=member_role_name)
    if message.author.bot is True:
        return
    else:
        if member_role_id not in [role.id for role in message.author.roles]:
            if message.content.upper().startswith(".ACCEPT"):
                await client.add_roles(user_name, role)
                await asyncio.sleep(.1)
                await client.delete_message(message)
                await client.send_message(discord.Object(id=notification_channel),
                                          "<@{}> is now a Member :ok_hand:".format(user_id))
                print("{0}: {1} joined the server (.accept)".format(get_time(), user_name))
            else:
                await asyncio.sleep(.1)
                await client.delete_message(message)
                print("{0}: DIDN'T type '.accept'".format(get_time(), user_name))

    # Verified Code
    if verified_role_id in [role.id for role in message.author.roles]:
        # UD Code
        if message.content.upper().startswith(".UD"):
            target_def = message.content[4:]
            target_def_link_format = target_def.replace(" ", "%20")

            if "MAGGIE" in message.content.upper():
                print("{0}: {1}  requested the UD for Maggie".format(get_time(), user_name))
                embed = discord.Embed(title="Definition Page", url="https://goo.gl/j2DX9N", color=embed_color)
                embed.set_author(name="Definition for Maggie", url="https://goo.gl/j2DX9N")
                embed.set_footer(text="Girl with YUUUG milkers. Doesnt need a coat")
                await client.send_message(message.channel, embed=embed)
            else:
                try:
                    term = udtop(target_def)
                    print("{0}: {1} requested the UD for {2}".format(get_time(), user_name, target_def))
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
            print("{0}: {1} requested '.8BALL'".format(get_time(), user_name))

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
            print("{0}: {1} requested '.VERSION'".format(get_time(), user_name))
            await client.send_message(message.channel, "The bot is currently running version `{}`"
                                      .format(file_name[10:-3]))

        # Uptime Code
        if message.content.upper().startswith(".UPTIME"):
            print("{0}: {1} requested '.UPTIME'".format(get_time(), user_name))
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
            level_target = message.content[7:]
            if level_target == "":
                user_level_req = user_id
            else:
                if not message.raw_mentions:
                    await client.send_message(message.channel, "You need to `@` a user")
                    return
                else:
                    user_level_req = str(message.raw_mentions)[2:-2]
            print("{0}: {1} requested {2}'s level".format(get_time(), user_name, user_level_req))
            await client.send_message(message.channel, "<@{0}> is level `{1}`"
                                      .format(user_level_req, get_level(user_level_req)))

        # Gets random bear picture
        if message.content.upper().startswith(".BEAR"):
            print("{0}: {1} sent a bear".format(get_time(), user_name))
            fp = random.choice(os.listdir("bears"))
            await client.send_file(message.channel, "bears/{}".format(fp))

        # Gets random Sam picture
        if message.content.upper().startswith(".SAM"):
            print("{0}: {1} sent a sam".format(get_time(), user_name))
            fp = random.choice(os.listdir("sams"))
            await client.send_file(message.channel, "sams/{}".format(fp))

        # Server Info
        if message.content.upper().startswith(".SERVERINFO"):
            print("{0}: {1} requested '.SERVER'".format(get_time(), user_name))
            online = 0
            for i in message.server.members:
                if str(i.status) == "online" or str(i.status) == "idle" or str(i.status) == "dnd":
                    online += 1

            role_count = len(message.server.roles)
            emoji_count = len(message.server.emojis)
            server_created_time = message.server.created_at

            print("{0}: {1} activated the SERVER command".format(user_name, get_time()))
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
            print("{0}: {1} activated the BETA command".format(user_name, get_time()))
            user = await client.get_user_info(user_id)
            await client.send_message(message.channel, "Hey <@!196355904503939073>, <@{}> wants beta access. "
                                                       "Type `.allow` to send them an invite".format(user_id))
            msg = await client.wait_for_message(content=".allow")
            if msg is None:
                await client.send_message(message.channel, "<@!196355904503939073> DIDN'T respond in time :(. "
                                                           "Please try another time.")
            else:
                if msg.author.id == "196355904503939073":
                    testinvite = get_json('./test_server.json')
                    invite = testinvite.get("invite")
                    await client.send_message(user, "You've been accepted! {}".format(invite))
                    await client.send_message(message.channel,
                                              "<@{}> was accepted into the beta testing server! :tada:"
                                              .format(user_id))
                    # await client.send_message(message.channel, "https://discord.gg/wjPwUJx")
                else:
                    await client.send_message(message.channel, "You can't do that!")

        # Karma System
        if message.content.upper().startswith(".KARMA"):
            karma_target = message.content[7:]
            if karma_target == "":
                user_req = user_id
            else:
                if not message.raw_mentions:
                    await client.send_message(message.channel, "You need to `@` a user")
                    return
                else:
                    user_req = str(message.raw_mentions)[2:-2]
                    # user_req = message.content[10:-1]
            print("{0}: {1} requested {2}'s level".format(get_time(), user_name, user_req))
            await client.send_message(
                message.channel, "<@{0}> has `{1}` karma".format(user_req, get_karma(user_req)))

        # Poll System
        if message.content.upper().startswith(".CREATEPOLL"):
            global vote_phase
            if vote_phase != 1:
                vote_phase += 1
                print("{0}: {1} created a poll".format(get_time(), user_name))
                await asyncio.sleep(.1)
                await client.delete_message(message)

                title_embed = discord.Embed(title="\u200b", color=embed_color)
                title_embed.set_author(name="Generating a poll for {0} {1}".format(user_name,
                                                                                   random.choice(clock_emoji)))
                title_embed.add_field(name="\u200b", value="\u200b", inline=False)
                title_embed.add_field(name="Question", value="What would you like the title to be?",
                                      inline=False)
                title_message = await client.send_message(message.channel, embed=title_embed)

                # Title
                title = await client.wait_for_message(
                    timeout=120, author=message.author, channel=message.channel)

                try:
                    poll_title = title.content
                    print("{0}: Set title to {1}".format(get_time(), poll_title))
                    await asyncio.sleep(.1)
                    await client.delete_message(title)
                except AttributeError:
                    await client.send_message(
                        message.channel, "<@{}> DIDN'T respond fast enough, so the poll was cancelled".format(
                            message.author.id))
                    return

                options_embed = discord.Embed(title="\u200b", color=embed_color)
                options_embed.set_author(name="Generating a poll for {0} {1}"
                                         .format(user_name, random.choice(clock_emoji)))
                options_embed.add_field(name="Title:", value=str(poll_title), inline=False)
                options_embed.add_field(name="\u200b", value="\u200b", inline=False)
                options_embed.add_field(
                    name="Question", value="How many options do you want their to be? (No more than 6)",
                    inline=False)
                await asyncio.sleep(.1)
                await client.delete_message(title_message)
                options_message = await client.send_message(message.channel, embed=options_embed)

                # Number of Options
                options = await client.wait_for_message(
                    timeout=120, author=message.author, channel=message.channel)

                try:
                    poll_options = int(options.content)
                    print("{0}: Number of options set to {1}".format(get_time(), poll_options))
                    await asyncio.sleep(.1)
                    await client.delete_message(options)
                except ValueError:
                    await client.send_message(
                        message.channel, "You can only use **whole** numbers, no decimals!")
                    return
                except AttributeError:
                    await client.send_message(
                        message.channel, "<@{}> DIDN'T respond fast enough, so the poll was cancelled".format(
                            message.author.id))
                    return

                # Option debugging
                if poll_options <= 1:
                    await client.send_message(message.channel, "Sorry, You can't have 1 option")
                    return
                if poll_options > 6:
                    await client.send_message(message.channel, "Sorry, You can't have more than 6 options!")
                    return

                one_embed = discord.Embed(title="\u200b", color=embed_color)
                one_embed.set_author(name="Generating a poll for {0} {1}"
                                     .format(user_name, random.choice(clock_emoji)))
                one_embed.add_field(name="Title:", value=str(poll_title), inline=False)
                one_embed.add_field(name="Number of Options:", value=str(poll_options), inline=False)
                one_embed.add_field(name="\u200b", value="\u200b", inline=False)
                one_embed.add_field(
                    name="Question", value="What should option one be called?",
                    inline=False)
                await asyncio.sleep(.1)
                await client.delete_message(options_message)
                one_message = await client.send_message(message.channel, embed=one_embed)

                # Gets Option 1
                option_1 = await client.wait_for_message(timeout=120, author=message.author,
                                                         channel=message.channel)
                try:
                    poll_option_1 = option_1.content
                    print("{0}: Option 1 set to {1}".format(get_time(), poll_option_1))
                    await asyncio.sleep(.1)
                    await client.delete_message(option_1)
                    # await client.delete_message(bot_opt1)

                except AttributeError:
                    await client.send_message(
                        message.channel,
                        "<@{}> DIDN'T respond fast enough, so the poll was cancelled".format(
                            message.author.id))
                    return

                two_embed = discord.Embed(title="\u200b", color=embed_color)
                two_embed.set_author(name="Generating a poll for {0} {1}".format(user_name,
                                                                                 random.choice(
                                                                                     clock_emoji)))
                two_embed.add_field(name="Title:", value=str(poll_title), inline=False)
                two_embed.add_field(name="Number of Options:", value=str(poll_options), inline=False)
                two_embed.add_field(name="Option 1:", value=str(poll_option_1), inline=True)
                two_embed.add_field(name="\u200b", value="\u200b", inline=False)
                two_embed.add_field(
                    name="Question", value="What should option two be called?",
                    inline=False)
                await asyncio.sleep(.1)
                await client.delete_message(one_message)
                two_message = await client.send_message(message.channel, embed=two_embed)

                # Gets Option 2
                option_2 = await client.wait_for_message(
                    timeout=120, author=message.author, channel=message.channel)

                try:
                    poll_option_2 = option_2.content
                    print("{0}: Option 2 set to {1}".format(get_time(), poll_option_2))
                    await asyncio.sleep(.1)
                    await client.delete_message(option_2)

                except AttributeError:
                    await client.send_message(
                        message.channel,
                        "<@{}> DIDN'T respond fast enough, so the poll was cancelled".format(
                            message.author.id))
                    return

                if poll_options >= 3:

                    three_embed = discord.Embed(title="\u200b", color=embed_color)
                    three_embed.set_author(
                        name="Generating a poll for {0} {1}".format(user_name, random.choice(clock_emoji)))
                    three_embed.add_field(name="Title:", value=str(poll_title), inline=False)
                    three_embed.add_field(name="Number of Options:", value=str(poll_options), inline=False)
                    three_embed.add_field(name="Option 1:", value=str(poll_option_1), inline=True)
                    three_embed.add_field(name="Option 2:", value=str(poll_option_2), inline=True)
                    three_embed.add_field(name="\u200b", value="\u200b", inline=False)
                    three_embed.add_field(
                        name="Question", value="What should option three be called?",
                        inline=False)
                    await asyncio.sleep(.1)
                    await client.delete_message(two_message)
                    three_message = await client.send_message(message.channel, embed=three_embed)

                    # Option 3
                    option_3 = await client.wait_for_message(
                        timeout=120, author=message.author, channel=message.channel)

                    try:
                        poll_option_3 = option_3.content
                        print("{0}: Option 3 set to {1}".format(get_time(), poll_option_3))
                        await asyncio.sleep(.1)
                        await client.delete_message(option_3)

                    except AttributeError:
                        await client.send_message(
                            message.channel,
                            "<@{}> DIDN'T respond fast enough, so the poll was cancelled".format(
                                message.author.id))
                        return

                    if poll_options >= 4:
                        four_embed = discord.Embed(title="\u200b", color=embed_color)
                        four_embed.set_author(
                            name="Generating a poll for {0} {1}".format(user_name, random.choice(clock_emoji)))
                        four_embed.add_field(name="Title:", value=str(poll_title), inline=False)
                        four_embed.add_field(name="Number of Options:", value=str(poll_options), inline=False)
                        four_embed.add_field(name="Option 1:", value=str(poll_option_1), inline=True)
                        four_embed.add_field(name="Option 2:", value=str(poll_option_2), inline=True)
                        four_embed.add_field(name="Option 3:", value=str(poll_option_3), inline=True)
                        four_embed.add_field(name="\u200b", value="\u200b", inline=False)
                        four_embed.add_field(
                            name="Question", value="What should option four be called?",
                            inline=False)
                        await asyncio.sleep(.1)
                        await client.delete_message(three_message)
                        four_message = await client.send_message(message.channel, embed=four_embed)

                        # Option 4
                        option_4 = await client.wait_for_message(timeout=120, author=message.author,
                                                                 channel=message.channel)

                        try:
                            poll_option_4 = option_4.content
                            print("{0}: Option 4 set to {1}".format(get_time(), poll_option_4))
                            await asyncio.sleep(.1)
                            await client.delete_message(option_4)

                        except AttributeError:
                            await client.send_message(
                                message.channel,
                                "<@{}> DIDN'T respond fast enough, so the poll was cancelled".format(
                                    message.author.id))
                            return

                        if poll_options >= 5:
                            five_embed = discord.Embed(title="\u200b", color=embed_color)
                            five_embed.set_author(
                                name="Generating a poll for {0} {1}".format(user_name,
                                                                            random.choice(clock_emoji)))
                            five_embed.add_field(name="Title:", value=str(poll_title), inline=False)
                            five_embed.add_field(name="Number of Options:", value=str(poll_options),
                                                 inline=False)
                            five_embed.add_field(name="Option 1:", value=str(poll_option_1), inline=True)
                            five_embed.add_field(name="Option 2:", value=str(poll_option_2), inline=True)
                            five_embed.add_field(name="Option 3:", value=str(poll_option_3), inline=True)
                            five_embed.add_field(name="Option 4:", value=str(poll_option_4), inline=True)
                            five_embed.add_field(name="\u200b", value="\u200b", inline=False)
                            five_embed.add_field(
                                name="Question", value="What should option five be called?",
                                inline=False)
                            await asyncio.sleep(.1)
                            await client.delete_message(four_message)
                            five_message = await client.send_message(message.channel, embed=five_embed)

                            # Option 5
                            option_5 = await client.wait_for_message(
                                timeout=120, author=message.author, channel=message.channel)

                            try:
                                poll_option_5 = option_5.content
                                print("{0}: Option 5 set to {1}".format(get_time(), poll_option_5))
                                await asyncio.sleep(.1)
                                await client.delete_message(option_5)

                            except AttributeError:
                                await client.send_message(
                                    message.channel,
                                    "<@{}> DIDN'T respond fast enough, so the poll was cancelled".format(
                                        message.author.id))
                                return

                            if poll_options == 6:
                                six_embed = discord.Embed(title="\u200b", color=embed_color)
                                six_embed.set_author(
                                    name="Generating a poll for {0} {1}".format(user_name,
                                                                                random.choice(clock_emoji)))
                                six_embed.add_field(name="Title:", value=str(poll_title), inline=False)
                                six_embed.add_field(name="Number of Options:", value=str(poll_options),
                                                    inline=False)
                                six_embed.add_field(name="Option 1:", value=str(poll_option_1), inline=True)
                                six_embed.add_field(name="Option 2:", value=str(poll_option_2), inline=True)
                                six_embed.add_field(name="Option 3:", value=str(poll_option_3), inline=True)
                                six_embed.add_field(name="Option 4:", value=str(poll_option_4), inline=True)
                                six_embed.add_field(name="Option 5:", value=str(poll_option_5), inline=True)
                                six_embed.add_field(name="\u200b", value="\u200b", inline=True)
                                six_embed.add_field(
                                    name="Question", value="What should option six be called?",
                                    inline=False)
                                await asyncio.sleep(.1)
                                await client.delete_message(five_message)
                                six_message = await client.send_message(message.channel, embed=six_embed)

                                # Option 6
                                option_6 = await client.wait_for_message(
                                    timeout=120, author=message.author, channel=message.channel)

                                try:
                                    poll_option_6 = option_6.content
                                    print("{0}: Option 6 set to {1}".format(get_time(), poll_option_6))
                                    await asyncio.sleep(.1)
                                    await client.delete_message(option_6)
                                    await asyncio.sleep(.1)
                                    await client.delete_message(six_message)

                                except AttributeError:
                                    await client.send_message(
                                        message.channel,
                                        "<@{}> DIDN'T respond fast enough, so the poll was cancelled".format
                                        (message.author.id))
                                    return
                        else:
                            await asyncio.sleep(.1)
                            await client.delete_message(four_message)
                    else:
                        await asyncio.sleep(.1)
                        await client.delete_message(three_message)
                else:
                    await asyncio.sleep(.1)
                    await client.delete_message(two_message)

                embed = discord.Embed(
                    title=string.capwords(poll_title),
                    description="Created by {}".format(user_name), color=embed_color)
                embed.set_thumbnail(
                    url="https://png.icons8.com/metro/1600/poll-topic.png")
                embed.add_field(
                    name="Option 1:", value=string.capwords(poll_option_1), inline=True)
                embed.add_field(
                    name="Option 2:", value=string.capwords(poll_option_2), inline=True)
                if poll_options >= 3:
                    embed.add_field(
                        name="Option 3:", value=string.capwords(poll_option_3), inline=True)
                    if poll_options >= 4:
                        embed.add_field(
                            name="Option 4:", value=string.capwords(poll_option_4), inline=True)
                        if poll_options >= 5:
                            embed.add_field(
                                name="Option 5:", value=string.capwords(poll_option_5), inline=True)
                            if poll_options == 6:
                                embed.add_field(
                                    name="Option 6:", value=string.capwords(poll_option_6),
                                    inline=True)
                poll_message = await client.send_message(message.channel, embed=embed)

                await client.add_reaction(poll_message, one_emote)
                await asyncio.sleep(.1)
                await client.add_reaction(poll_message, two_emote)
                if poll_options >= 3:
                    await asyncio.sleep(.1)
                    await client.add_reaction(poll_message, three_emote)
                    if poll_options >= 4:
                        await asyncio.sleep(.1)
                        await client.add_reaction(poll_message, four_emote)
                        if poll_options >= 5:
                            await asyncio.sleep(.1)
                            await client.add_reaction(poll_message, five_emote)
                            if poll_options == 6:
                                await asyncio.sleep(.1)
                                await client.add_reaction(poll_message, six_emote)
                vote_phase -= 1
            else:
                await client.send_message(message.channel, "Sorry, another vote is taking place right now!")

        # Who-is command
        # Assistance from https://gist.github.com/Grewoss/c0601832982a99f59cc73510f7841fe4
        if message.content.upper().startswith(".WHOIS"):
            print("{0}: {1} requested '.WHOIS'".format(get_time(), user_name))
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
                    print("{0}: {1} requested '.WHOIS' but they DIDN'T exist".format(get_time(), user_name))
                    await client.send_message(message.channel, "Sorry, but I couldn't find that user")
                finally:
                    pass

        # TODO Make betting separate and return the user's karma to bet
        # Roulette system
        if message.content.upper().startswith(".ROULETTE"):
            if message.content.upper().startswith(".ROULETTE HELP"):
                embed = discord.Embed(title="Outcomes:", color=embed_color)
                embed.set_author(name="Roulette Help")
                embed.set_thumbnail(url="https://d30y9cdsu7xlg0.cloudfront.net/png/90386-200.png")
                embed.add_field(name="Zero:", value="0", inline=True)
                embed.add_field(name="Even:",
                                value="2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36",
                                inline=True)
                embed.add_field(name="Odd:",
                                value="1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35",
                                inline=True)
                embed.add_field(name="How to Play:",
                                value="Type .roulette [BET AMOUNT]",
                                inline=True)
                embed.set_footer(text="Maximum bet is 250 karma. Winning on zero will quattuordecuple (x14) your bet"
                                      " while odd and even will double your bet")
                await client.send_message(message.channel, embed=embed)
            else:
                message_split = message.content.split(" ")

                try:
                    bet_amount = int(message_split[1])
                except ValueError:
                    await client.send_message(message.channel, "Sorry, you need to bet a number between `10` and `250`")
                    return
                except IndexError:
                    await client.send_message(message.channel, "Sorry, you need to bet a number between `10` and `250`")
                    return

                if 9 < bet_amount < 251:
                    if bet_amount > author_karma:
                        await client.send_message(message.channel, "You don't have enough karma!")
                        return
                    outcomes = ["zero", "even", "odd"]
                    await client.send_message(message.channel, "What outcome would you like to bet on? The options are"
                                                               " `zero`, `even`, or `odd`")
                    outcomes_response = await client.wait_for_message(
                        timeout=120, author=message.author, channel=message.channel)

                    try:
                        outcomes_formatted = outcomes_response.content
                        print("{0}: Outcome set to {1}".format(get_time(), outcomes_formatted))
                    except AttributeError:
                        await client.send_message(
                            message.channel,
                            "<@{}> DIDN'T respond fast enough, so the roulette was canceled".format(
                                message.author.id))
                        return

                    if outcomes_formatted in outcomes:
                        user_add_karma(user_id, -int(bet_amount))
                        rolling_message = await client.send_message(message.channel, "Spinning")
                        await asyncio.sleep(.25)
                        await client.edit_message(rolling_message, "Spinning.")
                        await asyncio.sleep(.25)
                        await client.edit_message(rolling_message, "Spinning..")
                        await asyncio.sleep(.25)
                        await client.edit_message(rolling_message, "Spinning...")

                        spin = random.randint(0, 36)
                        await client.send_message(message.channel, "It landed on `#{}`!".format(spin))

                        if spin == 0:
                            if outcomes_formatted == "zero":
                                user_add_karma(user_id, int(bet_amount*14))
                                await client.send_message(message.channel, "ZERO")
                                return

                        else:
                            if spin % 2 == 0:
                                if outcomes_formatted == "even":
                                    await client.send_message(message.channel,
                                                              "Winner! :tada: You doubled up on chips!")
                                    user_add_karma(user_id, int(bet_amount * 2))
                                else:
                                    await client.send_message(message.channel, "Sorry, better luck next time!")
                            else:
                                if outcomes_formatted == "odd":
                                    await client.send_message(message.channel,
                                                              "Winner! :tada: You doubled up on chips!")
                                    user_add_karma(user_id, int(bet_amount * 2))
                                else:
                                    await client.send_message(message.channel, "Sorry, better luck next time!")

                    else:
                        await client.send_message(
                            message.channel, "`ERROR:` You needed to enter `zero`, `even`, or `odd`")

                else:
                    await client.send_message(message.channel,
                                              "Sorry, you need to bet a number between `10` and `250`")
                    return

    if admin_role_id in [role.id for role in message.author.roles]:
        if message.content.upper().startswith(".SERVERRULES"):
            print("{0}: {1} requested '.SEVERRULES'".format(get_time(), user_name))
            await asyncio.sleep(.1)
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

        # TODO Mute Command
        role = discord.utils.get(message.server.roles, name=mute_role_name)
        if message.content.upper().startswith(".MUTE"):
            mute_target = str(message.raw_mentions)[2:-2]
            print("{0}: {1} muted {2}".format(get_time(), user_name, mute_target))
            await client.add_roles(self.get_user_info(mute_target), role)

        if message.content.upper().startswith(".BAN"):
            ban_target = message.content[7:-1]
            server = message.server
            print("{0}: {1} banned {2}".format(get_time(), user_name, ban_target))
            if not message.raw_mentions:
                await client.send_message(message.channel, "You need to `@` a user")
            else:
                print("{0}: {1} banned {2}".format(get_time(), user_name, ban_target))
                await client.ban(member=server.get_member(ban_target), delete_message_days=0)

        if message.content.upper().startswith(".KICK"):
            kick_target = message.content[8:-1]
            server = message.server
            print("{0}: {1} kicked {2}".format(get_time(), user_name, kick_target))
            if not message.raw_mentions:
                await client.send_message(message.channel, "You need to `@` a user")
            else:
                print("{0}: {1} kicked {2}".format(get_time(), user_name, kick_target))
                await client.kick(member=server.get_member(kick_target))

        if message.content.upper().startswith(".UNBAN"):
            # unban_target = message.content[9:-1]
            # server = message.server
            await client.send_message(message.channel, "Sorry, this command is coming soon.")
            # print("{0}: {1} unbanned {2}".format(get_time(), user_name, unban_target))
            # if not message.raw_mentions:
            #     await client.send_message(message.channel, "You need to `@` a user")
            # else:
            #     print("{0}: {1} unbanned {2}".format(get_time(), user_name, unban_target))
            #     await client.unban(member=server.get_member(unban_target))

    if message.content.startswith("This is an automated message to spawn Pokémon."):
        print("{0}: {1} sent the pokemon spam message".format(get_time(), user_name))
        await asyncio.sleep(.1)
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

            file_name = os.path.basename(sys.argv[0])  # Gets file name
            r = random.randint(1, 3)
            if r == 1:
                await client.change_presence(game=discord.Game(name="Live for {0}:{1}:00".format(hours, minutes),
                                                               url="https://twitch.tv/mehvix", type=1))
            if r == 2:
                await client.change_presence(game=discord.Game(name="Version {}".format(file_name[10:-3]),
                                                               url="https://twitch.tv/mehvix", type=1))
            if r == 3:
                await client.change_presence(
                    game=discord.Game(name="Created by Mehvix#7172", url="https://twitch.tv/mehvix",
                                      type=1))
        elif hours == 24:
            hours = 0
            days += 1


def user_add_karma(user_id: int, karma: int):
    if os.path.isfile("C:/Users/maxla/PycharmProjects/synapsBot remastered/users.json"):
        try:
            with open('C:/Users/maxla/PycharmProjects/synapsBot remastered/users.json', 'r') as fp:
                users = json.load(fp)
            users[user_id]['karma'] += karma
            with open('C:/Users/maxla/PycharmProjects/synapsBot remastered/users.json', 'w') as fp:
                json.dump(users, fp, sort_keys=True, indent=4)
        except KeyError:
            with open('C:/Users/maxla/PycharmProjects/synapsBot remastered/users.json', 'r') as fp:
                users = json.load(fp)
            users[user_id] = {}
            users[user_id]['karma'] = karma
            with open('C:/Users/maxla/PycharmProjects/synapsBot remastered/users.json', 'w') as fp:
                json.dump(users, fp, sort_keys=True, indent=4)
    else:
        users = {user_id: {}}
        users[user_id]['karma'] = karma
        with open('C:/Users/maxla/PycharmProjects/synapsBot remastered/users.json', 'w') as fp:
            json.dump(users, fp, sort_keys=True, indent=4)


def get_karma(user_id: int):
    if os.path.isfile('C:/Users/maxla/PycharmProjects/synapsBot remastered/users.json'):
        with open('C:/Users/maxla/PycharmProjects/synapsBot remastered/users.json', 'r') as fp:
            users = json.load(fp)
        return users[user_id]['karma']
    else:
        return 0


def set_level(user_id: int, level: int):
    if os.path.isfile('C:/Users/maxla/PycharmProjects/synapsBot remastered/users.json'):
        with open('C:/Users/maxla/PycharmProjects/synapsBot remastered/users.json', 'r') as fp:
            users = json.load(fp)
        users[user_id]["level"] = level
        with open('C:/Users/maxla/PycharmProjects/synapsBot remastered/users.json', 'w') as fp:
            json.dump(users, fp, sort_keys=True, indent=4)


def get_level(user_id: int):
    if os.path.isfile('C:/Users/maxla/PycharmProjects/synapsBot remastered/users.json'):
        try:
            with open('C:/Users/maxla/PycharmProjects/synapsBot remastered/users.json', 'r') as fp:
                users = json.load(fp)
            return users[user_id]['level']
        except KeyError:
            return 0


client.loop.create_task(uptime())

client.run(token)
