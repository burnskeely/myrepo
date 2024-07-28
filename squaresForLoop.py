##########################
## Course 1
## Squares - FOR LOOP
##########################

## Task 1


#1-	Add a new file: Squares.py and make it the startup file 
#2-	Write a while loop that starts at 1 and ends at 100  
#3-	Calculates and displays each number and its square 
#4-	End the loop if that square is bigger than 2000  
#5-	Save and run. 

# While Loop
#n=1
#while n <= 100:
#    print("n is", n, "and the square is",n**2)
#    if(n**2 > 2000):
#        print("Breaking loop...n**2 > 2000")
#        break
    
#    n=n+1

# For Loop
for n in range(1,101):
    print("n is", n, "and the square is",n**2)
    if(n**2 > 2000):
        print("Breaking loop...n**2 > 2000")
        break
    