Snipe-bot-Antispam
Needs `Manage Messages` for the bot

delete messages that not contain lat/long
So message for `spottings` need to be in this format
```
pokemon_name lat/long IV 
```
any order or the messages will be deleted


Requirements

- Python 3.4.2+
- `aiohttp` library
- `websockets` library
- `PyNaCl` library (optional, for voice only)


Getting Started
```bash
git clone git@github.com:Navyguy330/Snipe-bot-Antispam.git
cd Snipe-bot-Antispam
pip3 install -r requirements.txt
cp config.json.sample config.json
```
Put your `api_key` in `config.json` and modify your channel name

start the bot
```bash
python3 bot.py
```
