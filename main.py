import discord
from discord.ext import commands
import random
from animal_images import images
from secret_token import my_token


bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

#empty dictionaries to store user message count and levels 
user_messages = {}
user_levels = {}


#initilization message
@bot.event
async def on_ready():
    print("bot is ready!")

@bot.event
async def on_message(message):
    
    #ignoring messages from the bot itself
    if message.author.bot or not message.guild:
        return

    #getting user id
    user_id = str(message.author.id)

    #check if the user exists in the dictionaries, if not, then add them
    user_messages.setdefault(user_id, 0)
    user_levels.setdefault(user_id, 1)

    #increment the user's message count
    user_messages[user_id] += 1

    #check if the user has reached 10 messages
    if user_messages[user_id] == 10:

        #if user reached 10 messages, send congratulation message
        result_image = random.choice(images)
        level_up_message = f"congratulations {message.author.mention}! you've reached level {user_levels[user_id]} !!"
        await message.channel.send(level_up_message, file=discord.File(result_image))

        #resetting message count for user
        user_messages[user_id] = 0

        #increment the user's level by 1
        user_levels[user_id] += 1

    #continue with event processing
    await bot.process_commands(message)

#running bot
bot.run(my_token)
