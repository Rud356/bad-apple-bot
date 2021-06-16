# Bad Apple bot!

This is a fork of this repository: https://github.com/NPCat/bad-apple-bot

I've improved code readability, added a bit of configurability and better install guide.

## How to install

Pre-requirements:
- python3 (will be called `python` in commands here)
- pip (pip for python3)
- virtualenv with python3 (if you want to have it - see this: https://virtualenv.pypa.io/en/latest/user_guide.html)
- see guide on how to set up bots for your server (https://realpython.com/how-to-make-a-discord-bot-python/)
  and obtain its token

### From repository
1. Clone repository
2. run `cd bad-apple-bot`
  and activate virtualenv if you have it (see guides)
3. run `pip install -r requirements.txt`
4. run `python start.py`
5. You must see error that says to edit config - that's okay, check next step
6. Move to bot/config and open config.json, then edit line `"token": "DISCORD_TOKEN"` by replacing
  `DISCORD_TOKEN` with previously copied token
7. Get back to repository root and run `python start.py` again
8. enjoy
