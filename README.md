# 🤖 Discord Automation Bot

A modular, production-ready Discord bot built with discord.py.

---

## 🚀 Features

- ⚡ Modular cog system
- 🛡️ Moderation commands (kick, ban)
- 🧠 Easy to extend architecture
- 🪵 Logging system
- 🔐 Secure token handling (.env)

---

## ⚙️ Setup

### 1. Clone repo
git clone https://github.com/yourusername/discord-automation-bot.git
cd discord-automation-bot

---

### 2. Create virtual environment

Windows:
python -m venv venv
venv\Scripts\activate

Mac/Linux:
python3 -m venv venv
source venv/bin/activate

---

### 3. Install dependencies
pip install -r requirements.txt

---

### 4. Setup environment
Rename `.env.example` → `.env`

Add your bot token:
DISCORD_TOKEN=your_token_here

---

### 5. Run bot
python main.py

---

## 🧠 Commands

!ping → test bot latency  
!kick @user → kick member (admin only)  
!ban @user → ban member (admin only)

---

## 📁 Architecture

- bot.py → core bot logic
- cogs/ → modular features
- config.py → environment management
- logger.py → logging system

---

## 🔥 Future upgrades

- Ticket system
- Slash commands (/)
- Database integration (SQLite/PostgreSQL)
- Web dashboard
- Auto moderation (anti-spam)

---

## ⭐ License

Free for personal and commercial use.
