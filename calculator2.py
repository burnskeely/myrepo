##########################
## Course 1
## Calculator
##########################

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

## Menu Option 1
print("1 - Add         +")
print("2 - Subtract    -")        
print("3 - Multiply    *")
print("4 - Divide      /")
print("5 - Square      s")

## Menu Option 2
#print("1 - Add         +\n2 - Subtract    -\n3 - Multiply    *\n4 - Divide/\n5 - Square      2")

## Menu Option 3
#print("""1 - Add         +
#2 - Subtract    -        
#3 - Multiply    *
#4 - Divide      /
#5 - Square      s""")

option=input("Enter an operation: ")

if option == "+":
    print(num1 + num2)
elif option == "-":
    print(num1-num2)
elif option == "*":
    print(num1 * num2)
elif option == "/":
    print(num1/num2)
elif option == "s":
    print(num1 * num1)
else:
    print("option not supported")