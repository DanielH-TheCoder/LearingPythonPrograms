import random

DiceMin = 1
DiceRoll = 0
BankBalance = 100 
loop = 0

# Dice Roll Code
while True:
    print("Playing the game...")

    DiceSides = int(input("How many sides of a dice do you want to roll?"))
    BetNumber = int(input("What number do you want to bet on?"))

    while loop == 0:
        if BetNumber > DiceSides:
            BetNumber = int(input(f"Your number is bigger than the potential highest dice roll, please choose again - a reminder the highest number achievable is: {DiceSides}"))
        if BetNumber < DiceMin:
            BetNumber = int(input(f"Your number is lower than the potential lowest dice roll, please choose again - a reminder the loewst number achievable is: {DiceMin}"))
        if BetNumber >= DiceMin and BetNumber <= DiceSides: 
            loop = 1

    Bet = int(input("How much do you want to bet on the roll?"))
    DiceRoll = random.randint(DiceMin, DiceSides)

    print("\nDiceRoll is:", DiceRoll, "\nYour Bet was", Bet)

    if BetNumber == DiceRoll:
        Bet = Bet*DiceSides
        BankBalance = BankBalance + Bet
    else:
        BankBalance = BankBalance - Bet
        Bet = 0

    print("You won:", Bet, "\nYour New Bank Balance is", BankBalance )
    
    play_again = input("Play again? (y/n): ").lower().strip()

    if play_again not in ["y", "n"]:
        print("Invalid choice.")
        continue

    if play_again == "n":
        break

