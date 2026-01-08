set1 = {1,2,3,4,5}
set2 = {4,5,6,7,8}
print(set1,set2)
#get unique values from both set (no repetation)
set3 = set1.union(set2)
print(set3)
#get common values from both set 
set4 = set1.intersection(set2)
print(set4)

#get all values that is in one(set1) set but not in other set (set2)
set5 = set1.difference(set2)
print(set5)

#create a list that has duplicate values 
numbers = [12, 18, 25, 31, 37, 42, 48, 53, 57, 61, 70, 74, 78, 82, 86, 92, 96, 99,12,18,48]
print(numbers)
print(len(numbers))
#remove all duplicate values 
unique_numbers = set(numbers) 
print(unique_numbers)