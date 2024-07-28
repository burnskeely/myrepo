#Chapter 7 Task 6

maths=int(input("Enter the mark for maths: "))
while 0>maths or maths>100:
	maths=int(input("Please enter a valid mark for maths: "))


eng=int(input("Enter the mark for english: "))
while 0>eng or eng>100:
	eng=int(input("Please enter a valid mark for english: "))

ict=int(input("Enter the mark for ICT: "))
while 0>ict or ict>100:
	ict=int(input("Please enter a valid mark for ict: "))

average=(maths+eng+ict)/3
if average>=65:
	print("Average mark is:", average, "which is a pass")
else:
	print("Average mark is:", average, "which is a fail")


#OR
CorrectExamCount=0
MCheck=0
ECheck=0
ICheck=0

while CorrectExamCount<3:
	maths=int(input("Enter the mark for maths: "))
	while 0>maths or maths>100:
		maths=int(input("Please enter a valid mark for maths: "))

	MCheck=1
	eng=int(input("Enter the mark for english: "))
	while 0>eng or eng>100:
		eng=int(input("Please enter a valid mark for english: "))
	ECheck=1
	ict=int(input("Enter the mark for ICT: "))
	while 0>ict or ict>100:
		ict=int(input("Please enter a valid mark for ict: "))
	ICheck=1
	
	CorrectExamCount=MCheck+ECheck+ICheck
	print(CorrectExamCount, MCheck, ECheck, ICheck)

if CorrectExamCount==3:	
	average=(maths+eng+ict)/3
	if average>=65:
		print("Average mark is:", average, "which is a pass")
	else:
		print("Average mark is:", average, "which is a fail")