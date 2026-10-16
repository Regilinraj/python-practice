salaries=[25000,32000,28000,45000,30000]
total=sum(salaries)
print("total:",total)
maximum=max(salaries)
print("max:",maximum)
average=total/len(salaries)
print("average:",average)
count=0
for salary in salaries:
    if salary>30000:
        count+=1
print("above 30000:",count)