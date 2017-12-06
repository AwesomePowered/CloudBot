from cloudbot import hook
import requests
import json


@hook.command("gif","giphy")
def randomgif(text, bot):
    "Searches for a random gif"

    url = "http://api.giphy.com/v1/gifs/random?api_key=dc6zaTOxFJmzC&tag={}".format(text.replace(" ", "+"))

    try:
        req = requests.get(url, headers={"User-Agent": bot.user_agent})
        req.raise_for_status()
    except (requests.exceptions.HTTPError, requests.exceptions.ConnectionError) as e:
        return "Could not search for gif"

    data = json.loads(req.text)

    if not data["data"]:
        return "'" + text + "' not found."
    else:

        url = "http://i.giphy.com/" + data["data"]["id"] + ".gif"

        return url
