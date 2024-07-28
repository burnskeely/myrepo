#In this lab you'll practice casting variables.


length=input('Enter the length of one side of a rectangle: ')
width=input('Enter the length of another side of a rectangle: ')

print(int(length) + int(length) + int(width) +int(width), 'is the perimeter of the rectangle')
print(int(length)*int(width), 'is the area of the rectangle')

#OR

length=int(input('Enter the length of one side of a rectangle: '))
width=int(input('Enter the length of another side of a rectangle: '))

print(length + length + width + width, 'is the perimeter of the rectangle')
print(length*width, 'is the area of the rectangle')

#OR

length=int(input('Enter the length of one side of a rectangle: '))
width=int(input('Enter the length of another side of a rectangle: '))

perimeter=length+length+width+width
area=length*width

print('Perimeter of the rectangle: ', str(perimeter))
print('Area of the rectangle: ', str(area))


print("20"*3)
print(int("20")*3)

myNumber=15
myNumber=myNumber+1
myNumber+=1 #shorthand of the above