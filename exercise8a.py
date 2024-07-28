# ################################################
# Exercise 8a Lists
#################################################

# Question 1
newList=[]
for num in range(1,11):
    newList.append(num)

print(newList)


# Question 2
newList=[]
count=1
while count <=10:
    newList.append(count)
    count+=1

print(newList)

# Question 3
for number in newList:
    print(number, "!" * number)


# Question 4
# Remove Edinburgh using the name
# Remove the first item in the list by index (or position)
# Remove the last item in the list by index using the length of the list to determine the position of the last item
cities=["Birmingham","London","Manchester","Edinburgh","Newcastle","Cardiff","Belfast"]

cities.remove("Edinburgh")
cities.pop(0)
cities.pop(len(cities)-1)
print(cities)

# Question 5
total=0
numList=[]
for number in range(5,21):
    numList.append(number)
    total += number

print("Total = ",total)
print("Average = ", total /len(numList) )


# Question 6
fruits=["apples","oranges","pears","grapes","bananas","strawberries"]

fruits[3] = "white grapes"

for index,fruit in enumerate(fruits):
    if fruit == "grapes":
        fruits[index] = "white grapes"

fruits.append("red grapes")
print(fruits)


# Question 7 - option 1
drinks=["cola","milk","water","lemonade","tea","coffee","hot chocolate","orange","apple"]

for index,drink in enumerate(drinks):
    if drink in ("apple","orange"):
        drinks[index] = drink + " juice"
    elif drink in ("tea","coffee"):
        drinks[index] = "ice " + drink
    
print(drinks)

# Question 7 - option 2

counter=0
for drink in drinks:
    if drink in ("apple","orange"):
        drinks[counter] = drink + " juice"
    elif drink in ("tea","coffee"):
        drinks[counter] = "ice " + drink
    counter+=1
    
print(drinks)


# Question 7 - option 3

for drink in drinks:
    counter=drinks.index(drink)
    if drink in ("apple","orange"):
        drinks[counter] = drink + " juice"
    elif drink in ("tea","coffee"):
        drinks[counter] = "ice " + drink
    counter+=1
    
print(drinks)

# Question 7 - option 4

for index in range(0,len(drinks)-1):
    if drinks[index] in ("apple","orange"):
        drinks[index] = drinks[index] + " juice"
    elif drinks[index] in ("tea","coffee"):
        drinks[index] = "ice " + drinks[index]
    
print(drinks)