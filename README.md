# Your First Discord Bot (Python)

This is a **terminal-controlled Discord bot** built using **discord.py**.  
You type messages in your terminal → the bot sends them to a specific Discord channel.

No slash commands. No UI.  
Just raw terminal → Discord energy.

---

## What This Bot Template Does

- Logs in as a Discord bot
- Connects to a specific channel
- Lets **you type messages in your terminal**
- Instantly sends them to that Discord channel
- Runs input handling in a separate thread (so Discord doesn’t freeze)

---

## Project Structure

```
discord-terminal-bot/
│
├── bot.py          # main bot code
├── README.md       # you are here
└── requirements.txt
```

---

## Requirements

- Python **3.9+** (recommended)
- A Discord account
- A Discord server where you have **Admin / Manage Server**
- Internet connection (obviously)

---

## Install Dependencies

Create a virtual environment (optional but based):

```bash
python -m venv venv
source venv/bin/activate   # Linux / macOS
venv\Scripts\activate    # Windows
```

Install `discord.py`:

```bash
pip install -U discord.py
```

Or create `requirements.txt`:

```txt
discord.py
```

Then:

```bash
pip install -r requirements.txt
```

---

## Step-by-Step: Create Your Own Discord Bot

### Go to Discord Developer Portal

 https://discord.com/developers/applications

- Click **New Application**
- Give it a name
- Create it

---

### Create a Bot User

- Go to **Bot** tab
- Click **Add Bot**
- Confirm

⚠️ **COPY THE BOT TOKEN**
- Click **Reset Token**
- Copy it
- **DO NOT SHARE IT**
- Treat it like a password

---

### Enable Required Intents

In the **Bot** section, enable:

- ✅ Message Content Intent

Save changes.

---

### Invite the Bot to Your Server

Go to **OAuth2 → URL Generator**

**Scopes:**
- ☑ bot

**Bot Permissions:**
- ☑ Send Messages
- ☑ Read Message History

Copy the generated URL → open it in browser → invite bot to your server.

---

## Get Your Channel ID

1. Discord → Settings → Advanced
2. Enable **Developer Mode**
3. Right-click a channel → **Copy ID**

---

## Run the Bot

```bash
python bot.py
```

If everything is correct, you’ll see:

```
[+] Logged in as BotName#1234
[*] Type messages below. CTRL+C to exit.
>
```

Now type anything → it appears in Discord.

---

## How It Works (Quick Explanation)

- `discord.Client()` connects to Discord
- `on_ready()` runs once the bot logs in
- A **separate thread** handles terminal input
- Messages are sent safely to the Discord event loop using:
  ```python
  asyncio.run_coroutine_threadsafe()
  ```

This avoids blocking Discord’s async loop.

---

## ⚠️ Common Errors & Fixes

### ❌ Bot logs in but sends nothing
- Wrong `CHANNEL_ID`
- Bot not in that server
- Missing permissions

### ❌ Privileged intent error
- Message Content Intent not enabled in Dev Portal

### ❌ Token invalid
- Token copied wrong
- Token regenerated → update code

---

## Security Notes (Read This)

- ❌ Never commit your bot token
- ❌ Never paste it in screenshots
- ✅ Use environment variables for production

Example:

```python
import os
TOKEN = os.getenv("DISCORD_TOKEN")
```

---

## Ideas to Extend This Bot

- Add command parsing (`!ping`, `!say`)
- Log messages to a file
- Turn it into a remote admin console
- Build a C2-style controller (educational 👀)
- Add slash commands
- Encrypt terminal input

---

## Final Words

This bot is **minimal**, **clean**, and **powerful**.
Perfect for:
- Learning async Python
- Understanding Discord bots
- Building automation tools

Break it. Modify it. Own it.

🔥 Happy ethical hacking.
