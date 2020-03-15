from random import sample


ABILITIES = [
    "strength",
    "dexterity",
    "constitution",
    "intelligence",
    "wisdom",
    "charisma"
]


def modifier(score):
    return (score - 10) // 2


class Character:
    def __init__(self):
        for ability in ABILITIES:
            setattr(self, ability, self.__ability())
        self.hitpoints = 10 + modifier(self.constitution)

    def ability(self):
        rolls = sorted(sample(range(1, 6), 4))
        return sum(rolls[1:])

    __ability = ability
