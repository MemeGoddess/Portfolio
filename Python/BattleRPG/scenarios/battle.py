from class_library.engine import Living, colorText, BColors, Player


def do_battle(player: Player, enemy: Living):
    player.has_used_item = False
    enemy.has_used_item = False
    while enemy.alive:
        action = player.choose_action()
        if action == 1:
            attackDamage = player.generate_damage()
            print("You hit the enemy for", str(attackDamage) + "!")
            enemy.take_damage(attackDamage)
        elif action == 2:
            spell = player.magic[player.choose_magic() - 1]
            if player.mp >= spell.cost:
                spellDamage = player.generate_spell_damage(spell)
                if spellDamage > 0:
                    print("You hit the enemy for", colorText(spellDamage, BColors.RED), "spell damage! Your mana is now", colorText(player.mp, BColors.BLUE) + "!")
                    enemy.take_damage(spellDamage)
                else:
                    print("Your mana is now", colorText(player.mp, BColors.BLUE) + "!")
            else:
                print("You try to cast", spell.name, "but it fizzles, as you don't have enough mana.")
                print("You have", colorText(player.mp, BColors.BLUE), "mana!")
        elif action == 3:
            if player.has_used_item:
                print("You have already used an item this round")
                continue
            else:
                consumableList = player.list_consumables()
                if len(consumableList) > 0:
                    print(consumableList[0].name)
                else:
                    print("You have no consumables in your inventory")
                continue
        print("Enemy now has", colorText(enemy.hp, BColors.GREEN), "health!")
        enemyDamage = enemy.generate_damage()
        print("Enemy deals", colorText(enemyDamage, BColors.RED), "damage to you!")
        player.take_damage(enemyDamage)
        print("You now have", colorText(player.hp, BColors.GREEN), "health!")
        print()
        print("-------------------------")
        print()
        player.has_used_item = False
        enemy.has_used_item = False

    if enemy.alive:
        print("You have lost :(")
    else:
        print("You win!")

    print()
    print("-------------------------")
