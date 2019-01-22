# the prompts are for correction (may use .format instead)


class Character:
    def __init__(self, hp, name):
        self.hp = hp
        self.max_hp = hp
        self.name = name
        print("You have have created a character with", self.max_hp, "hp")
        print("his/her name is", self.name)

    def hp_status(self):
        print("You now have", self.hp, "hp /", self.max_hp, "hp")

    def damage(self, damage_val):
        self.hp -= damage_val
        print("You have taken {} damage".format(damage_val))

        if self.hp < 0:
            self.hp = 0
            print("You have died.")
            print("Game over.")
            exit()
            # possibly insert some death consequence here
            # for the meantime, game will end

        self.hp_status()

    def heal(self, heal_val):
        print("You have been healed {} hp".format(heal_val))

        if self.hp + heal_val > self.max_hp:
            self.hp = self.max_hp
        else:
            self.hp += heal_val

        self.hp_status()
