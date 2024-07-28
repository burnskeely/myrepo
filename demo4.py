#23/01/20
#Keely Burns

#import statements

print("before import")

import math 




#functions

#making your own function

def make_full_name(first_name, last_name): #any instructions for this must be indented. Variables within this are local variables NOT GLOBAL ie only exist in this function.
	full_name=first_name+" "+last_name
	print(full_name) #can include this in the statement
	return full_name #this saves the result





#main code

print("hello world!")


first=input("Enter first name:")
last=input("Enter last name:")
my_name=make_full_name(first,last)
print("My name is",my_name)

if my_name=="_main_":
	print("main code starts")
	print(make_full_name("steph","voss"))

##function
def myFunction():
	global s
	print(s)
	s="I also love Python"
	print(s)

##main
s="I love Python"
print(s)
myFunction()
print(s)