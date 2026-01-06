nations = ("India", "United States", "China", "Russia", "Germany", "France", "Japan", "Brazil", "United Kingdom", "Australia","India","Sri lanka","India")
boxes = (100,True,1.25,'Bhavnagar',None)
print(nations) 
#display oth nation
print(nations[0])
#display 1st and 2nd and 3rd nation
print(nations[1:4])
#display all the items from 5th position onwards
print(nations[5:])
# nations[0] = "Bharat" #error tuple is immutable
#findout what is the position of russia in tuple
print("Position of Russia ",nations.index("Russia"))
print("Count of india ",nations.count("India"))
print("Count of Finland ",nations.count("Finland"))
# print("Position of Norway ",nations.index("Norway"))
print(nations*2)
print("good bye")
print(nations+boxes)