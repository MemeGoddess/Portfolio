from items.mage_equipment import Wand
from scenarios.battle import do_battle
from scenarios.change_equipment import change_equipment
from scenarios.dungeons.first_dungeon import FirstDungeon
from scenarios.inn import *
from scenarios.shop import *

title = "BattleRPG"
version = 0.1

# TODO Convert this to a database, with skill levels. Also, add descriptions to spells
magic = [Spell("Fire", 10, 50, 70),
         Spell("Thunder", 15, 60, 80),
         Spell("Blizzard", 20, 100, 120),
         Spell("Regenerate Mana", -50, 0, 0)]
enemyMagic = [Spell("Bite", 0, 5, 15)]

player = Player(500, 100, 60, 34, magic)
player.equipment[6] = Wand()
wand2 = Wand()
wand2.name = "Mage's Backup Wand"
player.inventory.append(wand2)
player.gold = 10
print("Welcome to", title, "v" + str(version) + "!")
running = True
while running:
    print("You are in town, what would you like to do?")

    userInput = Menu("Locations", "Go to the Inn", "Visit the Shop", "Fight at the Arena", "Explore a Dungeon", "Change your equipment")
    if userInput == 1:
        inn(player)
    elif userInput == 2:
        shop()
    elif userInput == 3:
        do_battle(player, Living(750, 0, 5, 0, 0, 0))
    elif userInput == 4:
        FirstDungeon().enter(player)
    elif userInput == 5:
        change_equipment(player)
