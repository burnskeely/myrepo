###################################
## EXERCISE 9b - Advanced Strings
###################################

myString=input("Enter a string of characters: ")


# 1. Uppercase version of string
print("Upper case version",myString.upper())

# 2. Lowercase version of string
print("Upper case version",myString.lower())

# 3. Number of characters
print("Number of characters =" ,len(myString))

# 4. Number characters without spaces
newString=myString.replace(' ','')
print("Number of characters without spaces is =",len(newString))

# 5. Number uppercase characters
count=0
for i in myString:
    if i.isupper():
        count+=1
print("Number of characters in upper case =",count)

# 6. Number lowercase characters
count=0
for i in myString:
    if i.islower():
        count+=1
print("Number of characters in lower case =",count)

# 7. Test Palindrome
count=len(myString)    
newString=''
while count >=1:
    newString= newString + myString[count-1]
    count-=1

if newString == myString:
    print("Is a Palindrome")
else:
    print("Is not a Palindrome")


# 8. Print String in Reverse
count=len(myString)    
while count >=1:
    print(myString[count-1])
    count-=1