#Chapter 8 Lists Level 2

#Part 1

ages = [12,18,33,84,45,67,12,82,95,16,10,23,43,29,40,34,30,16,44,69,70,74,38,65,36,83,50,11,79,64,78,37,3,8,68,22,4,60,33,82,45,23,5,18,28,99,17,81,14,88,50,19,59,7,44,93,35,72,25,63,11,69,11,76,10,60,30,14,21,82,47,6,21,88,46,78,92,48,36,28,51]

#1.
length=len(ages)
print(length)

#2. 
for age in ages:
	print(age)

#3.
counter=0
for age in ages:
	ages[counter]+=1
	counter+=1
print(ages)

#or
ages = [12,18,33,84,45,67,12,82,95,16,10,23,43,29,40,34,30,16,44,69,70,74,38,65,36,83,50,11,79,64,78,37,3,8,68,22,4,60,33,82,45,23,5,18,28,99,17,81,14,88,50,19,59,7,44,93,35,72,25,63,11,69,11,76,10,60,30,14,21,82,47,6,21,88,46,78,92,48,36,28,51]

for age in range(0,length):
	ages[age]+=1

print(ages)

#4.


newAge=[]


for age in ages:
	if age>=16 and age<=65:
		newAge.append(age)  #mutable#
		
print("New age", newAge)

#5. 
count=0
for age in newage:
	if age>=16 and age<=25:
		count+=1
print(count)

#6.
newAge.sort()
print(newAge)

#7.
proportion=count/len(newAge)*100
print(proportion)
print("New length", len(newAge))