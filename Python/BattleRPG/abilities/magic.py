from enum import Enum

from abilities.ability_type import Ability
from item_types.equipment import CombatStyle


class MagicType(Enum):
    # Combat
    Frost = 0,
    Fire = 1,
    # Restoration
    Debuff = 2,
    Buff = 3,


class MagicAbility(Ability):
    spell_type: MagicType


class MagicAbilityCustom(MagicAbility):
    pass


magic_spells = [
    MagicAbility("Snow blast", description="", level=1, cost=0, style=CombatStyle, power_min=5, power_max=10)
]



