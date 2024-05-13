from colorama import init
from colorama import Fore, Back, Style
from disnake.ext import commands
import importlib
# import caching
import time
import json
import sys
import os

import disnake

init()

helpp = "{{ action.reply(context, \"Hey, it\\\'s pynjaDS Bot!\") }}"

config = """{
    \"token\": \"YOUR TOKEN\",
    \"commands_prefix\": \"!\"
}"""

handler = """{
    \"events\": [
        {
            \"event\": \"prefix_command\",
            \"data\": \"help\",
            \"path\": \"help.j2\"
        }
    ]
}"""

static = """{
    \"events\": [
        {
            \"static\": \"slash_command\",
            \"data\": \"example\",
            \"path\": \"static_example.j2\"
        }
    ]
}"""
# LOAD

if not os.path.exists("config.json"):
    print("creating config.json")

    with open("config.json", "w") as file:
        file.write(config)

if not os.path.exists("eventshandler.json"):
    print("creating eventshandler.json")

    with open("eventshandler.json", "w") as file:
        file.write(handler)

if not os.path.exists("statichandler.json"):
    print("creating statichandler.json")

    with open("statichandler.json", "w") as file:
        file.write(static)

if not os.path.isdir('scripts'):
    print("creating scripts directory")
    os.mkdir("scripts")
    print("creating help.j2")

    with open("scripts/help.j2", "w") as file:
        file.write(helpp)

if not os.path.isdir('extensions'):
    print("creating extensions directory")
    os.mkdir("extensions")


f = open("config.json", "r")
jsondump = json.load(f)
f.close()

f = open("statichandler.json", "r")
staticload = json.load(f)["events"]
f.close()

if jsondump["token"] == "YOUR TOKEN":
    print("Change bot token in config.json!")
    time.sleep(3)
    sys.exit(0)

BOT = commands.Bot(command_prefix=";", intents=disnake.Intents.all())
#shashed_funcs = caching.cache_slashcommands(staticload) <<< SOON

# TODO: Slash commands by using exec

# for num, event in enumerate(staticload):
#     BOT.slash_command(name=event["name"], description=event["description"])(shashed_funcs[f"slash_cached{num}"])
#     print(f"loaded /{event["name"]}")

os.system('cls')

print(Fore.BLUE + "py" + Fore.LIGHTYELLOW_EX + "nja" + Fore.MAGENTA + " Discord" + Fore.WHITE)

BOT.remove_command("help")
BOT.load_extension("disnakebot")
BOT.run(token=jsondump["token"])