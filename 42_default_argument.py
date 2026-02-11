#default argument function
# write a program that will return total inches of given meter, foot, inches 
def getInches(meter,foot=0,inches=0):
    print(f"meter = {meter} foot = {foot} inches = {inches}")
    totalInches = meter * 39.3701
    totalInches = totalInches + (foot * 12) + inches
    return totalInches

print(getInches(10,5,7))
print(getInches(10,5))
print(getInches(10))
print("good bye")
