import random

def roll(sides=6) :
    num_rolled = random.randint(1,sides)
    return num_rolled


def main():
    sides = 6
    total_rolled=0
    rolling = True
    while rolling:
        roll_again = input("Ready to roll? ENTER=Roll. Q=Quit. ")
        if roll_again.lower() != "q":
            num_rolled = roll(sides)
            print("You rolled a", num_rolled)
            total_rolled += num_rolled
            print("Total:", total_rolled )
        else:
            rolling = False
        
    print("Thanks for playing.")

main()