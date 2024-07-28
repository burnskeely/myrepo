####################
# Course 1
# Selection Lab 2
####################

age = int(input('Enter age: '))

# Chain of if statements
if age >= 18:
	print("Category A")

if age >= 16:
	print("Category B")

if age < 16:
	print("Category C")


# Block of if /elif /else
if age >= 18:
    print("Category A")

elif age >= 16:
    print("Category B")

else:
    print("Another age...")