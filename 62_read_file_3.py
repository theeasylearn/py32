#write a program to read data from file fruits.txt
filename = input("Enter file name")
mode = "r"

try:
    #file open in read mode
    file = open(filename,mode)

    #read data from file line by line 
    for line in file:
        #this for loop fetch one line from file, store it into line variable
        print(line.strip()) #strip remove newline from both side of line variable

    file.close()
except FileNotFoundError as error:
    print("file not found")
else:
    print("*"*110)
    print("file read successfully")