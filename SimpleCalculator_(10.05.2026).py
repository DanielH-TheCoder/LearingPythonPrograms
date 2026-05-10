LoopCounter = 0
n1 = 0.0
n2 = 0.0
n3 = 0.0

while LoopCounter == 0:
    UserChoice = input("Do you want to add, subtract, multiply or divide?")
    if UserChoice not in ['add', 'subtract', 'multiply', 'divide']:
        print("You've selected an incorrect choice, please ensure you type one of the aforementioned options exactly")

    else:
        LoopCounter = 1

        if UserChoice == 'add':
            LoopCounter = 1
            n1 = float(input("Enter your 1st number"))
            n2 = float(input("Enter your 2nd number"))
            n3 = n1 + n2
        if UserChoice == 'subtract':
            LoopCounter = 1
            n1 = float(input("Enter your 1st number"))
            n2 = float(input("Enter your 2nd number"))
            n3 = n1 - n2
        if UserChoice == 'multiply':
            LoopCounter = 1
            n1 = float(input("Enter your 1st number"))
            n2 = float(input("Enter your 2nd number"))
            n3 = n1 * n2
        if UserChoice == 'divide':
            LoopCounter = 1
            n1 = float(input("Enter your 1st number"))
            n2 = float(input("Enter your 2nd number"))
            n3 = n1 / n2
    
print('Your answer is:', n3)

