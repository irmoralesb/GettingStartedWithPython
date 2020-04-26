import random


class Creature:
    def __init__(self, name, level):
        self.name = name
        self.level = level

    def __repr__(self):
        return "Creature {} of level {}".format(self.name, self.level)

    def get_defensive_roll(self):
        return random.randint(1, 12) * self.level


class Wizard(Creature):
    def __init__(self, name, level):
        super().__init__(name, level)

    def __repr__(self):
        return "Hero {} of level {}".format(self.name, self.level)

    def attack(self, creature):
        print("The wizard {} attacks {}!".format(self.name, creature.name))
        my_roll = random.randint(1, 12) * self.level
        creature_roll = creature.get_defensive_roll()

        print("Your roll {}...".format(my_roll))
        print("{} rolls {}...".format(creature.name, creature_roll))

        if my_roll > creature_roll:
            print("The wizard has handly triumphed {}".format(creature.name))
            return True
        else:
            print("The wizard has been DEFEATED")
            return False


class SmallAnimal(Creature):

    def __init__(self, name, level):
        super().__init__(name, level)

    def get_defensive_roll(self):
        base_roll = super().get_defensive_roll()
        return base_roll / 2


class Dragon(Creature):

    def __init__(self, name, level, scaliness, breaths_fire):
        super().__init__(name, level)
        self.breaths_fire = breaths_fire
        self.scale_thickness = scaliness

    def get_defensive_roll(self):
        base_roll = super().get_defensive_roll()
        fire_modifier = 5 if self.breaths_fire else 1
        return self.level * fire_modifier * self.scale_thickness
