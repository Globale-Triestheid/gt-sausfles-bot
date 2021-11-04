import discord
import mysql.connector
from database import DiscordDB

TOKEN = ""
client = discord.Client()

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="globaletriestheid"
)

discordDB = DiscordDB(client, db)


@client.event
async def on_message(message):
    author = message.author
    channel = message.channel

    if not discordDB.check_user(author.id):
        discordDB.insert_user(author.id)

    if not discordDB.check_channel(author.id):
        discordDB.insert_channel(channel.id)

    discordDB.update_user(author.id, author.name + "#" + author.discriminator)

    discordDB.update_channel(channel.id, channel.__str__())

    discordDB.insert_message(message)

    if message.channel.__str__() == "first_letter_last_letter":
        if message.content.lower() != "sausfles":
            await message.delete()


if __name__ == "__main__":
    client.run(TOKEN)
