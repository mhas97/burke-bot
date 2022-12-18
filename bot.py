import discord
import dotenv
import os


dotenv.load_dotenv()
BOT_TOKEN = os.environ.get("BOT_TOKEN")


async def send_angry(message):
    try:
        response = "Daddy Burke is angry"
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

    client.run(BOT_TOKEN)
