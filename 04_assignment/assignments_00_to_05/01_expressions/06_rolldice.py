# Import the random library which lets us simulate random things like dice!
import random

NUM_SIDES: int = 6

def main():
    # Setting a seed is useful for debbuging (uncomment the line below to do so!)
    #  random.seed(1)

    # Roll die
    die1: int = random.randint(1, NUM_SIDES)
    die2: int = random.randint(1, NUM_SIDES)

    # Get their total
    total: int = die1 + die2

    # print out the result
    print(f"Dice have {NUM_SIDES} sides each.")
    print(f"First die: {die1}")
    print(f"Second die: {die2}")
    print(f"Total of two dice: {total}")

if __name__ == '__main__':
    main()