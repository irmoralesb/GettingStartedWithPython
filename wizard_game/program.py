import random

from actors import Wizard, Creature, SmallAnimal, Dragon


def main():
    print_header()
    game_loop()


def print_header():
    print("----------------------------")
    print("     WIZARD GAME APP")
    print("----------------------------")


def game_loop():
    creatures = [
        SmallAnimal('Toad', 1),
        Creature('Tiger', 12),
        SmallAnimal('Bat', 3),
        Dragon('Dragon', 50, 20, True),
        Wizard('Evil Wizard', 1000)
    ]

    hero = Wizard('Gandolf', 75)

    while True:

        active_create = random.choice(creatures)
        print("A {} of level {} has appear from a dark and foggy forest...".format(active_create.name,
                                                                                   active_create.level))
        print()
        cmd = input("Do you [a]ttack, [r]unaway, or [l]ook around? ")
        if cmd == "a":
            if hero.attack(active_create):
                creatures.remove(active_create)
            else:
                print("Game Over")
                break
        elif cmd == "r":
            print("The wizard has become unsure of his power and flees!!!!")
        elif cmd == "l":
            print("The wizard {} takes in the surroundings and sees:".format(hero.name))
            for c in creatures:
                print(" * A {} of level {}".format(c.name, c.level))
        else:
            print("OK, exiting game... bye!")
            break

        if not creatures:
            print("You have defeated all creatures, YOU WIN!!!")
            return


if __name__ == "__main__":
    main()
