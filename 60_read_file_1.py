#write a program to read data from file fruits.txt
filename = "fruits.txt"
mode = "r"

#file open in read mode
file = open(filename,mode)

#read data from file line by line 
for line in file:
    #this for loop fetch one line from file, store it into line variable
    print(line.strip()) #strip remove newline from both side of line variable

print("*"*110)
print("file read successfully")