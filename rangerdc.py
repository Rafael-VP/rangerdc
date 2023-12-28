#!/usr/bin/env python

import discord
from discord.ext import commands
import os
import configparser
import textwrap
import subprocess


config = configparser.ConfigParser()
config.read(os.environ['HOME'] + '/.config/rangerdc/config.ini')
client = commands.Bot(command_prefix="/", self_bot=True)


@client.event
async def on_ready():
    print("Logged in as: " + client.user.name)


@client.event
async def on_message(message):
    if message.author != client.user:
        return

    command = config['Main']['uploadcommand']
    if message.content[:len(command)] == command:
        await message.delete()
        path = str(subprocess.check_output(["/bin/sh", os.environ['HOME'] + "/.config/rangerdc/filepicker", config['Main']['defaultdir']]))[:-1][2:]

        if len(message.content) > len(command):
            text = message.content[len(command):]
        else:
            text = ""

        if message.reference:
            message = message.reference.resolved
            await message.reply(text, file=discord.File(path))
        else:
            await message.channel.send(text, file=discord.File(path))

        print("Uploading " + path)
        return

    command = config['Main']['screenshotcommand']
    if message.content[:len(command)] == command:
        if message.content[:len(command)] == command:
            await message.delete()
            path = "/tmp/screenshot.png"
            os.system("scrot -s " + path)

            if len(message.content) > len(command):
                text = message.content[len(command):]
            else:
                text = ""

            if message.reference:
                message = message.reference.resolved
                await message.reply(text, file=discord.File(path))
            else:
                await message.channel.send(text, file=discord.File(path))

            print("Uploaded screenshot.")
            os.remove(path)
        return

    command = config['Main']['cmdcommand']
    if message.content[:len(command)] == command:
        await message.delete()
        result = "```" + textwrap.wrap(os.popen(message.content[len(command)+1:]).read(), 1990)[0] + "```"
        if message.reference:
            message = message.reference.resolved
            await message.reply(result)
        else:
            await message.channel.send(result)

        print("Command executed:" + message.content[len(command):])
        return


if __name__ == '__main__':
    print("Connecting...")
    client.run(config['Main']['token'])
