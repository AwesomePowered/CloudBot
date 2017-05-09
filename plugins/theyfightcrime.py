from cloudbot import hook
from cloudbot.util import http

@hook.command()
def plot():
    bold = "\x02"
    try:
        soup = http.get_soup("http://www.theyfightcrime.org")
        plot = soup.find('table').find('p').text
        return bold + plot + bold
    except:
        return "Could not get plot."
