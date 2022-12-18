import discord
import dotenv
import os
import league_match_service


dotenv.load_dotenv()
BOT_TOKEN = os.environ.get("BOT_TOKEN")


async def send_latest(message):
    latest_match_id = league_match_service.get_latest_match_id()
    response = league_match_service.get_match_data_by_id(latest_match_id)
    try:
        await message.channel.send(response)
    except Exception as e:
        print(e)


async def send_angry(message):
    response = "Daddy Burke is angry"
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

    client.run(BOT_TOKEN)
