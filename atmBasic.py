currentbal = 67.14
maxwithdrawal=(currentbalance//10)*10

print("Welcome to Northern Frock \n"
	  "1-	Display balance \n"
	  "2-	Withdraw funds \n"
	  "3-	Deposit funds \n"
	  "9-	Return card \n")

op=int(input("Enter an option: "))

if op<1 or op>3 and op != 9:
	print('Error: must enter a valid option')
else:
	if op==1:
		print("Current balance on card is £"+ str(currentbal), "\n"
			  "Maximum balance to withdrawal is £"+ str(maxwithdrawal))
	elif op==2:
		print("Please select a withdrawal amount \n"
	  "1- £10	2- £20 \n"
	  	  "3- £40	4- £60 \n"
	  "5- £80	6- £100 \n"
	  "7- Other amount \n"
	  "8- Return to main menu")
		withdrawal=int(input("Enter an option: "))
		if withdrawal<1 or withdrawal>6:
			if withdrawal==1 and maxwithdrawal>=10:
				print("Money has successfully been withdrawn")
				currentbal=currentbal-10
			else:
				print("Insufficient funds")
			if withdrawal==2 and maxwithdrawal>=20:
				print("Money has successfully been withdrawn")
				currentbal=currentbal-20
			else:
				print("Insufficient funds")
			if withdrawal==3 and maxwithdrawal>=40:
				print("Money has successfully been withdrawn")
				currentbal=currentbal-40
			else:
				print("Insufficient funds")
			if withdrawal==4 and maxwithdrawal>=60:
				print("Money has successfully been withdrawn")
				currentbal=currentbal-60
			else:
				print("Insufficient funds")
			if withdrawal==5 and maxwithdrawal>=80:
				print("Money has successfully been withdrawn")
				currentbal=currentbal-80
			else:
				print("Insufficient funds")
			if withdrawal==6 and maxwithdrawal>=100:
				print("Money has successfully been withdrawn")
				currentbal=currentbal-100
			else:
				print("Insufficient funds")




			if withdrawal==7 and currentbal>=10:
				print("Money has successfully been withdrawn")
			else:
				print("Insufficient funds")
			if withdrawal==8 and currentbal>=10:
				print("Money has successfully been withdrawn")
			else:
				print("Goodbye")
				break