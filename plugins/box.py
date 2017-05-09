import asyncio
from cloudbot import hook

@asyncio.coroutine
@hook.command
def box(text, message):
    """box <word> - Produces le box maymays"""
    if len(text) > 9:
        return "No."
    for i in range(0,len(text)):
        output = ""
        if i == 0:
            for l in text:
                output += "{} ".format(l)
        elif i == len(text) - 1:
            for l in text[::-1]:
                output += "{} ".format(l)
        else:
            output += "{} ".format(text[i])
            for maymay in range(0,len(text) - 2):
                output += "  "
            output += text[len(text) - 1 - i]
        message(output)
