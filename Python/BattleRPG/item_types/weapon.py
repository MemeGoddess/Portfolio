from item_types.equipment import Equipment, EquipmentSlot, CombatStyle


class Weapon(Equipment):
    must_equip = True
    slot = EquipmentSlot.PRIMARY
    style = CombatStyle.HYBRID
    stat_spell_damage: float = 0
    stat_damage: float = 0
    stat_resist: float = 0
    stat_mana_max: float = 0
    stat_mana_cost: float = 0

