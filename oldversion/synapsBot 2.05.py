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

description = 'synapsBot - A person Discord bot by Mehvix#7172'
Client = discord.Client()
client = commands.Bot(command_prefix='.')
seconds = 0
minutes = 0
hours = 0
days = 0

# TODO New Commands
'''''
# Request Role (verified / game)
# Cool down
# Hearthstone cards (import hearthstone)
# elif message.content.upper() == '.whoami':
# elif message.content.upper().startswith('.whois'):
# elif message.content.upper() == '.delete (messages)':
# elif message.content.upper().startswith('.vote'):
'''''

'''''
You need the following values. They are custom for every server. You can get them by typing in any text channel the 
desired value with a "\" in front of it. I.E. '\@Member' or '\:upvote:'
For your token go to https://discordapp.com/developers/applications/me, creating a new app, and getting the token by 
clicking 'reveal'.
'''''

token = 'NDE0Njc0MjU1NDAyMjM3OTY0.DWq2aQ.5z4rz6QRjdZ8QuEodYZ1GaCCLOY'
if token == 'NDE0Njc3ODYzMjU0NDU4Mzcw.DXJDCw.CX4bzf2CdhuoYB2Mh2WKKh6TP0Y':  # Bot Test
    upvote_emoji = ':upvote:414204250642579488'
    notification_channel = '414974032048553984'
    member_role_id = '414683704737267712'
    member_role_name = 'Member 🔸'
    shut_up_role = '414237651504332800'
    admin_role_name = 'Admin 💠'
    admin_role_id = '439175903600181269'
elif token == 'NDE0Njc0MjU1NDAyMjM3OTY0.DWq2aQ.5z4rz6QRjdZ8QuEodYZ1GaCCLOY':  # TS
    upvote_emoji = ':upvote:412119803034075157'
    notification_channel = '412075980094570506'
    member_role_id = '312693233329373194'
    member_role_name = 'Member 🔸'
    admin_role_name = 'Admin 💠'
    admin_role_id = '266701171002048513'
    shut_up_role = '414245504537591810'


@client.event
async def on_ready():
    users = len(set(client.get_all_members()))
    channels = len([c for c in client.get_all_channels()])
    file_name = os.path.basename(sys.argv[0])
    await client.change_presence(game=discord.Game(name='Version {}'.format(file_name[10:14])))
    servers = list(client.servers)
    print('============================================================')
    print('• Start Time:  {}'.format(datetime.datetime.now().time()))
    print('• Client Name: {}'.format(client.user))
    print('• Client ID:   {}\n'.format(client.user.id))
    print('• Channels:    {}'.format(channels))
    print('• Users:       {}'.format(users))
    print('• Connected to ' + str(len(client.servers)) + ' server(s):\n')
    for x in range(len(servers)):
        print('> ' + servers[x - 1].name)
    print('============================================================')


@client.event
async def on_resumed():
    print('Resumed.')


@client.event
async def on_member_join(member):
    client.send_message(discord.Object(id=notification_channel), '<@{}> joined the server :tada:'.format(member.id))


@client.event
async def on_member_remove(member):
    client.send_message(discord.Object(id=notification_channel), '<@{}> was either kicked or left the server :frowning'
                                                                 '2:'.format(member.id))


@client.event
async def on_reaction_add(reaction, user):
    emoji_used = '{}'.format(reaction.emoji)
    formted_uni = '<{}>'.format(upvote_emoji)
    if emoji_used == formted_uni:
        if reaction.message.author.id == user.id:
            print('{0} ({1}) upvoted there post. NO CHANGE'.format(user, user.id))
            pass
        else:
            user_add_karma(reaction.message.author.id, 5)
            print('GAVE 5 karma to {0} ({2}) for a reaction from {1} ({3})'.format(reaction.message.author, user,
                                                                                   reaction.message.author.id, user.id))


@client.event
async def on_reaction_remove(reaction, user):
    emoji_used = '{}'.format(reaction.emoji)
    formted_uni = '<{}>'.format(upvote_emoji)
    if emoji_used == formted_uni:
        if reaction.message.author.id == user.id:
            print('{0} ({1}) removed their upvote to there post. NO CHANGE'.format(user, user.id))
            pass
        else:
            user_add_karma(reaction.message.author.id, -5)
            print('REMOVED 5 karma to {0} ({2}) for a reaction from {1} ({3})'.format(reaction.message.author, user,
                                                                                      reaction.message.author.id,
                                                                                      user.id))


@client.event
async def on_message(message):
    user_id = message.author.id
    user_name = message.author
    user_add_karma(user_id, 1)
    author_level = get_level(user_id)
    author_karma = get_karma(user_id)

    print('GAVE 1 karma to {0} ({1}) for a message.'.format(user_name, user_id))

    # Checks Karma / Level
    if author_karma > 100 * (author_level + 1):
        role_name = 'Level {}'.format(author_level+1)
        level_role = discord.utils.get(message.server.roles, name=role_name)
        set_level(user_id, author_level+1)
        await client.add_roles(user_name, level_role)
        await client.send_message(message.channel, "Congrats, <@{0}>! You're now level `{1}`.  :tada: ".format(user_id,
                                                                                                            author_level+1))

    # '.accept' code
    role = discord.utils.get(message.server.roles, name=member_role_name)
    if member_role_id not in [role.id for role in message.author.roles]:
        if message.content.upper().startswith('.ACCEPT'):
            await client.add_roles(user_name, role)
            await client.delete_message(message)
            await client.send_message(discord.Object(id=notification_channel),
                                      '<@{}> is now a Member :ok_hand:'.format(user_id))
        else:
            await client.delete_message(message)

    # Karma System (BETA)
    elif message.content.upper().startswith('.KARMA'):
        if '!' in message.content[9:-1]:
            user_req = message.content[10:-1]
        else:
            user_req = message.content[9:-1]

        if message.content.upper()[7:] == 'HELP':
            embed = discord.Embed(title='Karma Commands:', color=0x0080c0)
            embed.add_field(name='.karma', value='Returns your karma amount.', inline=False)
            embed.add_field(name='.karma (@name)', value='Returns (name''s) karma amount.', inline=False)
            embed.add_field(name='\u200b', value='You get 5 karma for each upvote a link you post gets, and 1 for each'
                                                 ' message you send.')
            await client.send_message(message.channel, embed=embed)
        elif message.content[7:] == '':
            await client.send_message(message.channel, 'You have `{}` karma.'.format(get_karma(message.author.id)))
        else:
            await client.send_message(message.channel, '<@{0}> has `{1}` karma.'.format(user_req, get_karma(user_req)))

    # Leveling
    elif message.content.upper().startswith('.LEVEL'):
        await client.send_message(message.channel, "You're level `{}`".format(author_level))

    # UD Code
    elif message.content.upper().startswith('.UD'):
        target_def = message.content[4:]

        try:
            term = udtop(target_def)
            embed = discord.Embed(title='Definition Page', url='https://www.urbandictionary.com/define.php?term={}'
                                  .format(target_def), color=0x0080c0)
            embed.set_author(name='Definition for ' + target_def, url='https://www.urbandictionary.com/define.php?'
                                                                      'term={}'.format(target_def))
            embed.set_footer(text=term)
        except AttributeError:
            await client.send_message(message.channel, 'Sorry, `{0}` has no definition! You can add your own definition'
                                                       ' at https://www.urbandictionary.com/add.php?word={1}'
                                      .format(target_def, target_def))

    # 'Shut Up' code
    elif shut_up_role in [role.id for role in message.author.roles]:
        await client.send_message(message.channel, 'Shut up <@{}>'.format(user_id))

    # Upvote Code
    elif 'HTTP' in message.content.upper():
        await client.add_reaction(message, upvote_emoji)

    # 8-Ball Code
    elif message.content.upper().startswith('.8BALL'):
        def get_answer(answer_number):
            if answer_number == 1:
                return 'It is certain'
            elif answer_number == 2:
                return 'It is decidedly so'
            elif answer_number == 3:
                return 'Yes'
            elif answer_number == 4:
                return 'Reply hazy try again'
            elif answer_number == 5:
                return 'Ask again later'
            elif answer_number == 6:
                return 'Concentrate and ask again'
            elif answer_number == 7:
                return 'My reply is no'
            elif answer_number == 8:
                return 'Outlook not so good'
            elif answer_number == 9:
                return 'Very doubtful'

        r = random.randint(1, 9)
        fortune = get_answer(r)
        await client.send_message(message.channel, fortune)

    # Ping Command
    elif message.content.upper().startswith('.PING'):
        await client.send_message(message.channel, 'Pong! :ping_pong:')

    # About Command
    elif message.content.upper().startswith('.ABOUT'):
        embed = discord.Embed(title='Github', url='https://github.com/Mehvix/synaps-bot', color=0x0080c0)
        embed.set_author(name='About:', url='https://steamcommunity.com/id/Mehvix/')
        embed.set_thumbnail(url='https://goo.gl/FCddaV')
        embed.add_field(name='Creator:', value='\u200b', inline=True)
        embed.add_field(name='Mehvix#7172', value='\u200b', inline=True)
        await client.send_message(message.channel, embed=embed)

    # Help Command
    elif message.content.upper().startswith('.HELP'):
        embed = discord.Embed(title='Commands:', color=0x0080c0)
        embed.add_field(name='.uptime', value='Returns however long the bot has been online.', inline=False)
        embed.add_field(name='.8ball +question', value='Returns the true answer to a question.', inline=False)
        embed.add_field(name='.about', value='Returns info on the bot.', inline=False)
        embed.add_field(name='.karma', value='Returns your karma amount.', inline=False)
        embed.add_field(name='.karma @name', value='Returns (name''s) karma amount.', inline=False)
        embed.add_field(name='.ud +word', value='Returns (word) definition on Urban Dictionary.', inline=False)
        await client.send_message(message.channel, embed=embed)

    # Server Rules Command
    elif admin_role_id in [role.id for role in message.author.roles]:
        if message.content.upper().startswith('.SERVERRULES'):
            await client.delete_message(message)
            embed = discord.Embed(title="Synaps Rules and Info", url="https://steamcommunity.com/groups/team_synaps",
                                  color=0x0080ff)
            embed.set_thumbnail(url="https://goo.gl/ibJU2z")
            embed.add_field(name='📜 Rules 1.)', value='No spamming.', inline=True)
            embed.add_field(name='👙 Rules 2.)', value='No NSFW in Discussion.', inline=True)
            embed.add_field(name='🎵 Rules 3.)', value='Please keep music requests in the music que channel.', inline=True)
            embed.add_field(name='🔰 Getting Verified:', value='Just add "[TS]" to your steam name and DM a Admin.',
                            inline=True)
            embed.add_field(name='🔸 Getting Member:', value='Read the rules above and type ".accept" in this chat. If '
                                                             'for whatever reason it doesnt work, contact an Admin.',
                            inline=True
                            )
            await client.send_message(message.channel, embed=embed)
            await client.send_message(message.channel, '**Team Synaps Links**')
            await client.send_message(message.channel, '• http://steamcommunity.com/groups/team_synaps')
            await client.send_message(message.channel, '• https://socialclub.rockstargames.com/crew/team_synaps')
            await client.send_message(message.channel, '• https://blizzard.com/invite/XKp33F07e)')

    elif message.content.upper().startswith('.UPTIME'):
        if days > .9:
            await client.send_message(message.channel, 'The bot has been live for `{0}` day(s), `{1}` hours, `{1}` '
                                                       'minute(s), and `{2}` second(s)! :clock1:'
                                      .format(days, hours, minutes, seconds))
        elif hours > .9:
            await client.send_message(message.channel,
                                      'The bot has been live for `{0}` hour(s), `{1}` minute(s), and `{2}` second(s)!'
                                      ' :clock2:'.format(hours, minutes, seconds))
        elif minutes > .9:
            await client.send_message(message.channel,
                                      'The bot has been live for `{0}` minutes, `{1}` seconds :clock4:'
                                      .format(minutes, seconds))
        else:
            await client.send_message(message.channel,
                                      'The bot has been live for `{0}` second(s) :clock3:'.format(seconds))


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
            await client.change_presence(game=discord.Game(name='Version {}'.format(file_name[10:14])))
        else:
            if hours >= 1:
                if minutes >= 10:
                    await client.change_presence(game=discord.Game(name='Live for {0}:{1}:00'.format(hours, minutes)))
                else:
                    await client.change_presence(game=discord.Game(name='Live for {0}:0{1}:00'.format(hours, minutes)))
            else:
                await client.change_presence(game=discord.Game(name='Live for {0} min.'.format(minutes)))


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
