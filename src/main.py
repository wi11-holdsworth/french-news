import discord
import os
from utils import fetch_entries, entry_to_msg
from inputs import SOURCES
from dotenv import load_dotenv

load_dotenv()


class MyClient(discord.Client):

    # TODO: this technically can run more than once, is this going to be
    # a problem?

    async def on_ready(self):
        print(f"Logged in as {self.user} (ID: {self.user.id})")
        print("------")

        self.channel = self.get_channel(int(os.getenv("CHANNEL_ID")))
        self.guild = self.get_guild(int(os.getenv("GUILD_ID")))
        self.role = discord.utils.get(self.guild.roles, name=os.getenv("ROLE"))

        await self.channel.send(f"Voici les nouvelles {self.role.mention}!")

        for name, opts in SOURCES.items():

            # fetch the entries from the source

            entries: list[dict] = fetch_entries(opts["url"])
            max_entries: int = min(len(entries), opts["max_fetch"])

            # first tell the viewer the source

            await self.channel.send(f"# 🌐 {name}")

            # now display all the entries

            for entry in entries[:max_entries]:
                await self.channel.send(entry_to_msg(entry))

        # TODO: can we kill less violently?

        exit(0)


client = MyClient(intents=discord.Intents.default())
client.run(os.getenv("BOT_TOKEN"))
