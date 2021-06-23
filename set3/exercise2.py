"""Set 3, Exercise 2.

An example of how a guessing game might be written.
"""


import random


def exampleGuessingGame():
    """Play a game with the user.

    This is an example guessing game. It'll test as an example too.
    """
    # To begin with, print introduction of the game
    print("\nWelcome to the guessing game!")
    print("A number between 0 and _ ?")
    # I can give a range to the test by using this upperbound
    upperBound = input("Enter an upper bound: ")
    # Using .format to insert the data into str
    print("OK then, a number between 0 and {} ?".format(upperBound))
    # In order to playing guessing number game, change str into int
    upperBound = int(upperBound)

    # Randomly assign the actual number by using randint()
    actualNumber = random.randint(0, upperBound)

    guessed = False

    while not guessed:
        guessedNumber = int(input("Guess a number: "))
        print(
            "You guessed {},".format(guessedNumber),
        )
        if guessedNumber == actualNumber:
            print("You got it!! It was {}".format(actualNumber))
            guessed = True
        elif guessedNumber < actualNumber:
            print("Too small, try again :'(")
        else:
            print("Too big, try again :'(")
    return "You got it!"


if __name__ == "__main__":
    exampleGuessingGame()
