#Task1 

num1=int(input("Enter a first number: "))
num2=int(input("Enter a second number: "))

#print("1-\tAdd\t\t\t+\n2-\tSubtract\t\t-\n3-\tMultiply\t\t*\n4-\tDivide\t\t\t/\n5-\tSquare\t\t\ts")

print("1-	Add			+ \n"
	  "2-	Subtract		- \n"
	  "3-	Multiply		* \n"
	  "4-	Divide			/ \n"
	  "5-	Square			s \n")

op=input("Enter the operation you wish to perform: ")

if op=="+":
	print(num1+num2)
elif op=="-":
	print(num1-num2)
elif op=="*":
	print(num1*num2)
elif op=="/":
	print(num1/num2)
elif op=="s":
	print(num1**num2)


#Task 2