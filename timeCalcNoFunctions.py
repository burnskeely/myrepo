#####################################
## Lists - Time Calculator
#####################################


keepGoing=True
while keepGoing:

    print ("Time Calculator\n")
    print ("1-Add 2 times" )   
    print ("2-Find the difference between 2 times")  
    print ("3-Convert to Hours" )  
    print ("4-Convert to Minutes" )  
    print ("5-Convert Minutes to Time" )  
    print ("6-Convert Hours to Time" )  
    print ("7-Convert Days to Time" )  
    print ("8-Exit\n\n")

    option = int(input("Enter an option: "))  

    if(option in [1,2,3,4]):
        dt1 = input("Enter date-time value in DD:HH:MM format: ")
        timeParts1=dt1.split(":")
        days1=int(timeParts1[0])
        hours1=int(timeParts1[1])
        mins1=int(timeParts1[2])

        if(option == 1  or option == 2):
            dt2 = input("Enter second date-time value in DD:HH:MM format: ")
            timeParts2=dt2.split(":")
            days2=int(timeParts2[0])
            hours2=int(timeParts2[1])
            mins2=int(timeParts2[2])
        
        if(option == 1):
            print("Adding two date-times")
            daysRes = days1 + days2
            hoursRes = hours1 + hours2
            minsRes = mins1 + mins2

            if(minsRes >= 60):
                hoursRes +=1
                minsRes = minsRes%60

            if(hoursRes >= 24):
                daysRes +=1
                hoursRes = hoursRes%24
            
            timePartsRes = [str(daysRes),str(hoursRes),str(minsRes)]
            timeRes = ":".join(timePartsRes)
            print("New time = ",timeRes)

        elif(option == 2):
            print("Subtracting two date-times")
            daysRes = days1 - days2
            hoursRes = hours1 - hours2
            minsRes = mins1 - mins2

            if(hoursRes < 0):
                daysRes -=1
                hoursRes = hoursRes + 24

            if(minsRes < 0):
                hoursRes -=1
                minsRes = minsRes + 60
         
            timePartsRes = [str(daysRes),str(hoursRes),str(minsRes)]
            timeRes = ":".join(timePartsRes)
            print("New time = ",timeRes)
        
        elif(option == 3):
            hoursRes = (days1 * 24) + hours1
            print("Time in hours = ",hoursRes)

        elif(option == 4):
            minRes = mins1 + (hours1 * 60) + (days1 * 24 * 60)
            print("Time in minutes  = ",minRes)
    
    elif(option in [5,6,7]):
        time=int(input("Enter an integer: "))

        if (option == 5):
            hoursRes=int(time/60)
            minsRes=time%60
            daysRes=int(hoursRes/24)
            hoursRes=hoursRes%24
            
            timePartsRes = [str(daysRes),str(hoursRes),str(minsRes)]
            timeRes = ":".join(timePartsRes)
            print("New time from minutes = ",timeRes)

        elif(option == 6):
            daysRes=int(time/24)
            hoursRes=time%24
            minsRes=0

            timePartsRes = [str(daysRes),str(hoursRes),str(minsRes)]
            timeRes = ":".join(timePartsRes)
            print("New time from hours = ",timeRes)

        elif(option == 7):
            daysRes=time
            hoursRes=0
            minsRes=0

            timePartsRes = [str(daysRes),str(hoursRes),str(minsRes)]
            timeRes = ":".join(timePartsRes)
            print("New time from hours = ",timeRes)
    else:
        print("Option not found...exiting")
        break