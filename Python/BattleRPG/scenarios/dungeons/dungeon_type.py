from copy import copy
import random

from class_library.engine import Living


class Dungeon:
    encounter_list = []
    possible_encounters = []
    possible_chests = []
    boss: Living
    treasure_chance = 0
    total_encounters = 1

    def generate_encounters(self):
        for encounter in range(self.total_encounters):
            if self.chance_treasure():
                self.encounter_list.append(self.generate_treasure())
            else:
                self.encounter_list.append(self.generate_encounter())

    def chance_treasure(self):
        chance = random.randrange(1, 100)
        if chance <= self.treasure_chance:
            return True
        return False

    def generate_encounter(self):
        encounter = random.randrange(0, len(self.possible_encounters))
        return copy(self.possible_encounters[encounter])

    def generate_treasure(self):
        treasure = random.randrange(0, len(self.possible_chests))
        return copy(self.possible_chests[treasure])
