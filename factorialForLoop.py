inp=int(input("Enter an integer: "))
factorial=inp

for num in range(inp-1,1,-1):
	factorial=factorial*num

print("Factorial is", factorial)
