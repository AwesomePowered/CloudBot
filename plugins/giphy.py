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
        return "Could search for gif"

    gifId = json.loads(req.text)["data"]["id"]

    gifUrl = "http://i.giphy.com/"+gifId+".gif"

    return "Here is your gif " + gifUrl
