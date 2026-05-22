######### 
#-------- Initialise Global Variables
#########
import random
import matplotlib.pyplot as plt

list = []
i = 0
count = 0
n = 0
countHolder = 0
n1 = 0

print("Running the list program...")

def create_list():
    while True: 
        try:
            global i
            i = int(input("How many values do you want in the list?"))
            break

        except:
            print("You didn't choose a valid whole number")

    for count in range(i):
        count = count + 1
        n = round(random.random()*100)
        global list 
        list.append(n)  

    print(f"List: {list}") 

def run_program():
    while True:
        count = 0
        try:
            ascordesc = input("\nDo you want to: \n1. sort list by ascending [asc]  \n2. sort list by descending [desc] \n3. randomly shuffle values in list [rand]\n4. See Stats on the list [stats]\n5. Edit list manually [edit]\n6. Plot List onto Graph [vis]\n\nEnter your choice:")

            if ascordesc in ("[asc]", "[desc]","[rand]","[stats]","[edit]", "[vis]"):
                break

            else:
                print("you chose wrong, remember to enter your option as follows: [xxx]")

        except:
            print("you chose wrong, try again, remember to enter your option as follows: [xxx]")

    for for_count in range(i):
        if ascordesc == "[asc]":
            for count in range((len(list)-1)):
                if list [count] > list [(count + 1)]:
                    countHolder = list[(count + 1)]
                    list [(count + 1)] = list [count]
                    list [count] = countHolder
        if ascordesc == "[desc]":
            for count in range((len(list)-1)):
                if list [count] < list [(count + 1)]:
                    countHolder = list[(count + 1)]
                    list [(count + 1)] = list [count]
                    list [count] = countHolder
        if ascordesc == "[rand]":
            random.shuffle(list)
            break

        if ascordesc == "[stats]":
            print("\nCount:", len(list))
            print("Sum:", sum(list))
            print("Min:", min(list))
            print("Max:", max(list))
            print("Average:", sum(list)/len(list))
            break

        if ascordesc == "[edit]":
            while True:
                try:
                    choose = int(input("What is the position of the data point you want to edit (1 = 1st number)?\nEnter the position:"))
                    choose = choose - 1
                    choose_confirm = input(f"Position: {choose + 1} corresponds to this data point in the list: {list[choose]} \nConfirming this choice (y/n)?")
                    if choose_confirm.lower() == "y":
                        choose_change = int(input("What number do you want to change this too?"))
                        list[choose] = choose_change
                        break
                    else:
                        print("Lets try again...")
                    
                    
                except:
                    print("Please enter a whole number")
            break 

        if ascordesc == "[vis]":
            x_axis = range(1, len(list)+1)
            plt.plot(x_axis, list, marker ='X')
            plt.title("List Values Plotted")
            plt.xlabel("List Order")
            plt.ylabel("Numbers")
            plt.show()
            break

create_list()        
while True: 
    run_program()
    print(f"\nList: {list}")
    again = input("Do you want to run again? (y/n): ")

    if again.lower() != "y":
        print("Program Ended")
        break
