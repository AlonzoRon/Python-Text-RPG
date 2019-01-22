from Character import Character


def main():
    character_1 = Character(100, "Borik")

    character_1.damage(45)
    character_1.heal(1000)
    character_1.damage(45)
    character_1.damage(45)
    character_1.damage(45)


main()
