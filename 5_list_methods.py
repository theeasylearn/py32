fruits = ["apple", "banana", "apple", "orange", "mango", "banana", "grape", "apple", "kiwi", "orange"]
print(fruits)
#findout how many apples
print(fruits.count('apple'))
#findout how many banana
print(fruits.count('banana'))
print(fruits.count('cherry'))
#position of orange
print(fruits.index('orange'))
#position of kiwi
print(fruits.index('kiwi'))
# print(fruits.index('cherry')) error, because item not found

# fruits2 = fruits #mirror copy, means it create referernce of fruits
fruits2 = fruits.copy() #perfect way
print(fruits,fruits2)

fruits2.clear() 
print(fruits,fruits2)

