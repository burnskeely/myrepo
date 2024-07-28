##########################
## Course 1
## Exam Grade
##########################

mark = int(input("Enter mark for student between 1 and 100:"))

if mark < 1 or mark > 100 :
    print('Error: marks must be between 1..100')
elif mark < 50:
    print("Fail")
elif mark <= 60:
    print("Pass")
elif mark <= 70:
    print("Merit")
elif mark <= 100:
    print("Distinction")