# list means array 
#create list to store many students marks 
marks = [50,60,70,55,65,75,40,99,88]
kit = ['books',500,1.5,True,False,None]
print(marks)
print(kit)

#list is mutable (we can add, delete, modify, access any part of list)
#add new item 'Compass' at 0th position
kit.insert(0,'compass')
#add new item 100 at 1st position
kit.insert(1,100)
#add item at last position
kit.append("Lunch box")
print("now kit has ",kit)
#how to update item 
kit[0] = "Water bottle"
print(kit)
#how to delete item 
#delete 1st item 
del kit[1]
print(kit)
#delete by value 
kit.remove('books')
kit.remove(True)
# kit.remove('pencil') #error, because item does not exist in list
print(kit)
kit.pop(2) #remove 2nd item in list
print(kit)
#print 0th student marks
print(marks[0]) #50\
#print 3 students marks from begining
print(marks[0:3]) #50 60 70
#print all items from 4th position
print(marks[4:]) #[65, 75, 40, 99, 88]
#delete whole list
del marks
print(marks)