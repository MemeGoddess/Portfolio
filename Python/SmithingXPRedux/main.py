import math

import colorama
from colorama import Fore, Style


def colorText(text: object, color: object) -> str:
    return str("".join(color) + str(text) + Style.RESET_ALL)


def Menu(title: str, *entries):
    i = 1
    if title is not "":
        print(colorText(title, Fore.GREEN))
    for item in entries:
        print(str(i) + ":", str(item.name))
        i += 1

    userInput = input("> ")
    while True:
        try:
            userInput = int(userInput)
            if not 1 <= userInput <= (i - 1):
                raise ValueError
            break
        except ValueError:
            userInput = input("> ")
    print()
    return int(userInput)


def readNum(prompt: str):
    userInput = input(prompt + ": ")
    while True:
        try:
            userInput = int(userInput)
            break
        except ValueError:
            userInput = input(prompt + ": ")
    return userInput


def readDouble(prompt: str):
    userInput = input(prompt + ": ")
    while True:
        try:
            userInput = float(userInput)
            break
        except ValueError:
            if userInput == "":
                return 1.0
            userInput = input(prompt + ": ")
    return userInput


class TierInfo:
    def __init__(self, name: str, xpPerBar: int, barsPerBurial: int, xpPerBurial: int):
        self.name = name
        self.xpPerBar = xpPerBar
        self.barsPerBurial = barsPerBurial
        self.xpPerBurial = xpPerBurial


colorama.init()
tiers = [TierInfo("Bronze", 16, 0, 0),
         TierInfo("Iron", 42, 0, 0),
         TierInfo("Steel", 78, 0, 0),
         TierInfo("Mithril", 125, 0, 0),
         TierInfo("Adamant", 177, 48, 4080),
         TierInfo("Rune", 250, 96, 11520),
         TierInfo("Orikalkum", 363, 96, 16800),
         TierInfo("Necronium", 517, 192, 48000),
         TierInfo("Bane", 721, 192, 67200),
         TierInfo("Elder Rune", 1026, 384, 192000)]

Choice = Menu("Choose tier", *tiers) - 1
# Type = Menu("Choose mode", "Total XP Needed", "Level Range", "Level Range (Character)")
xp = readNum("Enter how much xp you want")
multiplier = readDouble("What is your xp multiplier, press enter for 1.00")

tierItem = tiers[Choice]
tierItem.xpPerBar *= multiplier
tierItem.xpPerBurial *= multiplier
if tierItem.barsPerBurial == 0:
    totalBars = math.ceil(xp / tierItem.xpPerBar)
    burials = 0
    leftOverBars = 0
else:
    totalXpPerBurial = tierItem.barsPerBurial * tierItem.xpPerBar + tierItem.xpPerBurial
    burials = math.floor(xp / float(totalXpPerBurial))
    leftOver = xp - (burials * totalXpPerBurial)
    leftOverBars = math.ceil(leftOver / tierItem.xpPerBar)
    if leftOverBars >= tierItem.barsPerBurial:
        burials += 1
        leftOver = xp - (burials * totalXpPerBurial)
        leftOverBars = math.ceil(leftOver / tierItem.xpPerBar)
        if leftOverBars < 0:
            leftOverBars = 0
    totalBars = burials * tierItem.barsPerBurial + leftOverBars


if leftOverBars > 0:
    print("In order to get", xp, "xp, you will need a total of", totalBars, "bars. " +
          "You will make", burials, "burials and", leftOverBars, "of any gear.")
elif burials > 0:
    print("In order to get", xp, "xp, you will need a total of", totalBars, "bars. " +
          "You will make", burials, "burial sets.")
else:
    print("In order to get", xp, "xp, you will need a total of", totalBars, "bars.")
while True:
    input("")




