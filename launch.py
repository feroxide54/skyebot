import discord
import os


class BotClient(discord.Client):
    async def on_ready(self):
        print("Logged on as {0}!".format(self.user))

    async def on_message(self, message):
        if message.author == self.user:
            return
        else:
            print("Message from {0.author}: {0.content}".format(message))


client = BotClient()
token = os.environ["BOTTOKEN"]
client.run(token)
