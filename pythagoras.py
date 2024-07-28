##########################
## Course 1
## Pythagoras
##
## Options for square root
## -----------------------
## pow(result,0.5)
## math.sqrt(result)
## result ** 0.5
##########################
import math

print("Pythagoras' Calculator")  
print("1-	Find the length of A given B and C")  
print("2-	Find the length of B given A and C") 
print("3-	Find the length of C given A and B")
option=int(input("Enter an option [1-3]:"))

## If ‘1’ is entered, prompt for the length of sides: B and C, calculate the length of side: A
## If ‘2’ is entered, prompt for the length of sides: A and C, calculate the length of side: B 
## If ‘3’ is entered, prompt for the length of sides: A and B, calculate the length of side: C 
## C**2 = A**2 + B**2

if(option == 1):
    sideB=int(input("Enter length of side B:"))
    sideC=int(input("Enter length of side C:"))

    print("Side A = ", math.sqrt((sideC ** 2) - (sideB ** 2)))

elif(option == 2):
    sideA=int(input("Enter length of side B:"))
    sideC=int(input("Enter length of side C:"))

    print("Side B = ", math.sqrt((sideC ** 2) - (sideA ** 2)))
else:
    sideA=int(input("Enter length of side A:"))
    sideB=int(input("Enter length of side B:"))

    print("Side C = ", math.sqrt((sideA ** 2) + (sideB ** 2)))