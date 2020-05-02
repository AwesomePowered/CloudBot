from cloudbot import hook
from cloudbot.util import http
import json

yes_prefix=u"\x02\x0f"
yes_suffix=u": \x033\x02\u2611\ufe0f"
no_prefix=u"\x02\x0f"
no_suffix=u": \x034\x02\U0001F6AB"

@hook.command()
def mojang():

    try:
        request = http.get("http://status.mojang.com/check")
    except (http.URLError, http.HTTPError) as e:
        return "Unable to get Minecraft server status: {}".format(e)

    # lets just reformat this data to get in a nice format
    data = json.loads(request.replace("}", "").replace("{", "").replace("]", "}").replace("[", "{"))

    # use a loop so we don't have to update it if they add more servers
    servers = []
    for server, status in data.items():
        if server == "account.mojang.com":
            server = "MJ|Account"
        elif server == "skins.minecraft.net":
            server = "MC|Skins"
        elif server == "auth.mojang.com":
            server = "MJ|Auth"
        elif server == "authserver.mojang.com":
            server = "MJ|AuthServer"
        elif server == "login.minecraft.net":
            server = "MC|Login"
        elif server == "session.minecraft.net":
            server = "MC|Session"
        elif server == "minecraft.net":
            server = "MC|Website"
        elif server == "sessionserver.mojang.com":
            server = "MJ|Session"
        elif server == "api.mojang.net":
            server = "MJ|API"
        elif server == "textures.minecraft.net":
            server = "MC|Textures"

        if status == "green":
            servers.append(u"{}{}{}".format(yes_prefix, server, yes_suffix))
        else:
            servers.append(u"{}{}{}".format(no_prefix, server, no_suffix))

    return "  ".join(servers)
