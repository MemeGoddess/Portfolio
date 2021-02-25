import re
import string

from class_library.engine import *
from class_library.linq import *
from item_types.equipment import *
from item_types.weapon import Weapon


def change_equipment(player: Player):
    while True:
        choice = Menu("Choose gear slot", *make_gear_list(player), "Back")
        if choice == 9:
            break
        gearList = get_equipment_by_slot(player, EquipmentSlot(choice - 1))
        if len(gearList) > 0:
            choiceGear = Menu("Choose gear to equip", *get_description_from_list(player, gearList), "Back")
            if choiceGear == len(gearList) + 1:
                continue
            print(choice - 1)
            print(player.equipment)
            player.inventory.append(player.equipment[choice - 1])
            newItem = gearList[choiceGear - 1]
            player.inventory.remove(newItem)
            player.equipment[choice - 1] = newItem
        else:
            print("You have no gear for that slot.")


def make_gear_list(player: Player):
    gearList = [None] * len(player.equipment)
    for x in range(len(player.equipment)):
        gearList[x] = string.capwords(re.sub('_', '-', EquipmentSlot(x).name)) + " > "
        if isinstance(player.equipment[x], Equipment):
            gearList[x] += player.equipment[x].name
        else:
            gearList[x] += "None"
    return gearList


def get_equipment_by_slot(player: Player, slot: EquipmentSlot):
    return list(Where(player.inventory, lambda x: issubclass(type(x), Weapon) and x.slot == slot))


def get_description_from_list(player: Player, gear):
    gearDesc = [str] * len(gear)
    for x in range(len(gear)):
        desc = gear[x].description
        gearDesc[x] = str(gear[x].name)
        if desc != "":
            gearDesc[x] += " - " + desc
    return gearDesc
