date1=(4,1,2024)
date2=(5,2,2025)

for i in range(len(date1)):
    for j in range(len(date2)):

#for days        
        if date1[0]<date2[0]:
            date=(date1[0]-date2[0])*(-1)
        else:
            date=date1[0]-date2[0]

#for month            
        if date1[1]<date2[1]:
             month=(date1[1]-date2[1])*(-1)
        else:
             month=date1[1]-date2[1]
        if(date1[1] % 4 == 0 and date1[1] % 100 != 0) or (date1[1] % 400 == 0):
            month = month*29
        else:
            month = month*30
        


        

#for year             
        if date1[2]%4==0 or date2[2]%4==0:
            if date1[2]<date2[2]:

                # leap year 

                year=(date1[2]-date2[2])*(-1)
                year=year*366
            else:
                year=date1[2]-date2[2]
                year=year*366
        else:
            if date1[2]<date2[2]:
                year=(date1[2]-date2[2])*(-1)
                year=year*365
            else:
                year=date1[2]-date2[2]
                year=year*365
            
        #month=month*30
        between=date+month+year
print("date =",date)
print("month =",month)
print("year =",year)
print(between)
