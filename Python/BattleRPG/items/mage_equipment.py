from item_types.equipment import *
from item_types.weapon import Weapon


# TODO Reform stat_mana_cost to allow a method to populate it, using 1-100
# Weapons =>
class MagicWeapon(Weapon):
    pass

class Wand(MagicWeapon):
    name = "Mage's Wand"
    stat_spell_damage = 0.0
    description = "Increases spell damage by 20% and reduces mana cost by 10%"
    slot = EquipmentSlot.PRIMARY

# Armour => TODO Add some armour
