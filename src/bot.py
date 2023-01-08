'''Checks any messages for a bot-command and executes the assiciated action'''
import discord
import dotenv
import os
import random
import src.league_service as league_service


dotenv.load_dotenv()
BOT_TOKEN = os.environ.get("BOT_TOKEN")


async def help(message):
    '''Lists available commands'''
    response = "Currently supported commands ```\n.burke-help\n.latest\n.never\n.angry\n.champ-[role]\n.action```"
    try:
        await message.channel.send(response)
    except Exception as e:
        print(e)


async def send_latest(message):
    '''Fetches the latest result for a player and outputs their stats'''
    response = league_service.get_latest_match_bot_string()
    try:
        await message.channel.send(response)
    except Exception as e:
        print(e)


async def send_angry(message):
    '''Randomly selects and outputs an anger level'''
    anger = random.randint(0, 100)
    response = f"Player is {anger}% angry"
    try:
        await message.channel.send(response)
    except Exception as e:
        print(e)


async def send_action(message):
    '''Sends a random league action'''
    actions = ["tower-dive", "all in", "recall", "flame team", "flame opponent",
               "invade", "force drag", "force nash", "roam mid", "roam bot", "buy a pink ward"]
    action = random.choice(actions)
    response = f"Player should {action}"
    try:
        await message.channel.send(response)
    except Exception as e:
        print(e)


async def send_champion(message):
    '''Selects a random champion from a user-provided role'''
    role = str(message.content[7:])
    top = ["Kled", "Shaco", "Singed"]
    jungle = ["Zac", "Shaco"]
    mid = ["Malzahar", "Kled", "Shaco", "Galio"]
    if role == "top":
        role_arr = top
    elif role == "jungle":
        role_arr = jungle
    else:
        role_arr = mid
    champion = random.choice(role_arr)
    response = f"Player should play {champion} {role}"
    try:
        await message.channel.send(response)
    except Exception as e:
        print(e)


async def send_has_never(message):
    '''Sends a random has-never action'''
    never_list = ["had a double kill", "achieved 6cs per minute", "intentionally outplayed someone",
                  "bought a mythic item", "unlocked his camera", "successfully recalled", "taken a tower", "landed a skillshot", "used a pink ward", "predicted a flash"]

    never_choice = random.choice(never_list)
    response = f"Player has never {never_choice}"
    try:
        await message.channel.send(response)
    except Exception as e:
        print(e)


def run_discord_bot():
    '''Runs the discord bot and listens for messages'''
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

        message_content = str(message.content).lower()

        if message_content == ".burke-help":
            await help(message)

        if message_content == ".angry":
            await send_angry(message)

        if message_content == ".latest":
            await send_latest(message)

        if message_content == ".action":
            await send_action(message)

        if message_content in [".champ-top", ".champ-jungle", ".champ-mid"]:
            await send_champion(message, )

        if message_content == ".never":
            await send_has_never(message)

    client.run(BOT_TOKEN)
