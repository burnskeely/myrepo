#############################
#Task 3 - Investment 
############################
#1-	Add a new file: Investment.py and make it the startup file   
#2-	Calculates how many years it will take an initial investment of £100 to grow to a target value of £1000 if the interest rate is 10%
#3-	Save and run.   
#4-	Make your calculation more usable by inputting the following values:
#	Initial investment  
#	Target value  
#	Interest rate  

sum=float(input("Enter initial investment:"))
target=float(input("Enter target sum:"))
rate=float(input("Enter interest rate as decimal number:"))

years=0

while sum <= target:
   sum = sum + (sum * (rate/100))
   years = years + 1

print("Total years =", years)