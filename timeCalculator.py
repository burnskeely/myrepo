import TimeCalculator
import datetime


print("Time Calculator\n"
"1- Add 2 times \n"
"2- Find the difference between 2 times \n"
"3- Convert to Hours \n"
"4- Convert to Minutes \n"
"5- Convert Minutes to Time \n"
"6- Convert Hours to Time \n"
"7- Convert Days to Time \n"
"8- Exit")


option=int(input("Enter an option between 1 and 8: "))

while 1>option>8:
	option=int(input("Invalid option, please try again. \n "
					 "Enter an option between 1 and 8: "))

while 1<=option<=8:
	if option==1 or option==2:
		time1=input("Please enter the first time in the format DD:HH:MM: ").split(":") #creating a list where the first character in list is date then hours then minutes
		time2=input("Please enter the second time in the format DD:HH:MM: ").split(":")
		time1=datetime.datetime(time1)
		time2=datetime.datetime(time2)
		if option==2:
			diff=time1-time2
			print("The difference between 2 times is:", diff)
	
	elif option==3 or option==4 or option==5:
		time3=input("Please enter a time in the format DD:HH:MM: ").split(":")
		if option==3:
			f#convert to hours
		elif option==4:
			f#convert to mins
		elif option==5:
			f#convert minutes to time

	elif option==6 or option==7:
		time4=int(input("Please enter a single integer: "))
		if option==6:
			f#convert hours to time
		elif option==7:
			f#convert days to time
	elif option==8:
		break #exit