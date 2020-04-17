import random

print("-----------------------------------------")
print("         GUESS THAT NUMBER")
print("-----------------------------------------")
print()

the_number = random.randint(0, 100)
guess = -1
#print(guess_text, type(guess_text))
#print(guess, type(guess))
while guess != the_number:
    guess_text = input("Guess a number between 0 and  100: ")
    guess = int(guess_text)

    if guess < the_number:
        print("Your guess of {0} was too low".format(guess))
    elif guess > the_number:
        print("Your guess of {0} was too high".format(guess))
    else:
        print("Congratulations!!!")

print("done.")
