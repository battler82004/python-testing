# James Taddei
# Monty Hall Problem Example
# 5/20/22

import random

def main():
    # Variable declarations
    correctGuesses = [0,0]
    runs = 100_000

    # Program description
    print("This program works to show the Monty Hall problem at work by running 100,000 test")
    print("of the problem with switching and 100,000 without before displaying the results of")
    print("all of the runs.")

    # This block finds the times the program guesses the door with the car behind it
    # based on the two selection methods
    for shouldSwitch in range(2):
        for i in range(runs):
            doors = create_random_doors()
            choice = random.randint(0,2)

            if (shouldSwitch): # switches doors on the second set of guesses
                choice = switch_doors(doors,choice)

            # counts the number of times the program correct guesses the car's pos
            if (doors[choice]):
                correctGuesses[shouldSwitch] += 1

    # Outputs the correct number of guesses
    print(f"Number of correct guesses without switching: {correctGuesses[0]}")
    print(f"Number of correct guesses with switching: {correctGuesses[1]}")
    print(f"Number of tests for each method: {runs}")

def create_random_doors() -> list:
    """
        Creates a list holding a set of 3 random doors with 2 0's and
        1 1. (The 0's represent the goats and the 1 represents the car)
    """

    doors = [0,0,0]
    carPos = random.randint(0,2)
    doors[carPos] = 1
    
    return doors

def door_to_remove(doors: list,choice: int) -> int:
    """
        Takes in the list 'doors' and the chosen door and returns
        the door (holding a goat) which should be removed from the
        program's choices in order to simulate the Monty Hall Problem.
    """

    goatPoses = [0,1,2] # possible positions for a goat to be
    goatPoses.pop(choice)

    if (doors[choice]): # the program originally chose the car
        return random.choice(goatPoses) # returns one of the goats' positions

    # the programn originally chose a goat
    if not(doors[goatPoses[0]]): # the first number in list is a goat
        return goatPoses[0]

    return goatPoses[1] # the second number in the list is the only goat pos returnable

def switch_doors(doors: list,choice: int) -> int:
    """
        Takes the door chosen by the list 'doors' and the pos
        chosen by the user and returns the pos of the other
        choosable door so that the program can switch which
        door to choose after one of the goat doors is removed.
    """

    removedDoor = door_to_remove(doors,choice)
    options = [0,1,2]
    options.pop(removedDoor)

    originallyChosen = choice

    # if the originally chosen is after the removed goat door,
    # subtract 1 since the removed door was removed from the list
    if (choice > removedDoor):
        originallyChosen -= 1
    
    options.pop(originallyChosen)

    return options[0]

main()
