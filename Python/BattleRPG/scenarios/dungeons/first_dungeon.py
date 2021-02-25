from class_library.engine import Living
from items.potions import *
from scenarios.battle import do_battle
from scenarios.dungeons.dungeon_type import Dungeon


class FirstDungeon(Dungeon):

    def enter(self, player: Player):
        print("Welcome to Tutorial Dungeon!")
        print("You'll find weak monsters here and healing items.")

        self.possible_encounters = [
            Living(150, 0, 10, 0, 0, escape_chance=50, name="Ghoul"),
            Living(150, 0, 10, 0, 0, escape_chance=50, name="Ghoul"),
            Living(150, 0, 10, 0, 0, escape_chance=50, name="Ghoul"),
            Living(200, 0, 15, 0, 0, escape_chance=40, name="Greater Ghoul"),
            Living(100, 0, 20, 0, 0, escape_chance=75, name="Volatile Ghoul"),
        ]

        self.possible_chests = [
            HealthPotion(1),
            ManaPotion(1)
        ]
        boss = Living(500, 0, 30, 0, 0, escape_chance=0, name="Bonecrusher")
        boss.inventory.append(HealthPotion(3))
        boss.inventory.append(ManaPotion(1))
        self.boss = Living(500, 0, 30, 0, 0, escape_chance=0, name="Bonecrusher")

        self.treasure_chance = 20
        self.total_encounters = 4

        self.generate_encounters()

        for x in range(len(self.encounter_list)):
            current = self.encounter_list[x]
            if isinstance(current, Item):
                print("You have found ", str(current.quantity) + "x" + str(current.name))
                print("Would you like to pick it up?")
                choice = Menu("", "Yes", "No")
                if choice == 1:
                    merge_stacking_item(player, current)
            elif isinstance(current, Living):
                print("You have encountered a " + str(current.name) + ", prepare to fight!")
                do_battle(player, current)

