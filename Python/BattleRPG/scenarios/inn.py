import math

from class_library.engine import *
from items.potions import *

Stock = {
    "Health Potion": StockItem("Health Potions", 5, HealthPotion),
    "Mana Potion": StockItem("Mana Potions", 5, ManaPotion)
}


def inn(player: Player):
    while True:
        choice = Menu("Actions", "Buy drink(s)", "Rest", "Leave")
        if choice == 1:
            buy_from_stock(player, Stock, "Inn")
        elif choice == 2:
            inn_rest(player)
        elif choice == 3:
            break


def inn_rest(player: Player):
    player.hp = player.max_hp
    print("You rest at the Inn and are healed to full health, you heath is now",
          colorText(player.hp, BColors.GREEN) + "!")
