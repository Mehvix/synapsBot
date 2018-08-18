#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import time
import json
import karma
import random
import discord
import asyncio
import curtime
import settings
from discord.ext import commands
from urbandictionary_top import udtop

clock_emoji = ["🕐", "🕑", "🕒", "🕓", "🕔", "🕕", "🕖", "🕗", "🕘", "🕙", "🕚", "🕛"]  # Use random.choice(clock_emoji)


class Verified:
    def __init__(self, client):
        self.client = client

    print("Loading Verified...")

    async def on_message(self, message):
        # Message author variables
        user_id = message.author.id
        user_name = message.author

        author_level = karma.get_level(user_id)
        author_karma = karma.get_karma(user_id)

        if message.server:
            if settings.verified_role_id in [role.id for role in message.author.roles]:
                # UD Code
                if message.content.upper().startswith(".UD"):
                    target_def = message.content[4:]
                    target_def_link_format = target_def.replace(" ", "%20")

                    if "MAGGIE" in message.content.upper():  # Hey don't worry about these couple of lines
                        print("{0}: {1}  requested the UD for Maggie".format(curtime.get_time(), user_name))
                        embed = discord.Embed(title="Definition Page", url="https://goo.gl/j2DX9N", color=embed_color)
                        embed.set_author(name="Definition for Maggie", url="https://goo.gl/j2DX9N")
                        embed.add_field(name="Definition 📚", value="Girl with YUUUG milkers. Doesnt need a coat",
                                        inline=False)
                        embed.add_field(name="Example 💬",
                                        value="Maggie's got such big fun-fun milk bags, she doesn't need a coat! "
                                              "-Aidan Witkovsky 2018",
                                        inline=True)
                        await self.client.send_message(message.channel, embed=embed)
                    else:
                        try:
                            term = udtop(target_def)
                            print("{0}: {1} requested the UD for {2}".format(curtime.get_time(), user_name, target_def))
                            embed = discord.Embed(title="Definition Page", color=embed_color)
                            embed.set_author(name="Definition for {}".format(string.capwords(target_def)))
                            embed.add_field(name="Definition 📚", value=term.definition[:1024], inline=False)
                            embed.add_field(name="Example 💬", value=term.example[:1024], inline=True)
                            await self.client.send_message(message.channel, embed=embed)
                        except (IndexError, AttributeError):
                            await self.client.send_message(message.channel,
                                                           "Sorry, that word doesnt have a definition :( "
                                                           ". You can add your own here: ")
                            await self.client.send_message(
                                message.channel,
                                "https://www.urbandictionary.com/add.php?word=" + target_def_link_format)

                # 8Ball Code
                if message.content.upper().startswith(".8BALL"):
                    print("{0}: {1} requested '.8BALL'".format(curtime.get_time(), user_name))

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
                    await self.client.send_message(message.channel, fortune)

                # Uptime Code
                if message.content.upper().startswith(".UPTIME"):
                    print("{0}: {1} requested '.UPTIME'".format(curtime.get_time(), user_name))

                    await self.client.send_message(message.channel, "The bot has been live for `{}` {}".format(
                        curtime.uptime(), random.choice(clock_emoji)))

                # Gets random bear picture
                if message.content.upper().startswith(".BEAR"):
                    print("{0}: {1} sent a bear".format(curtime.get_time(), user_name))
                    fp = random.choice(os.listdir("media/bears"))
                    await self.client.send_file(message.channel, "media/bears/{}".format(fp))

                    # Gets random Sam picture
                if message.content.upper().startswith(".SAM"):
                    print("{0}: {1} sent a sam".format(curtime.get_time(), user_name))
                    fp = random.choice(os.listdir("media/sams"))
                    await self.client.send_file(message.channel, "media/sams/{}".format(fp))

                    # Gets random Apu picture
                if message.content.upper().startswith(".APU"):
                    print("{0}: {1} sent a apu".format(curtime.get_time(), user_name))
                    fp = random.choice(os.listdir("media/apus"))
                    await self.client.send_file(message.channel, "media/apus/{}".format(fp))

                # Server Info
                if message.content.upper().startswith(".SERVERINFO"):
                    print("{0}: {1} requested '.SERVER'".format(curtime.get_time(), user_name))
                    online = 0
                    for i in message.server.members:
                        if str(i.status) == "online" or str(i.status) == "idle" or str(i.status) == "dnd":
                            online += 1

                    role_count = len(message.server.roles)
                    emoji_count = len(message.server.emojis)
                    server_created_time = message.server.created_at

                    print("{0}: {1} activated the SERVER command".format(curtime.get_time(), user_name))
                    em = discord.Embed(color=settings.embed_color)
                    em.set_author(name="Server Info:")
                    em.add_field(name="Server Name:", value=message.server.name)
                    em.add_field(name="Owner:", value=message.server.owner, inline=False)
                    em.add_field(name="Members:", value=message.server.member_count)
                    em.add_field(name="Memebers Online:", value=online)
                    # em.add_field(name="Text Channels", value=str(channel_count))
                    em.add_field(name="Region:", value=message.server.region)
                    em.add_field(name="Verification Level:", value=str(message.server.verification_level).capitalize())
                    em.add_field(name="Highest ranking role:", value=message.server.role_hierarchy[0])
                    em.add_field(name="Number of roles:", value=str(role_count))
                    em.add_field(name="Number of custom emotes:", value=str(emoji_count))
                    em.add_field(name="Created At:", value=str(server_created_time)[:10])
                    em.add_field(name="Default Channel:", value=message.server.default_channel)
                    em.add_field(name="AFK Time:", value=message.server.afk_timeout + "seconds")
                    em.add_field(name="AFK Channel:", value=message.server.afk_channel)
                    em.add_field(name="Voice Client:", value=message.server.voice_client)
                    em.add_field(name="Icon URL", value=message.server.icon_url)
                    em.set_thumbnail(url=message.server.icon_url)
                    em.set_author(name="\u200b")
                    em.set_footer(text="Server ID: {}".format(message.server.id))
                    await self.client.send_message(message.channel, embed=em)

                # Gives Server Emojis
                if message.content.upper().startswith(".EMOTES"):
                    print("{0}: {1} activated the EMOTES command".format(curtime.get_time(), user_name))
                    emojis = [str(x) for x in message.server.emojis]
                    emojis_str = "".join(emojis)
                    await self.client.send_message(message.channel, emojis_str)

                    # Gives link to beta testing server
                if message.content.upper().startswith(".BETA"):
                    print("{0}: {1} activated the BETA command".format(curtime.get_time(), user_name))
                    user = await self.client.get_user_info(user_id)
                    await self.client.send_message(message.channel,
                                                   "Hey <@!196355904503939073>, <@{}> wants beta access.\nType"
                                                   " `.allow` to send them an invite".format(user_id))
                    msg = await self.client.wait_for_message(content=".allow")
                    if msg is None:
                        await self.client.send_message(
                            message.channel,
                            "<@!196355904503939073> didn't respond in time :(. Please try another time.")
                    else:
                        if msg.author.id == "196355904503939073":  # My Discord ID
                            testinvite = settings.get_json('./test_server.json')
                            invite = testinvite.get("invite")
                            await self.client.send_message(user, "You've been accepted! {}".format(invite))
                            await self.client.send_message(message.channel,
                                                           "<@{}> was accepted into the beta testing server! "
                                                           ":tada:".format(user_id))
                        else:
                            await self.client.send_message(message.channel, "You can't do that!")

                if message.content.upper().startswith(".DMME"):
                    user = await self.client.get_user_info(user_id)
                    await self.client.send_message(user, "DM")

                # Who-is command
                # Assistance from https://gist.github.com/Grewoss/c0601832982a99f59cc73510f7841fe4
                if message.content.upper().startswith(".WHOIS"):
                    print("{0}: {1} requested '.WHOIS'".format(curtime.get_time(), user_name))
                    try:
                        user = message.mentions[0]
                    except IndexError:
                        await self.client.send_message(message.channel, "You `@` a role, not a user!")
                    full_user_name = "{}#{}".format(user.name, user.discriminator)
                    if message.content[7:] is None:
                        await self.client.send_message(message.channel, "You forgot to '@' a user!")
                    else:
                        try:
                            user_join_date = str(user.joined_at).split('.', 1)[0]
                            user_created_at_date = str(user.created_at).split('.', 1)[0]
                            avatar = user.avatar_url if user.avatar else user.default_avatar_url

                            embed = discord.Embed(title="Username:", description=full_user_name,
                                                  color=settings.embed_color)
                            embed.set_author(name="User Info")
                            embed.add_field(name="Joined the server at:", value=user_join_date[:10])
                            embed.add_field(name="User Created at:", value=user_created_at_date[:10])
                            embed.add_field(name="User ID:", value=user.id)
                            embed.add_field(name="User Status:", value=str(user.status).title())
                            embed.add_field(name="User Game:", value=user.game)
                            embed.add_field(name="User Custom Name:", value=user.nick)
                            embed.add_field(name="User Color:", value=user.color)
                            if len(user.roles) > 1:  # TIL @everyone is a role that is assigned to everyone but hidden
                                embed.add_field(name="User Top Role (Level):", value=user.top_role)
                            else:
                                embed.add_field(name="User Top Role (Level):", value="User has no roles")
                            embed.add_field(name="User Avatar URL", value=avatar)
                            embed.set_thumbnail(url=user.avatar_url)
                            await self.client.send_message(message.channel, embed=embed)
                        except (IndexError, AttributeError):
                            print("{0}: {1} requested '.WHOIS' but they DIDN'T exist".format(curtime.get_time(),
                                                                                             user_name))
                            await self.client.send_message(message.channel, "Sorry, but I couldn't find that user")
                        finally:
                            pass

                if message.content.upper().startswith(".BANLIST"):
                    ban_list = await self.client.get_bans(message.server)
                    if not ban_list:
                        await self.client.send_message(message.channel, "This server doesn't have anyone banned (yet)")
                    else:
                        userid = [user.id for user in ban_list]
                        name = [user.name for user in ban_list]
                        discriminator = [user.discriminator for user in ban_list]
                        bot = [user.bot for user in ban_list]

                        newlist = []
                        for item in bot:
                            if item:
                                item = "<:bottag:473742770671058964>"
                            else:
                                item = ""
                            newlist.append(item)
                        bot = newlist

                        total = list((zip(userid, name, discriminator, bot)))

                        # Thanks to happypetsy on stackoverflow for helping me with this!
                        pretty_list = set()
                        for details in total:
                            data = "•<@{}>{} ({}#{}) ".format(details[0], details[3], details[1], details[2])
                            pretty_list.add(data)

                        await self.client.send_message(message.channel,
                                                       "**Ban list:** \n{}".format("\n".join(pretty_list)))

                # Create an Invite
                if message.content.upper().startswith(".CREATEINVITE"):
                    invite = await self.client.create_invite(destination=message.channel, max_age=0, temporary=False,
                                                             unique=True)
                    await self.client.send_message(message.channel, invite)

                if message.content.upper().startswith(".INVITE"):
                    if not message.raw_mentions:
                        await self.client.send_message(message.channel, 'You need to `@` a user (maybe you meant '
                                                                        '`.createinvite` :thinking:')
                    else:
                        invite_target = message.raw_mentions[0]
                        user = await self.client.get_user_info(invite_target)
                        invite = await self.client.create_invite(destination=message.channel, max_age=0,
                                                                 temporary=False,
                                                                 unique=True)
                        try:
                            await self.client.send_message(
                                user, "<@{}> ({}) wants to invite  you to `{}`. You can join with this link: {}".format(
                                    message.author.id, message.author.name, message.server.name, invite))
                        except discord.Forbidden:
                            await self.client.send_message(message.channel, "Sorry, but I cannot send a message to "
                                                                            "that user due to there privacy settings "
                                                                            ":(")
                # Roulette system
                if message.content.upper().startswith(".ROULETTE"):
                    if message.content.upper().startswith(".ROULETTE HELP"):
                        print("{0}: {1} requested roulette help")
                        embed = discord.Embed(title="Outcomes:", color=settings.embed_color)
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
                                        value="Just type '.roulette'",
                                        inline=True)
                        embed.set_footer(
                            text="Maximum bet is 250 karma. Winning on zero will quattuordecuple (x14) your "
                                 "bet while odd and even will double your bet")
                        await self.client.send_message(message.channel, embed=embed)
                        return None
                    if message.content.upper().startswith(".ROULETTE OUTCOMES"):
                        with open('C:/Users/maxla/PycharmProjects/synapsBot remastered/roulette_outcomes.json',
                                  'r') as fp:
                            outcomes = json.load(fp)
                        odd_total = outcomes['odd']
                        even_total = outcomes['even']
                        zero_total = outcomes['zero']
                        total_total = outcomes['total']

                        outcomes_list = [odd_total, even_total, zero_total]
                        total = sum(outcomes_list)
                        embed = discord.Embed(title="\u200b", color=settings.embed_color)
                        embed.set_author(name="Roulette Outcomes 📊")
                        embed.add_field(name="Total number of times 'spun'", value=total, inline=True)
                        embed.add_field(name="Total Bet", value=total_total, inline=False)
                        embed.add_field(name="Odd", value=odd_total, inline=True)
                        embed.add_field(name="Even", value=even_total, inline=True)
                        embed.add_field(name="Zero", value=zero_total, inline=True)
                        await self.client.send_message(message.channel, embed=embed)
                        return None
                    else:
                        await self.client.send_message(
                            message.channel,
                            "How much would you like to bet? It must be between `10` and `250` and cannot be "
                            "more than your karma (`{}`)".format(karma.get_karma(user_id)))
                        bet_amount_message = await self.client.wait_for_message(
                            timeout=120, author=message.author, channel=message.channel)
                        try:
                            bet_amount = int(bet_amount_message.content)
                            print("{0}: Bet {1}".format(curtime.get_time(), bet_amount))
                        except ValueError:
                            await self.client.send_message(
                                message.channel, "Sorry, you need to bet a number between `10` and `250`")
                            return
                        except IndexError:
                            await self.client.send_message(
                                message.channel, "Sorry, you need to bet a number between `10` and `250`")
                            return

                        if 10 <= bet_amount <= 250:
                            if bet_amount > author_karma:
                                await self.client.send_message(
                                    message.channel, "You don't have enough karma! You must bet under `{}`".format(
                                        karma.get_karma(user_id)))
                                return

                            with open('C:/Users/maxla/PycharmProjects/synapsBot remastered/roulette_outcomes.json',
                                      'r') as fp:
                                outcomes = json.load(fp)
                            outcomes['total'] += bet_amount
                            with open('C:/Users/maxla/PycharmProjects/synapsBot remastered/roulette_outcomes.json',
                                      'w') as fp:
                                json.dump(outcomes, fp, sort_keys=True, indent=4)

                            outcomes = ["zero", "even", "odd"]
                            await self.client.send_message(
                                message.channel,
                                "What outcome would you like to bet on? The options are `zero`, `even`, or "
                                "`odd`")
                            outcomes_response = await self.client.wait_for_message(
                                timeout=120, author=message.author, channel=message.channel)

                            try:
                                outcomes_formatted = outcomes_response.content
                                outcomes_formatted = outcomes_formatted.lower()
                                print("{0}: Outcome set to {1}".format(curtime.get_time(), outcomes_formatted))
                            except AttributeError:
                                await self.client.send_message(
                                    message.channel,
                                    "<@{}> DIDN'T respond fast enough, so the roulette was canceled".format(
                                        message.author.id))
                                return

                            if outcomes_formatted in outcomes:
                                print("{0}: Outcome set to {1}".format(curtime.get_time(), outcomes_formatted))
                                karma.user_add_karma(user_id, -int(bet_amount))
                                print("{0}: subtracted {1} karma for bet".format(curtime.get_time(), -int(bet_amount)))
                                rolling_message = await self.client.send_message(message.channel, "Spinning")
                                await asyncio.sleep(.25)
                                await self.client.edit_message(rolling_message, "Spinning.")
                                await asyncio.sleep(.25)
                                await self.client.edit_message(rolling_message, "Spinning..")
                                await asyncio.sleep(.25)
                                await self.client.edit_message(rolling_message, "Spinning...")
                                await asyncio.sleep(.25)
                                await self.client.delete_message(rolling_message)

                                spin = random.randint(0, 36)
                                print("{0}: Landed on {1}".format(curtime.get_time(), spin))
                                msg = await self.client.send_message(message.channel, "It landed on `{}`!".format(spin))
                                if msg.content == "It landed on `0`!":
                                    await self.client.pin_message(msg)
                                    david_dm = await self.client.get_user_info("240608458888445953")
                                    await self.client.send_message(david_dm,
                                                                   "Someone landed on 0 via roulette in `{}`".format(
                                                                       message.server.name))

                                if spin == 0:
                                    with open(
                                            'C:/Users/maxla/PycharmProjects/synapsBot remastered/roulette_outcomes.json',
                                            'r') as fp:
                                        outcomes = json.load(fp)
                                    outcomes['zero'] += 1
                                    with open(
                                            'C:/Users/maxla/PycharmProjects/synapsBot remastered/roulette_outcomes.json',
                                            'w') as fp:
                                        json.dump(outcomes, fp, sort_keys=True, indent=4)

                                    if outcomes_formatted == "zero":
                                        karma.user_add_karma(user_id, int(bet_amount * 14))
                                        msg = await self.client.send_message(
                                            message.channel,
                                            "Winner! :tada:\n You quattuordecuple up on karma for a total of "
                                            "`{}`!".format(karma.get_karma(user_id)))
                                        print("{0}: won on zero! {1}".format(curtime.get_time(), bet_amount))
                                        await self.client.pin_message(msg)
                                        return
                                    else:
                                        await self.client.send_message(
                                            message.channel,
                                            "Sorry, better luck next time. You now have `{}` karma".format(
                                                karma.get_karma(user_id)))
                                else:
                                    if spin % 2 == 0:
                                        with open(
                                                'C:/Users/maxla/PycharmProjects/synapsBot '
                                                'remastered/roulette_outcomes.json',
                                                'r') as fp:
                                            outcomes = json.load(fp)
                                        outcomes['even'] += 1
                                        with open(
                                                'C:/Users/maxla/PycharmProjects/synapsBot '
                                                'remastered/roulette_outcomes.json',
                                                'w') as fp:
                                            json.dump(outcomes, fp, sort_keys=True, indent=4)

                                        if outcomes_formatted == "even":
                                            karma.user_add_karma(user_id, int(bet_amount * 2))
                                            await self.client.send_message(message.channel,
                                                                           "Winner! :tada:\n You doubled up on karma "
                                                                           "for a total of `{}`!".format(
                                                                               karma.get_karma(user_id)))
                                        else:
                                            await self.client.send_message(
                                                message.channel,
                                                "Sorry, better luck next time. You now have `{}` karma".format(
                                                    karma.get_karma(user_id)))
                                    else:
                                        with open(
                                                'C:/Users/maxla/PycharmProjects/synapsBot '
                                                'remastered/roulette_outcomes.json', 'r') as fp:
                                            outcomes = json.load(fp)
                                        outcomes['odd'] += 1
                                        with open(
                                                'C:/Users/maxla/PycharmProjects/synapsBot '
                                                'remastered/roulette_outcomes.json', 'w') as fp:
                                            json.dump(outcomes, fp, sort_keys=True, indent=4)
                                        if outcomes_formatted == "odd":
                                            karma.user_add_karma(user_id, int(bet_amount * 2))
                                            await self.client.send_message(message.channel,
                                                                           "Winner! :tada:\n You doubled up on karma "
                                                                           "for a total of `{}`!".format(
                                                                               karma.get_karma(user_id)))
                                        else:
                                            await self.client.send_message(
                                                message.channel,
                                                "Sorry, better luck next time. You now have `{}` karma".format(
                                                    karma.get_karma(user_id)))
                            else:
                                await self.client.send_message(
                                    message.channel, "`ERROR:` You needed to enter `zero`, `even`, or `odd`")
                        else:
                            await self.client.send_message(message.channel,
                                                           "Sorry, you need to bet a number between `10` and `250`")
                            return

                if message.content.upper().startswith(".BANNEDWORDS"):
                    banned_words = settings.get_json(
                        "C:/Users/maxla/PycharmProjects/synapsBot remastered/banned_words.json")
                    await self.client.send_message(
                        message.channel, "**Banned Words List:** \n• `{}`".format("`\n• `".join(banned_words)))
        else:
            return


def setup(client):
    client.add_cog(Verified(client))
