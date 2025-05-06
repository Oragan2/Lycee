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

async def handle_greeting(message, author):
    greetings_en = r"(hello|hi|hey|greetings|good morning|good evening|good afternoon|sup)\b"
    greetings_fr = r"(bonjour|salut|coucou|bonne journée|bonsoir)\b"
    if re.search(greetings_en, message, re.IGNORECASE):
        return f"Hello {author.mention}!"
    elif re.search(greetings_fr, message, re.IGNORECASE):
        return f"Bonjour {author.mention} !"
    return None

async def handle_weather_request(message):
    weather_pattern = r"(what's the weather like in|weather in|temperature in)\s+(?P<city>\w+)"
    match = re.search(weather_pattern, message, re.IGNORECASE)
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
    if re.search(joke_pattern, message, re.IGNORECASE):
        jokes = [
            "Why don't scientists trust atoms? Because they make up everything!",
            "Parallel lines have so much in common... it’s a shame they’ll never meet.",
            "Why did the scarecrow win an award? Because he was outstanding in his field!"
        ]
        import random
        return random.choice(jokes)
    return None

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

    responses = []
    for msg in message.content.split(". "):
        intents = 'unknow'
        greeting_response = await handle_greeting(msg, message.author)
        if greeting_response:
            responses.append(greeting_response)
            intents = 'greeting'

        weather_response = await handle_weather_request(msg)
        if weather_response:
            responses.append(weather_response)
            intents = 'get_weather'

        joke_response = await handle_joke_request(msg)
        if joke_response:
            responses.append(joke_response)
            intents = 'demand_joke'

        with open("intent_data.txt","a") as file:
            file.write(f"{message.author}:{msg}\t{intents}\n")

    if responses and (bot.user.mentioned_in(message) or "memo" in message.content.lower()):
        await message.channel.send("\n".join(responses))

if __name__ == "__main__":
    bot.run(TOKEN)