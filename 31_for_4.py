#for loop with string
# count vowels  
line = input("What is your name")
vowels = ['a','e','i','o','u']
count = 0
for letter in line:
     if str.lower(letter) in vowels:
          count+=1
        
print(count)
    
