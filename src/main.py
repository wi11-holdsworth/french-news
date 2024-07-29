import discord
import os
import time
from utils import fetch_entries, entry_to_msg
from constants import SOURCES
from dotenv import load_dotenv

load_dotenv()


class MyClient(discord.Client):
    async def on_ready(self):
        print(f"Logged in as {self.user} (ID: {self.user.id})")
        print("------")

        self.channel = self.get_channel(1267471756604739665)

        for name, opts in SOURCES.items():
            # try to avoid getting rate-limited

            time.sleep(3)

            # fetch the entries from the source

            entries: list[dict] = fetch_entries(opts["url"])
            max_entries: int = min(len(entries), opts["max_fetch"])

            # first tell the viewer the source

            await self.channel.send(f"# 🌐 {name}")

            # now display all the entries

            for entry in entries[:max_entries]:
                for msg in entry_to_msg(entry):
                    await self.channel.send(msg)

        # all done!

        await self.channel.send("goodbye until next time!")

        # TODO: can we kill less violently?

        exit(0)


intents = discord.Intents.default()

client = MyClient(intents=intents)
client.run(os.getenv("BOT_TOKEN", ""))
