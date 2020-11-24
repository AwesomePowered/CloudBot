from cloudbot import hook
import urllib.request as urlr
import json, datetime

api_next = "https://api.spacexdata.com/v4/launches/next"
api_rocket = "https://api.spacexdata.com/v4/rockets/"
api_launchpad = "https://api.spacexdata.com/v4/launchpads/"


def getTimeLeft(timestamp):
    delta = datetime.datetime.fromtimestamp(timestamp) - datetime.datetime.now()
    return "{} days {} hours {} minutes".format(delta.days, delta.seconds//3600 % 24, delta.seconds // 60 % 60)

def getJson(api_link):
    data = urlr.urlopen(api_link).read().decode("utf-8")
    return json.loads(data)

@hook.command()
def spacex(bot):
    launch = getJson(api_next)
    return "A SpaceX {} is scheduled to launch {} from {} in {}".format(getJson(api_rocket+launch["rocket"])["name"], launch["name"], getJson(api_launchpad+launch["launchpad"])["name"], getTimeLeft(launch["date_unix"]))
