#Chapter 7 task 2

inp=int(input("Enter an integer: "))
factorial=inp
counter=1

while counter>0 and counter<inp:
	factorial=factorial*counter
	counter+=1

print("Factorial is", factorial)