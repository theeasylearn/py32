#write a program to calculate & display count , total and average of all the numeric values using arbitrary argument function
def getResult(*values): #*value means tuple
    count = 0
    total = 0
    for item in values:
        count=count+1
        total=total+item
    average = total / count
    return count,total,average

result = getResult(10,20,30,100,200,1125.22)
print(result) #0th position has count, 1st position has total, 2nd position has average