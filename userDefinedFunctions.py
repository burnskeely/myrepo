##############################
## Name: Stephanie
## Date: 04/10/2019
## Desc: User Defined Functions
###############################

#import statistics
#import math

### User Defined Functions

def getAreaRectangle(length,width):
    return length * width

def getPerimeter(length,width):
    return (2* width) + (2 *length)

def countVowels(aString):
    vowels = "aeiou"
    counter=0
    for letter in aString:
        if letter.lower() in vowels:
            counter+=1
    return counter

def countItems(aList):
    counter=0
    for i in aList:
        counter+=1
    return counter


###### Main Code

userLength=int(input("Enter length:"))
userWidth=int(input("Enter width"))
area=getAreaRectangle(userLength,userWidth)
perimeter=getPerimeter(userLength,userWidth)

print(area)
print(perimeter)

word = input("Enter a word:")
print("Number of vowels in word is",countVowels(word))

myList=input("Enter items into a list separated by comma:").split(",")
print("Number items in list",countItems(myList))