import discord
import asyncio
import threading

TOKEN = "ENTER_YOUR_BOT_TOKEN_HERE"
CHANNEL_ID = 123456789012345678  # replace with your channel ID

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f"[+] Logged in as {client.user}")
    channel = client.get_channel(CHANNEL_ID)

    if channel is None:
        print("[-] Channel not found. Check CHANNEL_ID.")
        return

    print("[*] Type messages below. CTRL+C to exit.\n")

    def cmd_input():
        while True:
            try:
                msg = input("> ")
                asyncio.run_coroutine_threadsafe(
                    channel.send(msg),
                    client.loop
                )
            except EOFError:
                break

    threading.Thread(target=cmd_input, daemon=True).start()

try:
    client.run(TOKEN)
except KeyboardInterrupt:
    print("\n[!] Bot shutting down.")
