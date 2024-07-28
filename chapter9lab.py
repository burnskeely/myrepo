import statistics


#1.

data="100,30,53,67,85,87,50,45,51,72,64,69,59,17,22,23,44,25,16,67,85,87,50,45,51,72,59,14,50,55,32,23,24,25,37,28,39,30,33,35,40,34,41,43,94,95,59,98,99,44,45,47,48,49,53,61,63,69,75,77,60,83"


grades=data.split(",")
print(grades)
mini=min(grades)

print("Minimum value:", mini)

maxi=max(grades)

print("Maximum value:", maxi)

grades=list(map(int,grades))

print("Minimum value:", min(grades))

print("Maximum value:", max(grades))

summ=sum(grades)
length=len(grades)
av=summ/length
aver=round(av,2)

print("Average of the grades:", aver)

m=statistics.mean(grades)
rounded_mean=round(m,2)

print("Average of the grades:", rounded_mean)

med=statistics.median(grades)
print("Median:", med)

print("The minimum value is: "+ str(mini)+". \n"+ "The maximum value is: "+ str(maxi)+". \n"+ "The average value is: "+str(aver)+". \n"+ "The mean() value is: "+str(rounded_mean)+". \n"+ "The median value is: "+str(med)+".")

#str.format()

print("The minimum value is: {0}. \n" "The maximum value is: {1}. \n" "The average value is: {2} \n" "The mean() value is: {3}. \n" "The median value is: {4}.".format(mini,maxi,aver,rounded_mean,med))