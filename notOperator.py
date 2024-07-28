##########################
## Name: S Voss
## Date: 20/01/2020
## Desc: not operator
##########################

mark = int(input("Enter a mark between 1 and 100:"))

if mark >= 1 and mark <= 100:
    print("Mark is valid")
    markValid=True
else:
    print("Mark is invalid")
    markValid=False


if markValid == True:
    print("Mark is valid")
else:
    print("Mark is invalid")


if markValid:
    print("Mark is valid")
else:
    print("Mark is invalid")


if markValid==False:
    print("Mark is invalid")

if not(markValid):
    print("Mark is invalid")