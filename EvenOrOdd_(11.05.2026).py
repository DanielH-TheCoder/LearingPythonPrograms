
while True:
    try:
        numberInput = input("Please enter a whole number and I will check whether it is even or odd")
        number = int(numberInput) 
        print("Bro this is a whole number")
        break
    except ValueError:
        print("Brother this ain't a whole number")
        
if (number % 2) == 0:
    print ("Bro this is an even number")
else: 
    print ("Bro this an odd number")

