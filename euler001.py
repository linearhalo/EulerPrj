temp=0
tempInt=0
mins=0
for i in range (1000):
    if (i)%3==0:
        tempInt+=i
    if (i)%5==0:
        temp+=i
    if (i)%15==0:
        mins+=i

print tempInt+temp-mins