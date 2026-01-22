# write a program to print following series 
# 1     -4      9     -16     25      -36     1000
# 1     2       3       4       5       6    
number = 1
square = 0
while square<961:
    square = number * number 
    reminder = number % 2 #0
    if reminder==0: #false
        square = 0 - square
    print(square,end=' ')
    number=number+1
    

