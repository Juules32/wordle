from typing import Final
import os
from dotenv import load_dotenv
from discord import Intents, Client, Message
from responses import get_responses
from parsing import *

# Load local token
load_dotenv()
TOKEN: Final[str] = os.getenv('DISCORD_TOKEN')

# Setup bot
intents: Intents = Intents.default()
intents.message_content = True  # NOQA
bot: Client = Client(intents=intents)

# Handle bot startup
@bot.event
async def on_ready() -> None:
    print(f'{bot.user} is now running!')

# Handle incoming messages
@bot.event
async def on_message(message: Message) -> None:
    # Ignore irrelevant messages
    if message.author.bot or message.content[0] != '!':
        return

    # Remove '!' from message content
    message.content = message.content[1:]
    
    # Print message information
    username: str = str(message.author)
    user_message: str = message.content
    channel: str = str(message.channel)
    print(f'[{channel}] {username}: "{user_message}"')
    
    # Get responses asynchronously
    await get_responses(message)

# Run the bot
if __name__ == '__main__':
    bot.run(token=TOKEN)
