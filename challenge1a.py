#Part 1

data=[90,30,13,67,85,87,50,45,51,72,64,69,59,17,22,23,44,25,16,67,85,87,50,45,51,72,59,14,50,55,32,23,24,25,37,28,39,30,33,35,40,34,41,43,94,95,98,99,44,45,47,48,49,53,61,63,69,75,77,60,83]

length=len(data)

print("Number of student marks in the data sample is", str(length))

data.sort()
mini=min(data)
maxi=max(data)

print(("The lowest mark is {0} and the highest mark is {1}").format(mini, maxi))

av=sum(data)/length
rounded_av=round(av,2)

print(("The average mark of the data is {0}").format(rounded_av))


#Part 2


count0=0
count10=0
count20=0
count30=0
count40=0
count50=0
count60=0
count70=0
count80=0
count90=0



for index in range(0,length):
	if data[index]>=0 and data[index]<10:
		count0+=1
	elif data[index]>=10 and data[index]<20:
		count10+=1
	elif data[index]>=20 and data[index]<30:
		count20+=1
	elif data[index]>=30 and data[index]<40:
		count30+=1
	elif data[index]>=40 and data[index]<50:
		count40+=1
	elif data[index]>=50 and data[index]<60:
		count50+=1
	elif data[index]>=60 and data[index]<70:
		count60+=1
	elif data[index]>=70 and data[index]<80:
		count70+=1
	elif data[index]>=80 and data[index]<90:
		count80+=1
	elif data[index]>=90 and data[index]<100:
		count90+=1

star0=count0*"*"
star10=count10*"*"
star20=count20*"*"
star30=count30*"*"
star40=count40*"*"
star50=count50*"*"
star60=count60*"*"
star70=count70*"*"
star80=count80*"*"
star90=count90*"*"


print("Mark \t Count \t \n"
	  "0-10 \t", str(count0), "\t", str(star0), "\n"
	  "10-20 \t", str(count10), "\t", str(star10), "\n"
	  "20-30 \t", str(count20), "\t", str(star20), "\n"
	  "30-40 \t", str(count30), "\t", str(star30), "\n"
	  "40-50 \t", str(count40), "\t", str(star40), "\n"
	  "50-60 \t", str(count50), "\t", str(star50), "\n"
	  "60-70 \t", str(count60), "\t", str(star60), "\n"
	  "70-80 \t", str(count70), "\t", str(star70), "\n"
	  "80-90 \t", str(count80), "\t", str(star80), "\n"
	  "90-100 \t", str(count90), "\t", str(star90))




#Part 3

cutoff=int(0.6*length)

print("To ensure that at least 60% of students will pass the exam,",str(cutoff), "people must pass.")

difference=length-cutoff
passmark=data[difference]
passmark=(passmark//10)*10

print("Therefore, the pass mark of the exam is "+str(passmark)+".")