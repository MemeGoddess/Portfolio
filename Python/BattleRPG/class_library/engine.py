import math
import random
from enum import Enum
from typing import List

from class_library.linq import Where, Select

# TODO Bosses with ability rotations
# TODO Melee builds rage
# TODO Range can only hold 25 arrows
# TODO Add a create-a-character screen, with a debug mode to use a pre-created version


class BColors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    STRIKE = '\u0336'
    BLACK = '\033[0;30;2m'
    RED = '\033[0;31m'
    GREEN = '\033[0;32m'
    YELLOW = '\033[0;33m'
    BLUE = '\033[0;34m'
    PURPLE = '\033[0;35m'
    CYAN = '\033[0;36m'
    WHITE = '\033[0;37m'


class StockItem:
    def __init__(self, plural, price, type):
        self.plural = plural
        self.price = price
        self.type = type


def colorText(text: object, color: object) -> str:
    return str("".join(color) + str(text) + BColors.ENDC)


def Menu(title: str, *entries):
    i = 1
    if title != "":
        print(colorText(title, BColors.BOLD))
    for item in entries:
        print(str(i) + ":", str(item))
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


def Quantity(title: str, min: int, max: int):
    print(title)
    userInput = input("> ")
    while True:
        try:
            userInput = int(userInput)
            if not min <= userInput <= max:
                raise ValueError
            break
        except ValueError:
            userInput = input("> ")
    print()
    return int(userInput)


class ItemEffects(Enum):
    DAMAGE = 0
    SPELL_DAMAGE = 1
    MANA = 2
    DEFENCE = 3
    USE = 4
    WIN = 5
    LOSE = 6


class Spell:
    def __init__(self, name: str, cost: int, min_damage: int, max_damage: int):
        self.name = name
        self.cost = cost
        self.min_damage = min_damage
        self.max_damage = max_damage


class Living:
    def __init__(self, hp: int, mp: int, atk: int, df: int, magic, escape_chance=50, name="Enemy"):
        self.max_hp = hp
        self.hp = hp
        self.max_mp = mp
        self.mp = mp
        self.atkl = atk - 5
        self.atkh = atk + 5
        self.df = df
        self.magic = magic
        self.name = name

        self.alive = True
        self.escape_chance = escape_chance
        self.inventory = []
        self.equipment = [None] * 8
        self.gold = 0
        self.has_used_item = False

    def mod_health(self, amount: int):
        self.hp += amount
        if self.hp > self.max_hp:
            self.hp = self.max_hp
        elif self.hp < 0:
            self.hp = 0

    def mod_resource(self, amount: int):
        self.mp += amount
        if self.mp > self.max_mp:
            self.mp = self.max_mp
        elif self.mp < 0:
            self.mp = 0

    def generate_damage(self):
        return random.randrange(self.atkl, self.atkh)

    def generate_spell_damage(self, spell: Spell):
        stat_spell_damage = self.get_equipment_stat("stat_spell_damage") + 1.0
        stat_mana_cost = 1.0 - self.get_equipment_stat("stat_mana_cost")
        self.mp -= int(spell.cost * stat_mana_cost)
        if spell.max_damage == 0:
            return 0;
        return int(random.randrange(spell.min_damage, spell.max_damage) * stat_spell_damage)

    def take_damage(self, damage: int):
        self.hp -= damage
        if self.hp < 0:
            self.alive = False
            self.hp = 0
        return self.hp

    def get_equipment_stat(self, stat: str):
        return sum(Select(list(Where(self.equipment, lambda x: x != None)), lambda x: getattr(x, stat)))

    def generate_info_bars(self):
        pass



class Item:
    quantity: int = 1
    name: str = ""
    sell_price: int = 0
    description: str = ""

    effects: List[ItemEffects] = []

    def __init__(self, quantity=1):
        self.quantity = quantity

    def use_item(self, user: Living):
        pass

    def passive_damage(self):
        pass

    def passive_mana(self):
        pass

    def passive_defence(self):
        pass

    def passive_win(self):
        pass

    def passive_lose(self):
        pass


class Player(Living):
    actions = ["Attack", "Magic", "Use Item", "Escape"]

    def choose_action(self):
        i = 1
        print(colorText("Actions", BColors.BOLD))
        for item in self.actions:
            print(str(i) + ":", item)
            i += 1

        userInput = input("> ")
        while True:
            try:
                userInput = int(userInput)
                break
            except ValueError:
                userInput = input("> ")
        return int(userInput)

    def choose_magic(self):

        menuList = []
        for item in self.magic:
            itemCost = str(item.cost)
            if item.cost < 0:
                itemCost = "+" + str(item.cost * -1)
            menuList.append(item.name + " (" + colorText(itemCost, BColors.BLUE) + ")")

        userInput = Menu("Spells", *menuList)

        return userInput

    def list_consumables(self):
        return list(Where(self.inventory, lambda x: isinstance(x, Item) and any(ItemEffects.USE in y for y in x.effects)))


def get_gold_text(living: Living):
    return colorText(str(living.gold) + "g", BColors.YELLOW)


def buy(title: str, stock: dict):
    stockList = list(map(lambda x: x[0] + " (" + colorText(str(x[1].price) + "g", BColors.YELLOW) + ")", stock.items()))
    choice = Menu("Stock - " + title, *stockList, "Back")
    if choice == len(stockList) + 1:
        return 0
    return choice


def select_quantity(item: str, itemCost: int, playerGold: int):
    can_buy = math.floor(playerGold / itemCost)
    amount = Quantity("How many " + item + " would you like to buy? You have "
                      + colorText(str(playerGold) + "g", BColors.YELLOW) + ", you can afford " + str(can_buy)
                      + " of those!", 0, can_buy)
    return amount


def merge_stacking_item(living: Living, item: Item):
    if any(x.name is Item.name for x in living.inventory):
        item_in_inventory = next(x for x in living.inventory if x.name is item.name)
        item_in_inventory += item.quantity
    else:
        living.inventory.append(item)


def charge_gold(living: Living, cost: int, quantity: int = 1):
    living.gold -= int(cost * quantity)


def buy_from_stock(player: Player, stock: dict, title: str):
    item_index = buy(title + " | you have " + str(player.gold) + "g", stock) - 1
    if item_index != -1:
        while True:
            stock_item: StockItem = list(stock.values())[item_index]
            if player.gold >= stock_item.price:
                break
            else:
                print("You don't have the money for that.")
                item_index = buy(title + " | you have " + str(player.gold) + "g", stock) - 1
        amount = select_quantity(stock_item.plural, stock_item.price, player.gold)
        if amount != 0:
            item = stock_item.type()
            item.quantity = amount
            merge_stacking_item(player, item)
            charge_gold(player, stock_item.price, amount)

def format_length(text: str, length: int):
    return text + (length-len(text))*" "