# -------------------------------------------MADARA-------------------------------------------
# Madara#8657 - A general purpose bot written entirely in Python using discord.py
# Made for Uchiha's Pride discord server [https://discord.com/invite/7rNeQem4kC]
# License - [https://github.com/SpaceRanger21/madara-discord-bot/blob/master/LICENSE]
# Github Repo - [https://github.com/SpaceRanger21/madara-discord-bot]
# Made by SpaceRanger21#7533 @Discord
# ------------------------------------------COPYRIGHT-----------------------------------------
#                                        © SpaceRanger2
#
# Discord : SpaceRanger21#7533  [I don't think discord has user links ¯\_(ツ)_/¯]
# GitHub  : SpaceRanger21       [https://github.com/SpaceRanger21]
# Reddit  : u/SpaceRanger21     [https://www.reddit.com/user/SpaceRanger21]
# ============================================================================================
#                             ------------------
#                            | LIST OF COMMANDS |
#                             ------------------
# +--------------+---------------------------------------------------------+
# | Command Name | Command Description                                     |
# +--------------+---------------------------------------------------------+
# | add          | Add two, three, or four numbers.                        |
# | botstop      | Stop the bot with this command (plot twist, you can't)  |
# | cointoss     | Toss a coin (to the witcher?)                           |
# | credits      | This command shows the maker of the bot                 |
# | dice         | Roll a dice and get a random number between 1 and 6!    |
# | die          | This command returns random last words                  |
# | divide       | Divide two numbers                                      |
# | help         | Shows the help message                                  |
# | hi           | This command returns a random welcome message           |
# | kill         | Kill your friends with this command!                    |
# | mckill       | Kill your friends in Minecraft!                         |
# | multiply     | Multiply two, three, or four numbers.                   |
# | ping         | his command shows the latency of the bot                |
# | rules        | This command shows the Rules                            |
# | substract    | Subtract two numbers                                    |
# | truth        | This command tell you the truth                         |
# | whois        | This command shows information of a specific member     |
# +--------------+---------------------------------------------------------+
#
# ============================================================================================

import discord
from discord.ext import commands
from random import choice
import time
import datetime



intents = discord.Intents().all()
intents.members = True
bot = commands.Bot(command_prefix=">",intents = intents, activity = discord.Game(name=">help"))

icon_url         = "https://cdn.discordapp.com/attachments/900657033479598080/900658254768656406/unknown.png"
rules_image1_url = "https://cdn.discordapp.com/attachments/900657033479598080/900663459811840030/Rules_b.png"
rules_image2_url = "https://cdn.discordapp.com/attachments/900657033479598080/900657102849200158/Blue.gif"
rules_image3_url = "https://cdn.discordapp.com/attachments/900657033479598080/900657099984474122/Yellow.gif"
rules_image4_url = "https://cdn.discordapp.com/attachments/900657033479598080/900657106804420619/pURPLE.gif"

#-----------------------events-----------------------#

#---Logs Deleted Messages---
@bot.event
async def on_message_delete(message):
	ts = time.time()
	st = datetime.datetime.fromtimestamp(ts).strftime('%d-%m-%Y at %H:%M:%S')
	message_channel = bot.get_channel(message.channel.id) 
	embed = discord.Embed(title = "has deleted a message", description=f"{message.content}\n**in #{message_channel}**",color=discord.Color.random()).add_field(name="Time & Date", value=f"{st}").set_author(name=message.author)	
	channel = bot.get_channel(977299094722719776) #Uchiha's pride: 977299094722719776, Test Server: 977287324591345754
	await channel.send(embed = embed)

#---Logs Edited Messages---
@bot.event
async def on_message_edit(message_before, message_after):
	if message_before.author == "Dank Memer#5192":
		pass
	else:
		ts = time.time()
		st = datetime.datetime.fromtimestamp(ts).strftime('%d-%m-%Y at %H:%M:%S')
		message_channel = bot.get_channel(message_before.channel.id)
		embed = discord.Embed(title="Has edited a message", color = discord.Color.random(), description=f"**in #{message_channel}**").add_field(name="Message before", value=f"{message_before.content}", inline=False).add_field(name="Message after", value=f"{message_after.content}", inline=False).add_field(name="Time & Date",value=f"{st}",inline=False).set_author(name=message_before.author)
		channel = bot.get_channel(977299231004061756) #Uchiha's pride: 977299231004061756, Test Server: 977292597573857321
		await channel.send(embed=embed)

#---All Message Logger---
# @bot.event
# async def on_message(message: str):
#     ts = time.time()
#     st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
#     with open("logs.txt", "a") as text_file:
#         print(f"<{st}> <{message.author}> {message.content}", file=text_file)

#----------On Join Events----------

@bot.event
async def on_member_join(member):
	#rules   channel @ Uchiha's pride: #818447224556093461, Test Server: #764528019627966495
	#bots    channel @ Uchiha's pride: #818548614409879563, Test Server: #776021863188660245
	#general channel @ Uchiha's pride: #818399268955226145, Test Server: #764525792972898354
	welcome_embed = discord.Embed(title="Welcome to the server!", description=f"{member.mention} Hope you have a great time here!", color = discord.Color.from_rgb(52, 152, 219)).add_field(name="Read the rules!", value="in <#818447224556093461>").add_field(name="Check out the bots!", value="Use commands in <#818548614409879563>").add_field(name="Say Hi", value="Send your first message in <#818399268955226145>").set_thumbnail(url=member.avatar_url) 
	welcome_channel = bot.get_channel(818447187125469184) #Uchiha's pride: 818447187125469184, Test Server: 781924697116770344
	await welcome_channel.send(embed= welcome_embed)

@bot.event
async def on_member_remove(member):
	goodbye_channel = bot.get_channel(844187141596643369) #Uchiha's pride: 844187141596643369, Teste Server: 781924734824218644
	await goodbye_channel.send(f"**{member}** has just left the server, was a bitch anyways.")

#add a role to a member on join
# @bot.event
# async def on_member_join(member):
# 	Testers_role = discord.utils.get(member.guild.roles, name="Testers") 
# 	await member.add_roles(Testers_role)

#-----------------------commands-----------------------#

#---Add command---
@bot.command(help=" - add two, three, or four numbers.")
async def add(ctx, num1:int, num2:int, num3:int = None, num4:int = None):
	if num4:
		await ctx.reply(num1+num2+num3+num4)
	elif num3:
		await ctx.reply(num1+num2+num3)
	else:
		await ctx.reply(num1+num2)

#---Botstop command---
@bot.command(aliases=['bstop', 'bs'], help=' - Stop the bot with this command (plot twist, you can\'t)')
@commands.is_owner()
async def botstop(ctx):
	await ctx.send('Goodbye')
	await bot.logout()

#---Coin toss command---
@bot.command(aliases=['toss', 'coin'], help=' - Toss a coin (to the witcher?)')
async def cointoss(ctx):
	toss = ['heads', 'tails']
	await ctx.send("**Tossing a coin... **<:cointoss:905373298169368586>")
	await ctx.send(choice(toss))

#---Credits command---
@bot.command(name='credits', help=' - This command shows the maker of the bot')
async def credits(ctx):
    await ctx.send('Made by the legend himself, `SpaceRanger21#7533`')

#---Dice command---
@bot.command(name="dice", aliases=['roll'], help=' - Roll a dice and get a random number between 1 and 6!')
async def roll_a_dice(ctx):
	dice = [1, 2, 3, 4, 5, 6]
	await ctx.send("**Rolling a dice...** <:white_dice:905032599439818752> **The number is**")
	await ctx.send(choice(dice))

#---Die command---
@bot.command(name='die', help=' - This command returns random last words')
async def die(ctx):
    responses = ['*why have you brought my short life to an end??!*',
    'I could have done so much more... :\'(',
    'i have a family, kill them instead!!',
    'DON\'T KILL MEEEEEE!!',
    'NOOOOOOOOOOOOOOOOO',
    'I am far too young to die!',
    'Jokes on you I can\'t be killed!',
    'HOW CAN YOU DO THIS TO ME??! ***Dies***']

    await ctx.send(choice(responses))

#---Divide command---
@bot.command(aliases=['div'], help=" = Divide two numbers")
async def divide(ctx, num1:int, num2:int):
	await ctx.reply(num1/num2)

#---Hi command---
@bot.command(help = ' - This command returns a random welcome message')
async def hi(ctx, member : discord.Member = None):
	responses = [
	'***grumble*** Why did you wake me up?',
	'Top of the morning to you lad!',
	'Hello, how are you?',
	'Hi',
	'Wasssuup!'
	]

	if member:
		responses_tag = [
		f'Hi {member.mention}',
		f'Hello {member.mention}, how are you?',
		f'***{ctx.author}*** is saying hi to {member.mention}',
		f'What\'s up {member.mention}?'
		]
		await ctx.send(choice(responses_tag))
	else:
		await ctx.send(choice(responses))


#---Kill command---
@bot.command(help= ' - Kill your friends with this command!')
async def kill(ctx, member : discord.Member = None):
	kill_ways = [
		f"**{ctx.author}** has yeeted **{member}**",
		f"**{ctx.author}** loaded a shotgun and shot **{member}** in the head, killing them instantlly."
	]

	if member:
		await ctx.send(choice(kill_ways))
	else:
		await ctx.send("Who to kill? Please mention someone.")

#---Minecraft Kill Command---
@bot.command(help=' - Kill your friends in Minecraft!')
async def mckill(ctx, member : discord.Member):
	mcdeath = [f'**{member}** was shot by **{ctx.author}**', 
	f'**{member}** was pummeled by **{ctx.author}** using snowballs',
	f'**{member}** walked into a cactus whilst trying to escape **{ctx.author}**',
	f'**{member}** drowned whilst trying to escape **{ctx.author}**',
	f'**{member}** was slain by **{ctx.author}**',
	f'**{member}** was fireballed by **{ctx.author}**',
	f'**{member}** tried to swim in lava',
	f'**{member}** was pricked to death',
	f'**{member}** was killed by magic',
	f'**{member}** hit the ground too hard',
	f'**{member}** suffocated in a wall',
	f'**{member}** experienced kinetic energy'
	f'**{member}** went up in flames',
	f'**{member}** was stung to death',
	f'**{member}** went off with a bang whilst fighting **{ctx.author}**',
	f"**{member}** fell out of the world"]
	if member:
		await ctx.send(choice(mcdeath))
	else:
		await ctx.send("Who to kill? Please mention someone.")


#---Multiply Command---
@bot.command(aliases = ["mul"],help=" - multiply two, three, or four numbers.")
async def multiply(ctx, num1:int, num2:int, num3:int = None, num4:int = None):
	if num4:
		await ctx.reply(num1*num2*num3*num4)
	elif num3:
		await ctx.reply(num1*num2*num3)
	else:
		await ctx.reply(num1*num2)

#---Ping command---
@bot.command(name="ping", pass_context=True, help=" - This command shows the latency of the bot")
async def ping(ctx):
	await ctx.send(f'**Pong!** Latency: {round(bot.latency * 1000)}ms')

#---Rules command---
@bot.command(name="rules", aliases=['rule'], help=" - This command shows the Rules")
async def rules(ctx):
	rules_embed1 = discord.Embed(colour = discord.Color.from_rgb(255, 243, 243)).set_image(url=rules_image1_url)
	rules_embed2 = discord.Embed(title = '🚨 Here are some General rules that everyone needs to follow 🚨', color = discord.Color.from_rgb(49, 173, 204), description = '----------------------------------\n1. No **NSFW**: don\'t post any NSFW content in any channel.\n2. Don\'t abuse/fight or curse at anyone; you can still debate or argue on topics though.\n3. No self Promotions; please don\'t promote yourself anywhere in the server.\n4. Only spam in  <#821289001032876084> ,do not spam anywhere else in the server.\n5. Only discuss on topics in their respective channels; for example if you want to discuss about games then do it only on the <#818449546224074752>  channel.\n6. Competitions will be conducted in <#821293589987328040>.\n7. Chat only in English, this is an international server. You can chat in other languages in the <#834685905347543092> channel.').set_author(name='PЯłÐΞ 𒂟 Rinnegod', url=icon_url).set_image(url=rules_image2_url)
	rules_embed3 = discord.Embed(title = '🎂 Birthday Commands 🎂', color = discord.Color.from_rgb(255, 174, 71), description = '----------------------------------\n**!forget-birthday** - *Remove your Birthday*\n**!next-birthdays** - *List up to 10 paring birthday*\n**!remember-birthday** - *Add your birthday*\n**!set-user-birthday** - *set another user\'s birthday*\n**!unset-user-birthday** - *remove another user\'s birhtday*\n**!birthday** - *view your or another user\'s birthday*\n\nTo add your birthday type : `!remember-birthday 11-21` (replace the date with your birth date). The date should be in the format `mm-dd` or `mm-dd-yyyy`').set_image(url=rules_image3_url)
	rules_embed4 = discord.Embed(title = ':chart_with_upwards_trend: Ranking System  :chart_with_upwards_trend:', color = discord.Color.from_rgb(204, 42, 255,), description = '----------------------------------\n<@&819089010235801601> - *Given on level 5*\n<@&818451003229601792> - *Given on level 7*\n<@&819089007467298858> - Given on level 10\n<@&818790536575713311> - *Given on level 14*\n<@&819089004753453148> - Given on level 15\n<@&818790538085400576> -  *Given on level 21*\n<@&819089002052714546> -  *Given on level 25*\n<@&818451001718603786> -  *Given on level 28*\n<@&818451000327143436> -  *Given on level 35*\n<@&818451005204332574> -  *Given on level 45*\n<@&881034097328283678> - *Given on level 50*\n<@&881035116254752818> - *Given on level 52*\n<@&881036272548839445> - *Given on level 54*\n<@&881757270407528488> - *Given on level 56*\n\n__*NOTE:*__ Leveling is done by <@437808476106784770>. You can level up by sending messages in any channel (except for <#821289001032876084>').set_image(url=rules_image4_url)
	await ctx.send(embed = rules_embed1)
	await ctx.send(embed = rules_embed2)
	await ctx.send(embed = rules_embed3)
	await ctx.send(embed = rules_embed4)

#---Subtract command---
@bot.command(aliases=['sub'], help=" - Subtract two numbers")
async def subtract(ctx, num1:int, num2:int):
	await ctx.reply(num1-num2)

#---Truth Command---
@bot.command(help=" - This command tell you the truth")
async def truth(ctx):
	await ctx.reply("Uchiha's Pride is the best server!! <a:name:903915089139236895>")

#---Who Is command---
@bot.command(help=' - This command shows information of a specific member')
async def whois(ctx, member : discord.Member):
	if member:
		await ctx.send(f'> **Name:** `{member}`\n > **ID:** `{member.id}`\n > **Requested by** `{ctx.author}`')
	else:
		await ctx.send("Please mention a user")

#-----------------------commands-----------------------#

#---------------------editing-area---------------------#



#---------------------editing-area---------------------#

@bot.event
async def on_ready():
	print('Bot is ready!'.format(bot))
	# DiscordComponents(bot)


bot.run('TOKEN')

# -------------------------
#     © SpaceRanger21
#        2021-2022
