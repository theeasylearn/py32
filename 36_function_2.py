import shutil as st 
width = st.get_terminal_size().columns
# 1	 Without return value without argument
def printLine():
    print('_' * width)
# 2	Without return value with argument 
def printMessage(message): #print message in center
    print(message.center(width))
# 3	 With return value without argument
def getPi():
    #local variable
    pi = 22/7
    return pi 
printLine() #call function
printMessage('THE EASYLEARN')
printLine()
#normal variable
pi = getPi()
print("pi =",pi)