import openai
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
openai_api = open('openaiapikey.txt')
openai.api_key = openai_api.read()
discord_api = open('discordapikey.txt')
DISCORD_TOKEN = discord_api

intents = discord.Intents(messages=True, guilds=True)
intents.message_content = True
intents.typing = False
intents.presences = False

bot = commands.Bot(command_prefix="!", intents=intents)


async def gpt_response(prompt):
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.5,
        max_tokens=500,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    return completion.choices[0].message.content


@bot.event
async def on_ready():
    guild_count = 0
    for guild in bot.guilds:
        print(f"Online in:\nServer ID: {guild.id} (Name: {guild.name})")
        guild_count = guild_count + 1
    print("ChatGPT is in " + str(guild_count) + " guilds.")


@bot.command(name="gpt")
async def gpt(ctx, *, prompt: str):
    response = await gpt_response(prompt)
    await ctx.send(response)

bot.run(discord_api.read())
