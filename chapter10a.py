#In this lab you'll practice casting variables.

#functions

#1.
def area(length, width):
	area=length*width
	print("Area of rectangle is: ",area)
	return(area)

def perimeter(length, width):
	perim=(2*length)+(2*width)
	print("Perimeter of rectangle is: ",perim)
	return(perim)


#main code

length=int(input('Enter the length of a rectangle: '))
width=int(input('Enter the width of a rectangle: '))

area(length,width)
perimeter(length,width)

#2. Take your code that counts the vowels in a string and turn this into a function 

#function
def vowels(string):
	count=0
	for letter in string:
		if letter.lower() in "aeiou": #this converts the letters into lower case letters. Need to do this bc the aeiou are in lower case (the vowels)!
			count+=1
	print("Count of vowels is:", count)
	return(count)



#main code

string=input("Please enter a word or sentence: ")


validstr=False
keepGoing=True
#someone might enter a number

while keepGoing:
	for i in string:
		if i.isdigit()==True:
			validstr=False
			string=input("Cannot take numbers. Please enter a word/sentence: ")
			break
		validstr=True
	if validstr:
		keepGoing=False

vowels(string)

#3. Write a function that counts the number of items in a list

#function

def num_items(list_):
	count=0
	for element in list_:
		count+=1
	print("There are "+str(count)+" items in the list.")
	return(count)

#main code

list_=input("Please enter a list separated by commas: ").split(",")

num_items(list_)