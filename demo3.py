#21/01/20

#while loops
counter1=1

#counting from 1 to 10
while counter1<=10: #must indent the things you want to carry out
	print(counter1)
	counter1+=1

print("Finished")

#printing times tables from 0 to 12 where the user inputs a number
num=int(input("Please enter a number between 1 and 12: "))

maxNum=12 #allows you to change the times tables you want to go up to

counter2=0

while counter2<=maxNum:
	print(num, "x", counter2, "=", num*counter2)
	counter2+=1

print("Finished")

#for loops -  dont have to update/initialise the counter yourself

for num in range(5): # for variable in *something which contains a sequence*
	print(num)

for num in range(5,0,-1): #wanting to start at 5 and end at 0 in decrements of 1
	print(num)

greeting="hello"

for letter in greeting:
	print(letter)


sentence=input("enter a sentence")

for l in sentence: #running through the sentence each letter at a time
	print(l)