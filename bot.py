import discord
import dotenv
import os
import league_service
import random


dotenv.load_dotenv()
BOT_TOKEN = os.environ.get("BOT_TOKEN")


async def send_latest(message):
    response = league_service.get_latest_match_bot_string()
    try:
        await message.channel.send(response)
    except Exception as e:
        print(e)


async def send_angry(message):
    anger = random.randint(0, 100)
    response = f"Daddy Burke is {anger}% angry"
    try:
        await message.channel.send(response)
    except Exception as e:
        print(e)


async def send_action(message):
    actions = ["tower-dive", "all in", "recall", "flame team", "flame opponent",
               "invade", "force drag", "force nash", "roam mid", "roam bot", "buy a pink ward"]
    action = random.choice(actions)
    response = f"Burke should {action}"
    try:
        await message.channel.send(response)
    except Exception as e:
        print(e)


def run_discord_bot():
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f"{client.user} is now running")

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        if str(message.content) == ".angry":
            await send_angry(message)

        if str(message.content) == ".latest":
            await send_latest(message)

        if str(message.content) == ".action":
            await send_action(message)

    client.run(BOT_TOKEN)
