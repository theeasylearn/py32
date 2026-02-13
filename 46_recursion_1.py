# write a program to display 1 to 10 in reverse order 
def printNumber(number):
    if number>=1:
        print(number)
        number=number-1
        printNumber(number) #function  called itself(recursion)

number = 10 
printNumber(number)