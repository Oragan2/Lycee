import discord
from discord.ext import commands
import re
import aiohttp
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
OPENWEATHER_API_KEY = os.getenv('WEATHER_API')
WEATHER_API_URL = "http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

learned_patterns = {}

async def fetch_weather(city):
    url = WEATHER_API_URL.format(city=city, api_key=OPENWEATHER_API_KEY)
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                return await response.json()
            else:
                return None

async def handle_greeting(message):
    greetings_en = r"(hello|hi|hey|greetings|good morning|good evening|good afternoon)\b"
    greetings_fr = r"(bonjour|salut|coucou|bonne journée|bonsoir)\b"
    if re.search(greetings_en, message.content, re.IGNORECASE):
        return f"Hello {message.author.mention}!"
    elif re.search(greetings_fr, message.content, re.IGNORECASE):
        return f"Bonjour {message.author.mention} !"
    return None

async def handle_weather_request(message):
    weather_pattern = r"(what's the weather like in|weather in|temperature in)\s+(?P<city>\w+)"
    match = re.search(weather_pattern, message.content, re.IGNORECASE)
    if match:
        city = match.group("city")
        weather_data = await fetch_weather(city)
        if weather_data:
            try:
                temperature = weather_data['main']['temp']
                description = weather_data['weather'][0]['description'].capitalize()
                humidity = weather_data['main']['humidity']
                wind_speed = weather_data['wind']['speed']
                return f"The weather in {city} is currently: {description}, with a temperature of {temperature}°C, {humidity}% humidity, and wind speeds of {wind_speed} m/s."
            except KeyError:
                return f"Sorry, I couldn't parse the weather data for {city}."
        else:
            return f"Sorry, I couldn't retrieve the weather information for {city}. Please make sure the city name is correct."
    return None

async def handle_joke_request(message):
    joke_pattern = r"(tell me a joke|make me laugh)"
    if re.search(joke_pattern, message.content, re.IGNORECASE):
        jokes = [
            "Why don't scientists trust atoms? Because they make up everything!",
            "Parallel lines have so much in common... it’s a shame they’ll never meet.",
            "Why did the scarecrow win an award? Because he was outstanding in his field!"
        ]
        import random
        return random.choice(jokes)
    return None

async def handle_mention(message):
    responses = []
    intents = 'unknow'
    greeting_response = await handle_greeting(message)
    if greeting_response:
        responses.append(greeting_response)
        intents = 'greeting'

    weather_response = await handle_weather_request(message)
    if weather_response:
        responses.append(weather_response)
        intents = 'get_weather'

    joke_response = await handle_joke_request(message)
    if joke_response:
        responses.append(joke_response)
        intents = 'demand_joke'

    with open("intent_data.txt","a") as file:
        file.write(f"{message.author}:{message.content}\t{intents}\n")

    if responses and bot.user.mentioned_in(message):
        await message.channel.send("\n".join(responses))
        return True
    return False

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')
    for guild in bot.guilds:
        if guild.id not in learned_patterns:
            learned_patterns[guild.id] = []

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    # Process learning regardless of mention
    if message.content.startswith("!learn"):
        await bot.process_commands(message)
        return
    elif message.content.startswith("!recall"):
        await bot.process_commands(message)
        return
    elif message.content.startswith("!add_pattern"):
        await bot.process_commands(message)
        return
    await handle_mention(message)

@bot.command()
async def learn(ctx, key, *, value):
    guild_id = ctx.guild.id
    if guild_id not in learned_patterns:
        learned_patterns[guild_id] = {}
    learned_patterns[guild_id][key.lower()] = value
    await ctx.send(f"Okay, I've learned that {key} is {value} in this server.")

@bot.command()
async def recall(ctx, key):
    guild_id = ctx.guild.id
    if guild_id in learned_patterns and key.lower() in learned_patterns[guild_id]:
        await ctx.send(f"{key} is {learned_patterns[guild_id][key.lower()]} in this server.")
    else:
        await ctx.send(f"Sorry, I haven't learned anything about {key} in this server yet.")

@bot.command()
async def add_pattern(ctx, pattern, *, response):
    guild_id = ctx.guild.id
    learned_patterns[guild_id].append((pattern, response))
    await ctx.send(f"Okay, I've learned to respond to '{pattern}' with '{response}' in this server.")

if __name__ == "__main__":
    bot.run(TOKEN)