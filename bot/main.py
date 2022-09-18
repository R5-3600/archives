# 1000 Years Later
# made by: Ryzen9-5950X-RTX3090
# stable bot version: 4.1.0
# last updated on: September 8, 2022
# created on November 30, 2021
# unstable test bot version: 4.0.1

import discord
import os
import requests
import json
import random
from replit import db
from neverSleep import neverSleep
from discord.ext import commands
from discord import Interaction

# bot = discord.Bot(debug_guilds=["821787691203952660"])
bot = commands.Bot(intents=discord.Intents.default())


@bot.event
async def on_ready():
    print('We have successfully logged in as {0.user} on Discord.'.format(bot))


@bot.slash_command(guild_ids=['821787691203952660'])
async def discordbot(interaction: Interaction):
    await interaction.response.send_message("The bot is working correctly.")


@bot.slash_command(name="first_slash")
async def first_slash(ctx):
    await ctx.respond("You executed the slash command!")


### Connection to discord
# client = discord.Client(intents=discord.Intents.default())

# sad_words = [
#     "sad", "depressed", "unhappy", "angry", "miserable", "pissed", "scared",
#     "terrified", "overwhelmed", "stressed", "depressing", "horrible", "awful",
#     "not good", "bad", "ugh", "outraged", "raged", "ticked", "not great",
#     "terrible", "mad"
# ]

# starter_encouragements = [
#     "Cheer up!", "Hang in there.", "You are doing great!",
#     "You are a great person/bot!"
# ]

# if "responding" not in db.keys():
#     db["responding"] = True


def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + " -" + json_data[0]['a']
    return (quote)


def get_joke():
    response = requests.get('https://official-joke-api.appspot.com/random_joke')
    json_data = json.loads(response.text)
    joke = json_data['setup'] + '\n\n' + json_data['punchline']
    return (joke)

# # def get_programming_joke():
# # response = requests.get('https://official-joke-api.appspot.com/jokes/programming/random')
# #  json_data = json.loads(response.text)
# #  joke = json_data[0]['setup'] + '\n\n' + json_data[0]['punchline']
# #  return joke

# def update_encouragements(encouraging_message):
#     if "encouragements" in db.keys():
#         encouragements = db["encouragements"]
#         encouragements.append(encouraging_message)
#         db["encouragements"] = encouragements
#     else:
#         db["encouragements"] = [encouraging_message]

# def delete_encouragement(index):
#     encouragements = db["encouragements"]
#     if len(encouragements) > index:
#         del encouragements[index]
#         db["encouragements"] = encouragements

# @client.event
# async def on_ready():
#     print('We have logged in as {0.user} on Discord.'.format(client))

# @client.event
# async def on_message(message):
#     if message.author == client.user:
#         return

#     if message.content.lower().startswith('hello'):
#         await message.channel.send('Hello!')

#     if message.content.lower().startswith('hola'):
#         await message.channel.send('Hola!')

#     if message.content.lower().startswith('hru'):
#         await message.channel.send('I am doing great, you?')

#     if message.content.lower().startswith('great'):
#         await message.channel.send('That is great to hear!')

#     if message.content.lower().startswith('terrible'):
#         await message.channel.send('What a shame!')

#     if message.content.lower().startswith('sup'):
#         await message.channel.send('sup weirdo')

#     if message.content.lower().startswith('weirdest'):
#         await message.channel.send('no u')

#     if message.content.lower().startswith('ur mom'):
#         await message.channel.send('no urs')

#     if message.content.lower().startswith('bye'):
#         await message.channel.send('Bye weirdo!')

#     if message.content.lower().startswith('gn'):
#         await message.channel.send('gn weirdo!')

#     if message.content.lower().startswith('gm'):
#         await message.channel.send('gm weirdo!')

#     if message.content.lower().startswith('bored'):
#         await message.channel.send('Sup bored, I am dad.')

#     if message.content.lower().startswith('ttyl'):
#         await message.channel.send('Ok see ya then')

#     if message.content.lower().startswith('!ro.build.info'):
#         await message.channel.send(
#             'V5.0.0, built on September 8, 2022, released on August 24, 2022.')

#     if message.content.lower().startswith('!download'):
#         await message.channel.send(
#             'https://github.com/Ryzen9-5950X-RTX3090/My-Summer-Game_Unity-project/releases'
#         )

#     if message.content.lower().startswith('!unity-info'):
#         await message.channel.send('Unity 2D personal, version 2022.1.15f1')

#     if message.content.lower().startswith('!source-code'):
#         await message.channel.send(
#             'https://github.com/Ryzen9-5950X-RTX3090/My-Summer-Game_Unity-project/'
#         )

#     if message.content.lower().startswith('!art-designers'):
#         await message.channel.send(
#             '@Wolvenare#7669, @Eleven | Hates NFTs#2022, @Nova Supreme#2472, and @玟静#1828.'
#         )

#     if message.content.lower().startswith('spam'):
#         await message.channel.send('https://giphy.com/gifs/spam-Hae1NrAQWyKA')

#     if message.content.lower().startswith('!bot-info'):
#         quote = get_quote()
#         await message.channel.send(
#             'stable bot version: 4.1.0, unstable test bot version: 4.0.1, last updated on: September 8, 2022, created on: November 30, 2021.'
#         )

#     if message.content.lower().startswith('updates'):
#         quote = get_quote()
#         await message.channel.send(
#             'WARNING: Do not turn of your PC. It is currently 50% done of installing the latest software upgrades! This should take aprx. 1-4 hours. ---------->>'
#         )

#     if message.content.lower().startswith('birthday'):
#         quote = get_quote()
#         await message.channel.send('Happy birthday!')

#     if message.content.lower().startswith('bday'):
#         quote = get_quote()
#         await message.channel.send('Happy birthday!')

#     if message.content.lower().startswith('christmas'):
#         quote = get_quote()
#         await message.channel.send('Merry Christmas!')

#     if message.content.lower().startswith('thanksgiving'):
#         quote = get_quote()
#         await message.channel.send('Happy Thanksgiving!')

#     if message.content.lower().startswith('halloween'):
#         quote = get_quote()
#         await message.channel.send('Happy Halloween!')

#     if message.content.lower().startswith('4th of july'):
#         quote = get_quote()
#         await message.channel.send('Happy 4th of July!')

#     if message.content.lower().startswith('new year'):
#         quote = get_quote()
#         await message.channel.send('Happy New Year!')

#     if message.content.lower().startswith('!github'):
#         quote = get_quote()
#         await message.channel.send(
#             'https://github.com/Ryzen9-5950X-RTX3090?tab=repositories')

#     if message.content.lower().startswith('!website'):
#         quote = get_quote()
#         await message.channel.send('https://ryzen9-5950x-rtx3090.github.io/')

#     if message.content.lower().startswith('!bot-source-code'):
#         quote = get_quote()
#         await message.channel.send(
#             'https://github.com/Ryzen9-5950X-RTX3090/1000-Years-Later_discord-bot/'
#         )

#     if message.content.lower().startswith('/bot-commands'):
#         quote = get_quote()
#         await message.channel.send(
#             'https://github.com/Ryzen9-5950X-RTX3090/1000-Years-Later_discord-bot/wiki/'
#         )


@bot.slash_command(guild_ids=['821787691203952660'])
async def inspire(interaction: Interaction):
    quote = get_quote()
    await interaction.response.send_message(quote)


@bot.slash_command(guild_ids=['821787691203952660'])
async def jokes(interaction: Interaction):
    quote = get_joke()
    await interaction.response.send_message(joke)

# # if message.content.startswith('!programming-jokes'):
# #   joke = get_programming_joke()
# #   await message.channel.send(joke)

#     if db["responding"]:
#         options = starter_encouragements
#         if "encouragements" in db.keys():
#             for i in range(len(db["encouragements"])):
#                 options.append(db["encouragements"][i])

#         if any(word in message.content for word in sad_words):
#             await message.channel.send(random.choice(options))

#     if message.content.lower().startswith("$new"):
#         encouraging_message = message.content.split("$new ", 1)[1]
#         update_encouragements(encouraging_message)
#         await message.channel.send(
#             "The new encouraging message has been added to the database.")

#     # if message.content.lower().startswith("$del"):
#     # encouragements = []
#     # if "encouragements" in db.keys():
#     #   index = int(message.content.split("$del", 1)[1])
#     #   delete_encouragement(index)
#     #   encouragements = db["encouragements"]
#     # await message.channel.send(encouragements)

#     if message.content.lower().startswith("$list"):
#         encouragements = []
#         if "encouragements" in db.keys():
#             encouragements = db["encouragements"]
#         await message.channel.send(encouragements)

#     if message.content.lower().startswith("$responding"):
#         value = message.content.split("$responding ", 1)[1]

#         if value.lower() == "true":
#             db["responding"] = True
#             await message.channel.send("Responding is on.")
#         else:
#             db["responding"] = False
#             await message.channel.send("Responding is off.")

# neverSleep()
# token = os.environ.get("DiscordBot_token")
# client.run(token)

# ### Extensions(cogs) Load and Unload
# @client.command(brief='Load an extension')
# async def load(ctx, extension):
#     client.load_extension(f'extensions.{extension}')
#     await ctx.send(f'{extension} extension loaded.')

# @client.command(brief='Unload an extension')
# async def unload(ctx, extension):
#     client.unload_extension(f'extensions.{extension}')
#     await ctx.send(f'{extension} extension unloaded.')

# # Auto Load extensions
# for filename in os.listdir('./extensions'):
#     if filename.endswith('.py'):
#         client.load_extension(f'extensions.{filename[:-3]}')
#         print(f'loaded {filename[:-3]}')
#     else:
#         print(f'Unable to load {filename[:-3]}')

bot.run(str(os.environ['DiscordBot_token']))
