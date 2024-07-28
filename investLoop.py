#Chapter 7 task 3

#Calculates how many years it will take an initial investment of £100 
#to grow to a target value of £1000 if the interest rate is 10%

initial=100
current=initial
target=1000
intRate=0.1 #10%
year=1

while current<=target:
	current= initial*(1+intRate)**year
	year+=1

print("It takes "+ str(year) + " years to meet your target value of £"+ str(target))

#OR

initial=int(input("Enter your initial investment: "))
current=initial
target=int(input("Enter your target value: "))
intRate=int(input("Enter the interest rate: "))
year=1

while current<=target:
	current=current*(1+intRate/100)**year
	year+=1

print("It takes "+ str(year) + " years to meet your target value of £"+ str(target) + " at an intererst rate of"+ str(intRate)+"%")