import discord
from discord.ext.commands import Bot
from discord.ext import commands
import random
from urbandictionary_top import udtop
import json
import asyncio
import os
import sys
import datetime
import requests
import io
import string
import async

description = "synapsBot - A person Discord bot by Mehvix#7172"
Client = discord.Client()
client = commands.Bot(command_prefix=".")

# Resets uptime settings
seconds = 0
minutes = 0
hours = 0
days = 0

# Decides if startup is during AM or PM ours (yea damn 'murica time)
if datetime.datetime.now().hour > 12:
    cur_hour = datetime.datetime.now().hour - 12
    am_or_pm = "PM"
else:
    cur_hour = datetime.datetime.now().hour
    am_or_pm = "AM"
cur_min = datetime.datetime.now().minute
cur_sec = datetime.datetime.now().second

# Selects random clock emoji for '.uptime' command
clock_emoji = ["🕑", "🕗", "🕛", "🕕", "🕒", "🕘", "🕙", "🕐", "🕖", "🕓", "🕔", "🕚", "🕟", "🕠", "🕦", "🕝", "🕣"]
random.choice(clock_emoji)

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# TODO New Commands
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
#  Request Role (verified / game)                                                                                   #
#  Mute user                                                                                                        #
#  Cool down                                                                                                        #
#  Hearthstone cards (import hearthstone)                                                                           #
#  elif message.content.upper() == ".delete (messages)":                                                            #
#  elif message.content.upper().startswith(".vote"):                                                                #
#  Role Info                                                                                                        #
#  Create invite                                                                                                    #
#  User in voice channel                                                                                            #
#  Invite info                                                                                                      #
#  Server invites / request (send owner of server DM and option to accept/decline user to server)                   #
#  Give XP for voice channel usage                                                                                  #
#  Remind me (x) x == time                                                                                          #
#  Add time values to prints                                                                                        #
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# How to get custom values
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
You need the following values. They are custom for every server. You can get them by typing in any text channel the 
desired value with a "\" in front of it. I.E. "\@Member" or "\:upvote:"
For your token go to https://discordapp.com/developers/applications/me, creating a new app, and getting the token by 
clicking "reveal".
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


# Custom values for my main server and my testing server.
server = "synaps"
if server == "bot":
    token = "NDE0Njc3ODYzMjU0NDU4Mzcw.DXJDCw.CX4bzf2CdhuoYB2Mh2WKKh6TP0Y"  # Bot Test
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

    # Number Emojis (because unicode is hard)
    one_emote = ":onev2:442817606961987585"
    two_emote = ":twov2:442817607020838913"
    three_emote = ":threev2:442817607301726208"
    four_emote = ":fourv2:442817606957924383"
    five_emote = ":fivev2:442817607188348938"
    six_emote = ":sixv2:442817607196868629"
else:
    token = "NDE0Njc0MjU1NDAyMjM3OTY0.DWq2aQ.5z4rz6QRjdZ8QuEodYZ1GaCCLOY"  # TS
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

    # Number Emojis (because unicode is hard)
    one_emote = ":one2:442836971161649152"
    two_emote = ":two2:442836971145134080"
    three_emote = ":three2:442836970935156738"
    four_emote = ":four2:442836971145003025"
    five_emote = ":five2:442836971153522688"
    six_emote = ":six2:442836970843013131"


"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


@client.event
async def on_ready():
    users = len(set(client.get_all_members()))
    channels = len([c for c in client.get_all_channels()])
    file_name = os.path.basename(sys.argv[0])  # Gets file name

    # Sets the setting
    await client.change_presence(game=discord.Game(name="Version {}".format(file_name[10:-3]),
                                                   url="https://twitch.tv/mehvix", type=1))
    servers = list(client.servers)

    print("============================================================")
    print("• Version:                   {}".format(discord.__version__))
    print("• Start Time:                {0}:{1}:{2} {3}".format(cur_hour, cur_min, cur_sec, am_or_pm))
    print("• Client Name:               {}".format(client.user))
    print("• Client ID:                 {}\n".format(client.user.id))
    print("• Channels:                  {}".format(channels))
    print("• Users:                     {}".format(users))
    print("• Connected to " + str(len(client.servers)) + " server(s):\n")
    for x in range(len(servers)):
        print("> " + servers[x - 1].name)
    print("============================================================")


@client.event
async def on_resumed():
    print("Resumed.")


@client.event
async def on_member_join(member):
    client.send_message(discord.Object(id=notification_channel), "<@{}> joined the server :tada:".format(member.id))


@client.event
async def on_member_remove(member):
    client.send_message(discord.Object(id=notification_channel), "<@{}> was either kicked or left the server :frowning"
                                                                 "2:".format(member.id))


@client.event
async def on_reaction_add(reaction, user):
    emoji_used = str(reaction.emoji)
    formted_up = "<{}>".format(upvote_emoji)
    formted_down = "<{}>".format(downvote_emoji)

    print("{0} reacted with {1} to {2}'s message".format(user, emoji_used, reaction.message.author))

    if reaction.message.channel.id != pokemon_channel:
        # If emote is the upvote emote
        if emoji_used == formted_up:
            if reaction.message.author.id == user.id:
                print("{0} ({1}) upvoted there post. NO CHANGE".format(user, user.id))
            else:
                user_add_karma(reaction.message.author.id, 5)
                print("GAVE 5 karma to {0} ({2}) for a reaction from {1} ({3})".format(reaction.message.author, user,
                                                                                       reaction.message.author.id, user.id))

        # If emote is the downvote emote
        if emoji_used == formted_down:
            if reaction.message.author.id == user.id:
                print("{0} ({1}) downvoted there post. NO CHANGE".format(user, user.id))
            else:
                user_add_karma(reaction.message.author.id, 5)
                print("REMOVED 5 karma to {0} ({2}) for a reaction from {1} ({3})".format(reaction.message.author, user,
                                                                                          reaction.message.author.id,
                                                                                          user.id))
    else:
        print("Didn't give {} karma because they sent it in the Pokemon Channel!".format(reaction.message.author))


@client.event
async def on_reaction_remove(reaction, user):
    emoji_used = str(reaction.emoji)
    formted_up = "<{}>".format(upvote_emoji)
    formted_down = "<{}>".format(downvote_emoji)

    if reaction.message.channel.id != pokemon_channel:
        if emoji_used == formted_up:
            if reaction.message.channel == notification_channel:
                if reaction.message.author.id == user.id:
                    print("{0} ({1}) removed their upvote to there post. NO CHANGE".format(user, user.id))
                else:
                    user_add_karma(reaction.message.author.id, -5)
                    print("REMOVED 5 karma to {0} ({2}) for a reaction from {1} ({3})".format(reaction.message.author, user,
                                                                                              reaction.message.author.id,
                                                                                              user.id))
            else:
                print("{} tried getting upvote karma in a non-message channel".format(reaction.message.author))

        # If emote is the downvote emote
        if emoji_used == formted_down:
            if reaction.message.author.id == user.id:
                print("{0} ({1}) removed their downvote to there post. NO CHANGE".format(user, user.id))
            else:
                user_add_karma(reaction.message.author.id, 5)
                print("GAVE 5 karma to {0} ({2}) for removal of downvote reaction from {1} ({3})"
                      .format(reaction.message.author, user, reaction.message.author.id, user.id))
    else:
        print("Didn't give {} karma because they sent it in the Pokemon Channel!".format(reaction.message.author))


@client.event
async def on_message(message):

    user_id = message.author.id
    user_name = message.author

    if message.channel.id == pokemon_channel:
        print("DIDN'T given karma to {0} because they sent a message in the Pokemon channel".format(message.author))
    else:
        user_add_karma(user_id, 1)
        print("GAVE 1 karma to {0} ({1}) for a message in {2}".format(user_name, user_id, message.channel.id))

    author_level = get_level(message.author.id)
    author_karma = get_karma(user_id)

    # Checks Karma / Level
    new_level = author_level + 1
    if author_karma >= 100 * new_level:
        role_name = "Level {}".format(new_level)
        level_role = discord.utils.get(message.server.roles, name=role_name)
        set_level(user_id, new_level)
        await client.add_roles(message.author, level_role)
        await client.send_message(message.channel, "Congrats, <@{0}>! You're now level `{1}`.  :tada: ".format(
            user_id, new_level))

    # Upvote Code
    if "HTTP" in message.content.upper():
        try:
            await client.add_reaction(message, upvote_emoji)
        except AttributeError:
            print("User has not role!")

    # "Shut Up" code
    if shut_up_role in [role.id for role in message.author.roles]:
        await client.send_message(message.channel, "Shut up <@{}>".format(user_id))

    if "EAT MY ASS" in message.content.upper():
        await client.send_message(message.channel, "*With pleasure 😋*")

    # Ping Command
    if message.content.upper().startswith(".PING"):
        await client.send_message(message.channel, "Pong! :ping_pong:")

    # About Command
    if message.content.upper().startswith(".ABOUT"):
        embed = discord.Embed(title="Github", url="https://github.com/Mehvix/synaps-bot", color=0x1abc9c)
        embed.set_author(name="About:", url="https://steamcommunity.com/id/Mehvix/",
                         icon_url="https://steamcdn-a.akamaihd.net/steamcommunity/public/images/avatars/08/080527004088"
                                  "e8e461d6fc9a4df248dfd3fa2dc8_full.jpg")
        embed.set_thumbnail(url="https://goo.gl/FCddaV")
        embed.add_field(name="Creator:", value="\u200b", inline=True)
        embed.add_field(name="Mehvix#7172", value="\u200b", inline=True)
        await client.send_message(message.channel, embed=embed)

    # Help Command
    if message.content.upper().startswith(".HELP"):
        embed = discord.Embed(title="Commands:", color=0x1abc9c)
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

    # ".Accept" code
    role = discord.utils.get(message.server.roles, name=member_role_name)
    if member_role_id not in [role.id for role in message.author.roles]:
        if message.content.upper().startswith(".ACCEPT"):
            await client.add_roles(user_name, role)
            await client.delete_message(message)
            await client.send_message(discord.Object(id=notification_channel),
                                      "<@{}> is now a Member :ok_hand:".format(user_id))
        else:
            await client.delete_message(message)

    # Verified Code
    words = [".UD", ".8BALL", ".UPTIME", ".LEVEL", ".BEAR", ".KARMA", ".CREATEPOLL", ".SAM", ".BETA", ".SERVER"]
    for word in words:
        if message.content.upper().startswith(word):
            if verified_role_id in [role.id for role in message.author.roles]:
                print("{} activated a verified command".format(user_name))
                # UD Code
                if message.content.upper().startswith(".UD"):
                    print("UD Requested!")
                    if "MAGGIE" in message.content.upper():
                        print("{0}  requested the UD for Maggie".format(user_name))
                        embed = discord.Embed(title="Definition Page", url="https://goo.gl/j2DX9N", color=0x1abc9c)
                        embed.set_author(name="Definition for Maggie", url="https://goo.gl/j2DX9N")
                        embed.set_footer(text="Girl with YUUUG milkers. Doesnt need a coat")
                        await client.send_message(message.channel, embed=embed)
                    else:
                        try:
                            target_def = message.content[4:]
                            term = udtop(target_def)
                            print("{0}  requested the UD for {1}".format(user_name, target_def))
                            embed = discord.Embed(title="Definition Page",
                                                  url="https://www.urbandictionary.com/define.php?term={}"
                                                  .format(target_def.replace(" ", "%20")), color=0x1abc9c)
                            embed.set_author(name="Definition for " + target_def,
                                             url="https://www.urbandictionary.com/define.php?term={}"
                                             .format(target_def))
                            embed.set_footer(text=term)
                            await client.send_message(message.channel, embed=embed)
                        except AttributeError:
                            await client.send_message(message.channel, "Sorry, that word doesnt have a definition :( . "
                                                                       "You can add your own here: ")
                            await client.send_message(message.channel, "https://www.urbandictionary.com/add.php?word={}"
                                                      .format(target_def.replace(" ", "%20")))

                # 8Ball Code
                elif message.content.upper().startswith(".8BALL"):
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

                # Uptime Code
                elif message.content.upper().startswith(".UPTIME"):
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
                    await client.send_message(message.channel, "You're level `{}`".format(get_level(user_id)))

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

                # TODO work of this
                # Server Info
                if message.content.upper().startswith(".SERVER"):
                    server_current = message.server

                    online = 0
                    for i in message.server.members:
                        if str(i.status) == "online" or str(i.status) == "idle" or str(i.status) == "dnd":
                            online += 1
                    all_users = []
                    for user in message.server.members:
                        all_users.append("{}#{}".format(user.name, user.discriminator))
                    all_users.sort()
                    all = "\n".join(all_users)

                    if message.server.region == "us-central":
                        server_region = "US-Central"
                    else:
                        server_region = message.server.region

                    # channel_count = len([x for x in message.channel if type(x) == message.server.TextChannel])

                    role_count = len(message.server.roles)
                    emoji_count = len(message.server.emojis)
                    server_created_time = message.server.created_at

                    print("{} activated the SERVER command".format(user_name))
                    em = discord.Embed(color=0x1abc9c)
                    em.add_field(name="Name", value=message.server.name)
                    em.add_field(name="Owner", value=message.server.owner, inline=False)
                    em.add_field(name="Members", value=message.server.member_count)
                    em.add_field(name="Currently Online", value=online)
                    # em.add_field(name="Text Channels", value=str(channel_count))
                    em.add_field(name="Region", value=server_region)
                    em.add_field(name="Verification Level", value=str(message.server.verification_level).capitalize())
                    em.add_field(name="Highest ranking role", value=message.server.role_hierarchy[0])
                    em.add_field(name="Number of roles", value=str(role_count))
                    em.add_field(name="Number of custom emotes", value=str(emoji_count))
                    em.add_field(name="Created At", value=str(server_created_time)[:10])
                    em.add_field(name="Default Channel", value=message.server.default_channel)
                    em.add_field(name="AFK Channel", value=message.server.afk_channel)
                    if message.server.icon_url == "":
                        print("There is no server URL!")
                    else:
                        em.set_thumbnail(url=message.server.icon_url)
                    em.set_author(name="Server Info", icon_url="https://i.imgur.com/RHagTDg.png")
                    em.set_footer(text="Server ID: {}".format(message.server.id))
                    await client.send_message(message.channel, embed=em)

                # TODO Make request system for link
                if message.content.upper().startswith(".BETA"):
                    print(message.author)
                    owner = message.channel.server.owner.id
                    print("Server owner = {}".format(owner))
                    await client.send_message(message.channel, "Hey <@!196355904503939073>, <@{}> wants beta access. "
                                                               "Type `.allow` to send them an invite".format(user_id))
                    msg = await client.wait_for_message(content=".allow")
                    if msg is None:
                        await client.send_message(message.channel, "No response in time :(")
                    else:
                        if msg.author.id == "196355904503939073":
                            await client.send_message(message.channel,
                                                      "You've been accepted! https://discord.gg/wjPwUJx")
                            print("'.ALLOW-ER' = " + msg.author.id)
                            # await client.send_message(message.channel, "https://discord.gg/wjPwUJx")
                        else:
                            await client.send_message(message.channel, "You can't do that!")

                # Karma System
                if message.content.upper().startswith(".KARMA"):
                    if "!" in message.content[9:-1]:
                        user_req = message.content[10:-1]
                    else:
                        user_req = message.content[9:-1]

                    if message.content.upper()[7:] == "HELP":
                        embed = discord.Embed(title="Karma Commands:", color=0x1abc9c)
                        embed.add_field(name=".karma", value="Returns your karma amount.", inline=False)
                        embed.add_field(name=".karma (@name)", value="Returns (name's) karma amount.", inline=False)
                        embed.add_field(name="\u200b",
                                        value="You get 5 karma for each upvote a link you post gets, and 1 for "
                                              "each message you send.")
                        await client.send_message(message.channel, embed=embed)
                    elif message.content[7:] == "":
                        await client.send_message(message.channel,
                                                  "You have `{}` karma.".format(get_karma(user_id)))
                    else:
                        await client.send_message(message.channel,
                                                  "<@{0}> has `{1}` karma.".format(user_req, get_karma(user_req)))

                # TODO
                # if message is None:

                # Poll System
                if message.content.upper().startswith(".CREATEPOLL"):
                    print("{} created a poll".format(user_name))
                    await client.delete_message(message)

                    # Time
                    time_bot = await client.send_message(
                        message.channel, "How long should this pole go on (in seconds)")
                    time = await client.wait_for_message(timeout=120, author=message.author, channel=message.channel)
                    poll_time = int(time.content)
                    print("Time set to {}".format(poll_time))
                    await client.delete_message(time)
                    await client.delete_message(time_bot)

                    # Title
                    title_bot = await client.send_message(message.channel, "What would you like the title to be?")
                    title = await client.wait_for_message(timeout=120, author=message.author, channel=message.channel)
                    poll_title = title.content
                    print("Set title to {}".format(poll_title))
                    await client.delete_message(title)
                    await client.delete_message(title_bot)

                    # Number of Options
                    num_bot = await client.send_message(message.channel, "How many options do you want their to be? "
                                                                         "(No more than 6)")
                    options = await client.wait_for_message(timeout=120, author=message.author, channel=message.channel)
                    poll_options = int(options.content)
                    print("They choose {} options!".format(poll_options))
                    await client.delete_message(num_bot)
                    await client.delete_message(options)

                    # Option debugging
                    if poll_options <= 1:
                        await client.send_message(message.channel, "Sorry, You can't have 1 option")
                    elif poll_options > 6:
                        await client.send_message(message.channel,
                                                  "Sorry, You can't have more than 6 options!")
                    else:
                        # Option 1
                        bot_opt1 = await client.send_message(
                            message.channel, "What would you like option `one` to be called?")
                        option_1 = await client.wait_for_message(timeout=120, author=message.author,
                                                                 channel=message.channel)
                        poll_option_1 = option_1.content
                        print("Option 1 set to {}".format(poll_option_1))
                        await client.delete_message(bot_opt1)
                        await client.delete_message(option_1)

                        # Option 2
                        bot_opt2 = await client.send_message(
                            message.channel, "What would you like option `two` to be called?")
                        option_2 = await client.wait_for_message(timeout=120,
                                                                 author=message.author,
                                                                 channel=message.channel)
                        poll_option_2 = option_2.content
                        print("Option 2 set to {}".format(poll_option_2))
                        await client.delete_message(bot_opt2)
                        await client.delete_message(option_2)

                        # 2 options response
                        if poll_options == 2:
                            embed = discord.Embed(title=string.capwords(poll_title),
                                                  description="Created by: {}".format(user_name),
                                                  color=0x1abc9c)
                            embed.set_thumbnail(
                                url="https://png.icons8.com/metro/1600/poll-topic.png")
                            embed.add_field(name="1️⃣ Option 1:",
                                            value=string.capwords(poll_option_1),
                                            inline=True)
                            embed.add_field(name="2️⃣ Option 2:",
                                            value=string.capwords(poll_option_2),
                                            inline=True)
                            embed.set_footer(text="I'll announce the winners in 3 minutes.")
                            poll_message = await client.send_message(message.channel, embed=embed)
                            await client.add_reaction(poll_message, one_emote)
                            await client.add_reaction(poll_message, two_emote)

                        else:
                            # Option 3
                            bot_opt3 = await client.send_message(
                                message.channel, "What would you like option `three` to be called?")
                            option_3 = await client.wait_for_message(
                                timeout=120, author=message.author, channel=message.channel)
                            poll_option_3 = option_3.content
                            print("Option 3 set to {}".format(poll_option_3))
                            await client.delete_message(bot_opt3)
                            await client.delete_message(option_3)

                            if poll_options == 3:
                                embed = discord.Embed(title=string.capwords(poll_title),
                                                      description="Created by: {}".format(user_name),
                                                      color=0x1abc9c)
                                embed.set_thumbnail(
                                    url="https://png.icons8.com/metro/1600/poll-topic.png")
                                embed.add_field(
                                    name="1️⃣ Option 1:",
                                    value=string.capwords(poll_option_1),
                                    inline=True)
                                embed.add_field(
                                    name="2️⃣ Option 2:",
                                    value=string.capwords(poll_option_2),
                                    inline=True)
                                embed.add_field(
                                    name="3️⃣ Option 3:",
                                    value=string.capwords(poll_option_3),
                                    inline=True)
                                embed.set_footer(
                                    text="I'll announce the winners in 3 minutes.")
                                poll_message = await client.send_message(message.channel,
                                                                         embed=embed)
                                await client.add_reaction(poll_message, one_emote)
                                await client.add_reaction(poll_message, two_emote)
                                await client.add_reaction(poll_message, three_emote)
                            else:
                                # Option 4
                                bot_opt4 = await client.send_message(
                                    message.channel, "What would you like option `four` to be called?")
                                option_4 = await client.wait_for_message(
                                    timeout=120, author=message.author,
                                    channel=message.channel)
                                poll_option_4 = option_4.content
                                print("Option 4 set to {}".format(poll_option_4))
                                await client.delete_message(bot_opt4)
                                await client.delete_message(option_4)

                                if poll_options == 4:
                                    embed = discord.Embed(
                                        title=string.capwords(poll_title),
                                        description="Created by: {}".format(user_name),
                                        color=0x1abc9c)
                                    embed.set_thumbnail(
                                        url="https://png.icons8.com/metro/1600/poll-topic.png")
                                    embed.add_field(
                                        name="1️⃣ Option 1:",
                                        value=string.capwords(poll_option_1),
                                        inline=True)
                                    embed.add_field(
                                        name="2️⃣ Option 2:",
                                        value=string.capwords(poll_option_2),
                                        inline=True)
                                    embed.add_field(
                                        name="3️⃣ Option 3:",
                                        value=string.capwords(poll_option_3),
                                        inline=True)
                                    embed.add_field(
                                        name="4️⃣ Option 4:",
                                        value=string.capwords(poll_option_4),
                                        inline=True)
                                    embed.set_footer(
                                        text="I'll announce the winners in 3 minutes.")
                                    poll_message = await client.send_message(message.channel, embed=embed)
                                    await client.add_reaction(poll_message, one_emote)
                                    await client.add_reaction(poll_message, two_emote)
                                    await client.add_reaction(poll_message, three_emote)
                                    await client.add_reaction(poll_message, four_emote)
                                else:
                                    # Option 5
                                    bot_opt5 = await client.send_message(
                                        message.channel,
                                        "What would you like option `five` to be"
                                        " called?")
                                    option_5 = await client.wait_for_message(
                                        timeout=120, author=message.author,
                                        channel=message.channel)
                                    poll_option_5 = option_5.content
                                    print("Option 5 set to {}".format(poll_option_5))
                                    await client.delete_message(bot_opt5)
                                    await client.delete_message(option_5)

                                    if poll_options == 5:
                                        embed = discord.Embed(
                                            title=string.capwords(poll_title),
                                            description="Created by: {}".format(user_name),
                                            color=0x1abc9c)
                                        embed.set_thumbnail(
                                            url="https://png.icons8.com/metro/1600/poll-topic.png")
                                        embed.add_field(
                                            name="1️⃣ Option 1:",
                                            value=string.capwords(poll_option_1),
                                            inline=True)
                                        embed.add_field(
                                            name="2️⃣ Option 2:",
                                            value=string.capwords(poll_option_2),
                                            inline=True)
                                        embed.add_field(
                                            name="3️⃣ Option 3:",
                                            value=string.capwords(poll_option_3),
                                            inline=True)
                                        embed.add_field(
                                            name="4️⃣ Option 4:",
                                            value=string.capwords(poll_option_4),
                                            inline=True)
                                        embed.add_field(
                                            name="5️⃣ Option 5:",
                                            value=string.capwords(poll_option_5),
                                            inline=True)
                                        embed.set_footer(
                                            text="I'll announce the winners in 3 "
                                                 "minutes.")
                                        poll_message = await client.send_message(
                                            message.channel, embed=embed)
                                        await client.add_reaction(
                                            poll_message, one_emote)
                                        await client.add_reaction(
                                            poll_message, two_emote)
                                        await client.add_reaction(
                                            poll_message, three_emote)
                                        await client.add_reaction(
                                            poll_message, four_emote)
                                        await client.add_reaction(
                                            poll_message, five_emote)
                                    else:
                                        try:
                                            # Option 6
                                            bot_opt6 = await client.send_message(
                                                message.channel,
                                                "What would you like option `six` "
                                                "to be called?")
                                            option_6 = await client.wait_for_message(
                                                timeout=120, author=message.author,
                                                channel=message.channel)
                                            poll_option_6 = option_6.content
                                            print("Option 6 set to {}"
                                                  .format(poll_option_6))
                                            await client.delete_message(bot_opt6)
                                            await client.delete_message(option_6)

                                            embed = discord.Embed(
                                                title=string.capwords(poll_title),
                                                description="Created by: {}".format(user_name),
                                                color=0x1abc9c)
                                            embed.set_thumbnail(
                                                url="https://png.icons8.com/metro/1600/poll-topic.png")
                                            embed.add_field(name="1️⃣ Option 1:",
                                                            value=string
                                                            .capwords(poll_option_1),
                                                            inline=True)
                                            embed.add_field(name="2️⃣ Option 2:",
                                                            value=string
                                                            .capwords(poll_option_2),
                                                            inline=True)
                                            embed.add_field(name="3️⃣ Option 3:",
                                                            value=string
                                                            .capwords(poll_option_3),
                                                            inline=True)
                                            embed.add_field(name="4️⃣ Option 4:",
                                                            value=string
                                                            .capwords(poll_option_4),
                                                            inline=True)
                                            embed.add_field(name="5️⃣ Option 5:",
                                                            value=string
                                                            .capwords(poll_option_5),
                                                            inline=True)
                                            embed.add_field(name="6️⃣ Option 6:",
                                                            value=string
                                                            .capwords(poll_option_6),
                                                            inline=True)
                                            embed.set_footer(
                                                text="I'll announce the winners in"
                                                     " 3 minutes.")
                                            poll_message = await client.send_message(
                                                message.channel, embed=embed)
                                            await client.add_reaction(poll_message,
                                                                      one_emote)
                                            await client.add_reaction(poll_message,
                                                                      two_emote)
                                            await client.add_reaction(poll_message,
                                                                      three_emote)
                                            await client.add_reaction(poll_message,
                                                                      four_emote)
                                            await client.add_reaction(poll_message,
                                                                      five_emote)
                                            await client.add_reaction(poll_message,
                                                                      six_emote)
                                        except AttributeError:
                                            await client.send_message(
                                                message.channel,
                                                "Sorry, <@{}>. You didn't respond "
                                                "in time".format(message.author))

            else:
                # If user isn't Verified
                if verified_role_id not in [role.id for role in message.author.roles]:
                    await client.send_message(message.channel,
                                              "Sorry, <@{0}>. You have to be {1} to use that command!"
                                              .format(user_id, verified_role_name))

    # Server Rules Command
    if admin_role_id in [role.id for role in message.author.roles]:
        if message.content.upper().startswith(".SERVERRULES"):
            await client.delete_message(message)

            embed = discord.Embed(
                title="Synaps Rules and Info",
                url="https://steamcommunity.com/groups/team_synaps",
                color=0x1abc9c)
            embed.set_thumbnail(
                url="https://goo.gl/ibJU2z")
            embed.add_field(
                name="📜 Rules 1.)",
                value="No spamming.",
                inline=True)
            embed.add_field(
                name="👙 Rules 2.)",
                value="No NSFW in Discussion.",
                inline=True)
            embed.add_field(
                name="🎵 Rules 3.)",
                value="Please keep music requests in the music que channel.",
                inline=True)
            embed.add_field(
                name="🔰 Getting Verified:",
                value="Just add '[TS]' to your steam name and DM a Admin.",
                inline=True)
            embed.add_field(
                name="🔸 Getting Member:",
                value="Read the rules above and type '.accept' in here. If for whatever reason it doesnt work, contact"
                      " an {}.".format(admin_role_name),
                inline=True)
            await client.send_message(message.channel, embed=embed)
            await client.send_message(message.channel, "**Team Synaps Links**")
            await client.send_message(message.channel, "• http://steamcommunity.com/groups/team_synaps")
            await client.send_message(message.channel, "• https://socialclub.rockstargames.com/crew/team_synaps")
            await client.send_message(message.channel, "• https://blizzard.com/invite/XKp33F07e)")
    else:
        if admin_role_id not in [role.id for role in message.author.roles]:
            if message.content.upper().startswith(".SERVERRULES"):
                await client.send_message(message.channel,
                                          "Sorry, <@{}>. Only <@&{}>'s have permission to use this)"
                                          .format(user_id, admin_role_id))

    if message.content.startswith("This is an automated message to spawn Pokémon."):
        await client.delete_message(message)

    # Who-is command
    # Assistance from https://gist.github.com/Grewoss/c0601832982a99f59cc73510f7841fe4
    if message.content.upper().startswith(".WHOIS"):
        if message.content[7:] == "":
            await client.send_message(message.channel, "You forgot to '@' a user!")
        else:
            try:
                user = message.mentions[0]
                user_join_date = str(user.joined_at).split('.', 1)[0]
                user_created_at_date = str(user.created_at).split('.', 1)[0]

                embed = discord.Embed(
                    title="Username:",
                    description="{}:{}".format(user.name, user.discriminator),
                    color=0x1abc9c
                )
                embed.set_author(
                    name="User Info"
                )
                embed.add_field(
                    name="Joined the server at:",
                    value=user_join_date
                )
                embed.add_field(
                    name="User Created at:",
                    value=user_created_at_date
                )
                embed.add_field(
                    name="User ID:",
                    value=user.id
                )
                embed.set_thumbnail(
                    url=user.avatar_url
                )

                await client.send_message(message.channel, embed=embed)
            except IndexError:
                await client.send_message(message.channel, "Sorry, but I couldn't find that user")
            finally:
                pass

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
        elif minutes % 2 == 0:  # Even Number
            file_name = os.path.basename(sys.argv[0])
            await client.change_presence(game=discord.Game(name="version {}".format(file_name[10:-3]),
                                                           url="https://twitch.tv/mehvix", type=1))
        else:
            if hours >= 1:
                if minutes >= 10:

                    await client.change_presence(game=discord.Game(name="Live for {0}:{1}:00".format(hours, minutes),
                                                                   url="https://twitch.tv/mehvix", type=1))
                else:
                    await client.change_presence(game=discord.Game(name="Live for {0}:0{1}:00".format(hours, minutes),
                                                                   url="https://twitch.tv/mehvix", type=1))
            else:
                await client.change_presence(game=discord.Game(name="Live for {0} min.".format(minutes),
                                                               url="https://twitch.tv/mehvix", type=1))


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


"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


client.loop.create_task(uptime())

client.run(token)

