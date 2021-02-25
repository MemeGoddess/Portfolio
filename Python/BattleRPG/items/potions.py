from class_library.engine import *


class HealthPotion(Item):
    name = "Health Potion"
    sell_price = 2
    description = "Restores 250 health on the user"

    def use_item(self, user: Living):
        user.mod_health(250)
        return "Healed for 250, health is now " + colorText(user.hp, BColors.GREEN) + "!"


class ManaPotion(Item):
    name = "Mana Potion"
    sell_price = 2
    description = "Restores 100 mana on the user"

    def use_item(self, user: Living):
        user.mod_resource(100)
        return "Restored 100 mana, mana is now " + colorText(user.mp, BColors.BLUE) + "!"