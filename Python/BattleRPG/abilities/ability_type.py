from class_library.engine import Living
from item_types.equipment import CombatStyle


class Ability:
    def __init__(self, name, level=1, off_level=0, cost=0, style=CombatStyle.HYBRID, full_hit_chance: int = 80,
                 power_min = 0, power_max = 0, description=""):
        self.name = name
        self.level = level
        self.off_level = off_level
        self.cost = cost
        self.style = style
        self.description = description
        self.full_hit_chance = full_hit_chance
        self.power_min = power_min
        self.power_max = power_max

    def on_use(self, caster: Living, target: Living):

        pass
