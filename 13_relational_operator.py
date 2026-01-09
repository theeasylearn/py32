#concept of relational operators in python 
num1 = int(input("Enter value for num1"))
num2 =int(input("Enter value for num2"))

result = num1 == num2 # False 
print(f"{result} = {num1} == {num2}")

result = num1 != num2 # True 
print(f"{result} = {num1} != {num2}")

result = num1 < num2 # True 
print(f"{result} = {num1} < {num2}")

result = num1 > num2 # False 
print(f"{result} = {num1} > {num2}")

result = num1 <= num2 # True 
print(f"{result} = {num1} <= {num2}")

result = num1 >= num2 # False 
print(f"{result} = {num1} >= {num2}")