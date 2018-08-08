import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import os
import sys
import random


Client = discord.Client()
client = commands.Bot(command_prefix=".")

seconds = 0
minutes = 0
hours = 0

# TODO Tokens Changed:


@client.event
async def on_ready():
    file_name = os.path.basename(sys.argv[0])
    await client.change_presence(game=discord.Game(name="Version {}".format(file_name[10:14])))
    servers = list(client.servers)
    print("==============================")
    print("• Client Name: {}".format(client.user.name))
    print("• Client ID:   {}".format(client.user.id))
    print(" ")
    print("• Connected to " + str(len(client.servers)) + " server(s):")
    for x in range(len(servers)):
        print('> ' + servers[x-1].name)
    print("==============================")


@client.event
async def on_resumed():
    print("Resumed.")
    bot.counter["session_resumed"] += 1


@client.event
async def on_member_join(member):
    await client.send_message(discord.Object(id="412075980094570506"),
                              "<@{}> joined the server :tada:".format(member.id))


@client.event
async def on_member_remove(member):
    await client.send_message(discord.Object(id="412075980094570506"),
                              "<@{}> was either kicked, banned, or left the server :frowning2:".format(member.id))


@client.event
async def on_message(message):
    user_id = message.author.id

    # ".accept" code
    role = discord.utils.get(message.server.roles, name="Member 🔸")
    if '312693233329373194' not in [role.id for role in message.author.roles]:
        if message.content.upper().startswith('.ACCEPT'):
            await client.add_roles(message.author, role)
            await client.delete_message(message)
            await client.send_message(discord.Object(id="412075980094570506"),
                                      "<@{}> is now a Member :ok_hand:".format(user_id))
        else:
            await client.delete_message(message)

    # "Shut Up" code
    elif '414245504537591810' in [role.id for role in message.author.roles]:
        await client.send_message(message.channel, "Shut up <@{}>".format(user_id))

    # Upvote Code
    elif 'HTTP' in message.content.upper():
        await client.add_reaction(message, 'upvote:412119803034075157')

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

    elif message.content == '.ping':
        await client.send_message(message.channel, "Pong! :ping_pong:")

    elif message.content.upper().startswith('.UPTIME'):
        if hours > .9:
            await client.send_message(message.channel,
                                      "The bot has been live for `{0}` hour(s), `{1}` minute(s), and `{2}` second(s)!"
                                      " :clock2:".format(hours, minutes, seconds))
        elif minutes > .9:
            await client.send_message(message.channel,
                                      "The bot has been live for `{0}` minutes, `{1}` seconds :clock4:"
                                      .format(minutes, seconds))
        else:
            await client.send_message(message.channel,
                                      "The bot has been live for `{0}` second(s) :clock3:".format(seconds))


async def uptime():
    await client.wait_until_ready()
    global seconds
    global minutes
    global hours
    minutes = 0
    while not client.is_closed:
        await asyncio.sleep(1)
        seconds += 1
        if seconds == 60:
            seconds = 0
            minutes += 1
        if minutes == 60:
            minutes = 0
            hours += 1

client.loop.create_task(uptime())
client.run("TOKEN")
