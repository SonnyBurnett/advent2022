
def colored(r, g, b, text):
    return "\033[7m\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(r, g, b, text)

def red(text):
    return colored(255,0,0,text)

def green(text):
    return colored(0, 153,0, text)

def blue(text):
    return colored(102, 204, 255, text)

def yellow(text):
    return colored(103, 102, 100, text)

def purple(text):
    return colored(204, 0,204, text)

def darkred(text):
    return colored(204, 0,0, text)

def orange(text):
    return colored(255, 153, 0, text)

def browne(text):
    return colored(153, 102, 51, text)

def rose(text):
    return colored(255, 204, 255, text)

def darkblue(text):
    return colored(0, 0, 255, text)

def oldpink(text):
    return colored(204, 102, 153, text)


def colorprint(tekst, num):
    if num == 0:
        return red(tekst)
    elif num == 1:
        return green(tekst)
    elif num == 2:
        return oldpink(tekst)
    elif num == 3:
        return blue(tekst)
    elif num == 4:
        return darkblue(tekst)
    elif num == 5:
        return purple(tekst)
    elif num == 6:
        return darkred(tekst)
    elif num == 7:
        return orange(tekst)
    elif num == 8:
        return browne(tekst)
    elif num == 9:
        return rose(tekst)
    elif num == 10:
        return yellow(tekst)
    else:
        return "\033[0m"
