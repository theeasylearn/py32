# concept of user defined function
#syntax 
#def function-name(parameters):
#example 
def getSquare(number):
    square = number * number
    #here square is local variable
    #local variables, variable created inside function, it is only available inside function in which it is created 
    return square

def getQube(num):
    qube = getSquare(num) * num 
    return qube 

n1 = int(input("Enter number"))
#calling function
result = getSquare(n1) #calling function synchronous calling
print("Square = ",result)
result2 = getQube(n1)
print("Qube = ",result2)
