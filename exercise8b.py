####################################
## Course 1
## Lists
####################################

# 1. Store in a variable and print length
ages = [12,18,33,84,45,67,12,82,95,16,10,23,43,29,40,34,30,16,44,69,70,74,38,65,36,83,50,11,79,64,78,37,3,8,68,22,4,60,33,82,45,23,5,18,28,99,17,81,14,88,50,19,59,7,44,93,35,72,25,63,11,69,11,76,10,60,30,14,21,82,47,6,21,88,46,78,92,48,36,28,51]

ageLength = len(ages)
print("Length of ages list = ", ageLength)

# 2. Display age on each line
print("Display ages")
for age in ages:
    print(age)

# 3. Add one year to every age
print("Adding a year to every age - copy")
for age in ages:
    print(age, age+1)

# 3b. Add one year to every age in place
print("Adding a year to every age")

for i,age in enumerate(ages):
	ages[i] = age + 1

print(ages)

# 4. Removing items outside thew specified age range
# Note the list copy as we cannot keep track of the list and remove elements at the same time
# The line with the list remove causes the existing item to be deleted (item 12) and therefore list is now at item 18
# When the loop moves back to the top and tries to get the next element it will automatically move to the next 
# item in the list (33) which leaves the current item (18) untested  for the age range. This is what causes
# items to be skipped from the test


print("Removing ages outside of the range")

ages_cp = ages.copy()
for age in ages_cp:
    if age < 16 or age > 65:
        print("age outside of range = ",age)
        ages.remove(age)

print("length of ages is now = ",len(ages))
for age in ages:
    print(age)


# 5. Display count of 16 - 25 year olds
count=0
print("Count of 16-25 year olds")
for age in ages:
    if age >= 16 and age <= 25:
        count+=1

print("Count = ",count)

# 6.  Sort the list
ages.sort()

print("display sorted list")
## Display sorted age on each line
for age in ages:
    print(age)

print(ages)
## Proportion of Ages between 16-25 inclusive

counter=0
for age in ages:
    if age >= 16 and age <= 25:
        counter+=1

print("Counter = ",counter)
print("Percentage of Ages between 16-25 is ", (counter/len(ages))*100,2)