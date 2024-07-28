################################
## Course 1
## In Built Functions Lab
################################

import statistics

data="100,30,53,67,85,87,50,45,51,72,64,69,59,17,22,23,44,25,16,67,85,87,50,45,51,72,59,14,50,55,32,23,24,25,37,28,39,30,33,35,40,34,41,43,94,95,59,98,99,44,45,47,48,49,53,61,63,69,75,77,60,83"

print(data)

grades = data.split(",")

print(grades)

print(min(grades))
print(max(grades))

# Using the map function
grades = list(map(int, grades))
print(grades)

print(min(grades))
print(max(grades))

# Display average of grades to 2dp

avg = round(sum(grades)/len(grades),2)
print(avg)

# Using statistics library
mean_grade = round(statistics.mean(grades),2)
median_grade = statistics.median(grades)

print(mean_grade)
print(median_grade)

# Using string.format() function for display
print("The mean is {} \n the median is {} \n the max is {} \n the min is {} \nThe average is {}".format(mean_grade,median_grade,max(grades),min(grades),avg))