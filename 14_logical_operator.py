#logical operators 
num1 = 100
num2 = 200 
num3 = 300 
# AND or OR
result = num1 < num2 and num2<num3
print(f"{result} = {num1} < {num2} and {num2}<{num3}")

result = num1 < num2 and num2>num3
print(f"{result} = {num1} < {num2} and {num2}>{num3}")

result = num1 < num2 or num2>num3
print(f"{result} = {num1} < {num2} or {num2}>{num3}")

result = num1 > num2 or num2>num3
print(f"{result} = {num1} > {num2} or {num2}>{num3}")

result = not (num1 > num2 or num2>num3)
print(f"{result} = not {num1} > {num2} or {num2}>{num3}")