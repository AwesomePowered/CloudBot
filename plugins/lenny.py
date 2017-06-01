from cloudbot import hook
import requests, json


@hook.command()
def lenny():
    r = requests.get('http://lenny.today/api/v1/random')
    smile = json.loads(r.text)[0]['face']
    return smile
