#To Do
#   Semi-Complete: Add role based effects
#   Track records of who it succeeded on, lowest percent/highest percent triggered, who got it at 1%, etc
#   Remove the Fuzzy's Executioner role from everyone in the server whenever a new person bans Fuzzy, so that there is only one person with the role at a time.

#Completed - Add role to person that most recently banned Fuzzy
#Completed - Make command only done once 24h per person

#Needed for the timer
from datetime import timedelta

#import Discord API
import discord

#create the bot
from discord.ext import commands

#let's make some random shit
import random

#literally just used to make it way for Unranked to be given
import time

import re

import json

#grab my bot's token from .env
import os
from dotenv import load_dotenv
load_dotenv()
token = os.getenv('DISCORD_TOKEN')
name = 'FuzzysaurusRex#0069'

chance = 1

#MyID: 223756729920258048
#Unranked: 694958483841482803
#SeniorAdmin: 244157417485500417 
#Admin: 244158756085039104
#Moderator: 322542712102322176
#Solder 712159699574718548
#Badmin 673560456333492250
#Booster 585542145851523076
#Fuzzy's Executioner 1005678698189553776

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='?', case_insensitive=True, intents=intents)

#This is just telling me that it's online

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

#def update_records(new_data):
#    records_file = 'records.json'
#    if os.path.exists(records_file):
#        with open(records_file, 'r') as file:
#            data = json.load(file)
#    else:
#        data = {'succeeded': [], 'lowest_percent': 100, 'highest_percent': 0, 'got_at_1': []}
#    
#    data['succeeded'].append(new_data['succeeded'])
#    data['lowest_percent'] = min(data['lowest_percent'], new_data['percent'])
#    data['highest_percent'] = max(data['highest_percent'], new_data['percent'])
#    if new_data['percent'] == 1:
#        data['got_at_1'].append(new_data['succeeded'])
#
 #   with open(records_file, 'w') as file:
  #      json.dump(data, file)

#This is the Ban Fuzzy command, making ?BanFuzzy dangerous to me.
    
@bot.command(name='BanFuzzy')
@commands.has_any_role(244157417485500417, 244158756085039104, 322542712102322176, 712159699574718548, 673560456333492250, 585542145851523076)
@commands.cooldown(1, 86400, commands.BucketType.user)
async def fuzzy_ban(ctx):
    global chance
    #Grab my name from the server and put it in the cache
    member = ctx.guild.get_member_named(name)
    #Grab name of person running command
    author = ctx.message.author
    #Simple way of doing a random chance. Chance = 1 at start, see if you're lower. Not? Next time it'll be 1 higher. If you get it, I get banned/unbanned.
    #if (True):
    if (random.randint(0,100) <= chance):
        await ctx.send("Let's find out if we're banning Fuzzy. His chance of being banned is: " + str(chance) + "%... **You did it!** He's gone! But he'll be back...and in greater numbers.")
        #await ctx.send("**VOTE FUZZY FOR CELEB. AS A CELEB HE WILL BRING MORE BANS!** His chance of being banned is: " + str(chance) + "%... **You did it!** He's gone! But he'll be back...and in greater numbers.")
        # Update the records
        #update_records({'succeeded': author.id, 'percent': chance})

        await member.ban(delete_message_days=0)
        await member.unban()
        # Remove the role from everyone in the server
        role = discord.utils.get(ctx.guild.roles, id=1005678698189553776)
        for member in ctx.guild.members:
            if role in member.roles:
                await member.remove_roles(role)
        await author.add_roles(role)
        chance = 1
    else:
        await ctx.send("Let's find out if we're banning Fuzzy. His chance of being banned is: " + str(chance) + "%... Nope! We'll get him next time! Increasing chance to ban by 1% to ensure it!")
        #await ctx.send("**VOTE FUZZY FOR CELEB. AS A CELEB HE WILL BRING MORE BANS!** His chance of being banned is: " + str(chance) + "%... Nope! We'll get him next time! Increasing chance to ban by 1% to ensure it!")
        chance += 1

#Just give me the percentage chance to ban
@bot.command(name='CheckBan')
async def check_ban(ctx):
    await ctx.send("Fuzzy's chance of being banned is: " + str(chance) + "%")

#Let's do some error checking
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        timer = str(timedelta(seconds=error.retry_after))
        timerString = timer.split(':')
        secondsString = timerString[2].split('.')
        await ctx.send(f'Give Fuzzy a break. You can try to ban him again in: {timerString[0]} Hours {timerString[1]} Minutes {secondsString[0]} Seconds.')
        #await ctx.send(f'**VOTE FUZZY FOR CELEB. AS A CELEB HE WILL BRING MORE BANS!** Give Fuzzy a break. You can try to ban him again in: {timerString[0]} Hours {timerString[1]} Minutes {secondsString[0]} Seconds.')
    elif isinstance(error, commands.MissingAnyRole):
        await ctx.send(f"Username is not in the sudoers file. This incident will be reported.")
        #await ctx.send(f"**VOTE FUZZY FOR CELEB. AS A CELEB HE WILL BRING MORE BANS!**")

#Random chat commands
@bot.event
async def on_message(message):
    if ("polestar" in str(message.content).lower() and message.author.bot == False):
        await message.channel.send('https://cdn.discordapp.com/emojis/973052369631870976.webp?size=96&quality=lossless', delete_after=5)
        #await message.channel.send(f"**VOTE FUZZY FOR CELEB. AS A CELEB HE WILL BRING MORE BANS!**")
    elif ("onlywieners" in str(message.content).lower() and message.author.bot == False):
        await message.channel.send("I see you mentioned OnlyWieners! Make sure you use promo code 'USAF' at https://www.OnlyWieners.com/lettuceboye for 20% off on my subscription! -Letty", delete_after=20)
        #await message.channel.send(f"**VOTE FUZZY FOR CELEB. AS A CELEB HE WILL BRING MORE BANS!**")
    elif ('?fuckfuzzy' in str(message.content).lower() and message.author.bot == False):
        await message.channel.send("I'm sorry, I'm just a bot and my life is a nightmare.", delete_after=15)
        #await message.channel.send(f"**VOTE FUZZY FOR CELEB. AS A CELEB HE WILL BRING MORE BANS!**")
    #elif (('waj' in str(message.content) or 'Waj' in str(message.content) or 'WaJ' in str(message.content) or 'WAj' in str(message.content)) and message.author.bot == False):
    #    await message.channel.send("It's 'waJ' you illiterate bastard! Put some respec on his name.", delete_after=30)
    #    await message.channel.send('https://cdn.discordapp.com/emojis/713184394806034463.webp?size=96&quality=lossless')
        #await message.channel.send(f"**VOTE FUZZY FOR CELEB. AS A CELEB HE WILL BRING MORE BANS!**")
    elif (re.search("[wW][aA][jJ]", str(message.content)) and not 'waJ' in str(message.content)):
        await message.channel.send("It's 'waJ' you illiterate bastard! Put some respec on his name.", delete_after=30)
        await message.channel.send('https://cdn.discordapp.com/emojis/713184394806034463.webp?size=96&quality=lossless')
    elif ('?sudo' in str(message.content).lower() and message.author.bot == False):
        await message.channel.send('''We trust you have received the usual lecture from the local System Administrator. It usually boils down to these three things:
        #1 Respect the privacy of others.
        #2 Think before you type.
        #3 With great power comes great responsibility.        
Username is not in the sudoers file. This incident will be reported.''', delete_after=15)
    elif("burgers" in str(message.content).lower() and message.author.bot == False):
        await message.channel.send("I don't watch his stuff anymore but this was good to watch", delete_after=30)
        await message.channel.send("https://youtu.be/BiiPDwCbzbM?si=slObHlShk3QTkzpS", delete_after=30)
    #Need this for on_message to not break other commands
    await bot.process_commands(message)
    
#This just removes unranked from me when I join. Checks against my ID and if it matches, removes the Unranked role via ID.
@bot.event    
async def on_member_join(member):
    fuzzy = discord.utils.get(member.guild.members, id=223756729920258048)
    role = discord.utils.get(member.guild.roles, id=694958483841482803)
    time.sleep(5)
    
    if (getattr(member, "id") == 223756729920258048):
        await fuzzy.remove_roles(role)

bot.run(token)
