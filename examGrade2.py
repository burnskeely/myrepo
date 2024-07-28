##########################
## Course 1
## Exam Grade 2
##########################


mark = int(input("Enter mark for student between 1 and 100:"))
level=0

if mark < 1 or mark > 100:
    print('Error: marks must be between 1..100')

else:
    level = int(input("Enter level for student: 1 or 2:"))
    if level < 1 or level > 2:
        print("Error: invalid value for level")

if level == 1:
    if mark < 50:
        print("Fail")
    elif mark <= 60 : 
        print("Pass")
    elif mark <= 70:
        print("Merit")
    elif mark >=71:
        print ("Distinction")
    
elif level == 2:
    if mark < 40:
        print("Fail")
    elif mark <= 50:
        print("Pass")
    elif mark <= 65:
        print("Merit")
    else:
        print("Distinction")