#1.
newList=[]

#for num in range(0,10,1):
#	newList=newList.insert(num,numList[num])

#print(newList)


for num in range(1,11):
	newList.append(num) #mutable

print(newList)

#2.

numList=[]
number=1
while number<11:
	numList.append(number)
	number+=1
print(numList)

#3. 

for exclaim in range(0,10):
	newList[exclaim]="!"*(exclaim+1)

print(newList)

#4.

cities=["Birmingham","London","Manchester","Edinburgh","Newcastle","Cardiff","Belfast"]

cities.remove("Edinburgh")
cities.pop(0)
cities.pop()

print(cities)

#5. 
numbers=[]

for num in range(5,21):
	numbers.append(num) #mutable
	sumOF=sum(numbers)
	length=len(numbers)
	averageNum=sumOF/length

print(numbers)
print(sumOF)
print(averageNum)


numbers2=[]
count=0
summ=0
for num in range(5,21):
	numbers2.append(num) #mutable therefore dont need to do numbers=numbers.append(num)
	summ=summ+numbers2[count]
	count+=1
	length=len(numbers2)
	av=summ/length

print(numbers2)
print(summ)
print(av)

#6. 
fruits=["apples","oranges","pears","grapes","bananas","strawberries"]

fruits[3]="white grapes"
fruits.append("red grapes")
print(fruits)

#7.
drinks=["cola","milk","water","lemonade","tea","coffee","hot chocolate","orange","apple"]


for word in range(0,len(drinks)):
	if drinks[word]=="apple" or drinks[word]=="orange":
		drinks[word]=drinks[word]+" juice"
	if drinks[word]=="tea" or drinks[word]=="coffee":
		drinks[word]="iced "+drinks[word]

print(drinks)

#OR#

drinks=["cola","milk","water","lemonade","tea","coffee","hot chocolate","orange","apple"]

counter=0
for word in drinks:
	if drinks[counter]=="apple" or drinks[counter]=="orange":
		drinks[counter]=word+" juice"
	if drinks[counter]=="tea" or drinks[counter]=="coffee":
		drinks[counter]="iced "+word
	counter+=1

print(drinks)


#OR#

drinks=["cola","milk","water","lemonade","tea","coffee","hot chocolate","orange","apple"]

indexApple=drinks.index('apple')
indexOrange=drinks.index('orange')
drinks[indexApple]='apple juice'
drinks[indexOrange]='orange juice'
print(drinks)