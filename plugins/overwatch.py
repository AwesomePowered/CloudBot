"""
overwatch.py

Check's a players competitive stats.

Created By:
    - LaxWasHere <https://github.com/LaxWasHere> for the sole purpose of showing spottedleaf that he's still plat

License:
    GPL v3
"""

from cloudbot import hook
import requests
import json

@hook.command("owstats", "owrank")
def owrank(text,bot,notice):
    """ Check a persons overwatch rank .owstats battle#id [us,eu,kr]"""

    split = text.split()
    if len(split) > 2:
        notice("Too many arguments")
        return
    elif len(split) < 2:
        notice("Battle#Tag [us,eu,kr]")
        return

    battletag = split[0]
    region = split[1].lower()

    url = "https://owapi.net/api/v3/u/{}/blob".format(battletag.replace("#","-"))
    notice("Requesting stats, please hold on.")

    try:
        req = requests.get(url,headers={'User-Agent': bot.user_agent})
        req.raise_for_status()
    except (requests.exceptions.HTTPError, requests.exceptions.ConnectionError) as e:
        return "Could not find stats"

    if json.loads(req.text)[region] is not None:
        compstats = json.loads(req.text)[region]["stats"]["competitive"]["overall_stats"]
    else:
        return "Could not find stats for that region"

    rank = str(compstats["comprank"]) #TypeError my ass
    tier = compstats["tier"]
    wins = str(compstats["wins"])
    losses = str(compstats["losses"])
    draws = str(compstats["ties"])
    wr = str(compstats["win_rate"])

    return text + " is currently ranked " + tier.title() + " at " + rank + " " + wins+"W/"+losses+"L/"+draws+"D" + " WinRate: " + wr
