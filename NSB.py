import discord
from discord.ext import commands
import datetime
import pytz

intents = discord.Intents.all()
intents.messages = True
intents.members = True
intents.presences = True

messages_per_day = {}
last_message_time = {}

bot = commands.Bot(command_prefix='/', intents=intents)


@bot.command(name='shutdown')
async def shutdown(ctx):
    await ctx.channel.send('Shutting down...')
    await bot.close()

@bot.event
async def on_message(message):
    await bot.process_commands(message)
    if message.author == bot.user:
        return
    today = datetime.datetime.now(pytz.timezone('America/New_York'))
    if today in messages_per_day:
        messages_per_day[today] += 1
    else:
        messages_per_day[today] = 1
    # Check if enough time has passed since the user's last message
    if message.author.id in last_message_time:
        time_since_last_message = datetime.datetime.now() - last_message_time[message.author.id]
        if time_since_last_message.total_seconds() < 86400:
            return
    else: 
        if ((today.hour > 1 and today.minute >30)and(today.hour<5 and today.minute<30)): 
            response = "<@{}>".format(message.author.id)+" **GO TO SLEEP**"
            await message.channel.send(response)
            #add to dictionary to index the number of sleepless nights. 
            return
        else: return
    
#token placement. Removed for safety reasons.   
bot.run('')

