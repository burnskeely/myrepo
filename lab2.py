input('Please enter your name: ') #this wont store your name, hasnt been assigned to a variable

username=input('Please enter your name: ') #this makes the console pop up and prompts you to input in these fields
age=input('Please enter your age: ') #this will hold age as a string even if it is entered as a number
print(username, 'is', age, 'years old') #commas will put spaces in for you, '+' will not! 3 inputs into print 

#print(age +1) #wont work
print(int(age)+1) #this fixes it