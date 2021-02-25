from enum import Enum
from class_library.engine import Item


class EquipmentSlot(Enum):
    HEAD = 0
    NECK = 1
    BODY = 2
    LEGS = 3
    FEET = 4
    HANDS = 5
    PRIMARY = 6
    OFF_HAND = 7
    NONE = 8


class CombatStyle(Enum):
    MELEE = 0
    RANGE = 1
    MAGIC = 2
    HYBRID = 3


class Equipment(Item):
    must_equip = False
    slot: EquipmentSlot = EquipmentSlot.NONE
    damage_resist = 0.0


# Equipment
class LeatherHelmet(Equipment):
    EquipmentSlot = EquipmentSlot.HEAD
    damage_resist = 0.1
