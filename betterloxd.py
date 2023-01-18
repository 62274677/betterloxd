import os
import discord
#import json
import yaml
import re
from logging import Logger


import time
import sqlite3
import datetime
import traceback
from seleniumboxd_helper import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# cursor.execute("CREATE TABLE user(discord_handle, username, password)")
# cursor.execute

# driver = initiate_driver()

    
 



client = discord.Client()
os.listdir("/git_repo")
os.listdir("/git_repo/data")

token = yaml.load(open('/git_repo/data/token.yaml'))['token']
prefix = 'z!'


def emote(guild, name):
    return discord.utils.get(guild.emojis, name=name)


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_error(event, *args, **kwargs):
    embed = discord.Embed(title=':x: Event Error', colour=0xe74c3c) #Red
    embed.add_field(name='Event', value=event)
    embed.description = '```py\n%s\n```' % traceback.format_exc()
    embed.timestamp = datetime.datetime.utcnow()
    await client.AppInfo.owner.send(embed=embed)
    
@client.event
async def on_message(message):
    print(message.channel.name=="movielog")
    if message.channel.name == "movielog":
        if message.content.startswith(prefix):
            print("Message seen")
            content = message.content.split(prefix)[1]
            await message.add_reaction("👀")
            print("Content: "+content)
            sql = sqlite3.connect("/git_repo/data/users.db", timeout=30)
            cursor = sql.cursor()
            driver = initiate_driver()
            wait = WebDriverWait(driver,30)
            driver.get('https://letterboxd.com/sign-in/')
            discord_handle = str(message.author)
            try:
                user = get_login(cursor,discord_handle)
            except:
                await message.channel.send("Requested user does not have an account registered with this bot.\nPlease contact your discord admin to get your login added.")
                terminate(driver,sql)
            else:
                sign_in(driver, user["username"], user["password"])
                add_movie(driver, sql, wait, content)
                await message.channel.send("Your movie, {}, has been added.".format(content))
                terminate(driver,sql)

client.run(token)
