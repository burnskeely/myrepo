#########################################################
## Task 4 – Input an integer between two limits
#########################################################
# Get Integer

min=1
max=100

attempts=1
maxAttempts=3

while attempts <= maxAttempts:
    number=int(input("Enter a number between 1 and 100:"))
    if number >= min and number <= max:
        break

    attempts= attempts + 1
 
if attempts > maxAttempts:
    print(None)
else:
    print(number)