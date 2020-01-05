from cloudbot import hook
import urllib.request as urlr
import json, datetime

link = "https://api.spacexdata.com/v3/launches/next"


def getTimeLeft(timestamp):
    delta = datetime.datetime.fromtimestamp(timestamp) - datetime.datetime.now()
    return "{} days {} hours {} minutes".format(delta.days, delta.seconds//3600 % 24, delta.seconds // 60 % 60)


@hook.command()
def spacex(bot):
    data = urlr.urlopen(link).read().decode("utf-8")
    newdata = json.loads(data)
    return "A {} is scheduled to launch {} from {} in {}".format(newdata["rocket"]["rocket_name"], newdata["mission_name"] newdata["launch_site"]["site_name"], getTimeLeft(newdata["launch_date_unix"]))
