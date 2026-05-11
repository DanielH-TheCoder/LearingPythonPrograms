#########
import random

list = []
i = 0
count = 0
n = 0
countHolder = 0
n1 = 0

while True: 
    try:
        i = int(input("How many values do you want in the list?"))
        break

    except:
        print("You didn't choose a valid whole number")

for count in range(i):
    count = count + 1
    n = round(random.random()*100)
    list.append(n)  

print(list) 

while True:
    count = 0
    try:
        ascordesc = input("Do you want to sort by ascending [asc] or descending [desc]")  
        break

    except:
        print("you chose wrong, try again")

for n1 in range(i):
    if ascordesc == "asc":
            for count in range((len(list)-1)):
                if list [count] > list [(count + 1)]:
                    countHolder = list[(count + 1)]
                    list [(count + 1)] = list [count]
                    list [count] = countHolder
                    n1 = n1 + 1
    if ascordesc == "desc":
            for count in range((len(list)-1)):
                if list [count] < list [(count + 1)]:
                    countHolder = list[(count + 1)]
                    list [(count + 1)] = list [count]
                    list [count] = countHolder
                    n1 = n1 + 1
                    
print(list)
