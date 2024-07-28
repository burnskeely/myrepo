######################################
#Task 2 - Factorial   - FOR LOOP
######################################

#1-	Add a new file: Factorial.py and make it the startup file  
#2-	Inputs an integer.
#3-	Display the number's factorial.
#Tip: Use a while loop.
#Note: the factorial of a number is that number multiplied by all the preceding numbers.
#		The factorial of 5 is =  5 x 4 x 3 x 2 x 1 = 120  
#		or if you like = 1 x 2 x 3 x 4 x 5


num=int(input("Enter a whole number:"))
factorial = 1;
while num >= 1:
    factorial = factorial * num    
    num = num-1
    
print(factorial)


## FOR LOOP
num=int(input("Enter a whole number:"))
factorial=1
for i in range(num,0,-1):
    factorial = factorial * i    
    
print(factorial)
