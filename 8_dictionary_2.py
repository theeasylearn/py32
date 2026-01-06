#example of dictionary 2
book = {}
print(book)
book['name'] = 'Atomic habit'
book['author'] = 'James clear'
book['price'] = 499
print(book)

#add tuple into dictionary
book['chapters'] = (1,2,3,4,5)
book['topics'] = ['abc','bcd','cde','xyz']
print(book)
#display only 1st chapter 
print(book['chapters'][0])
print(book['chapters'][1])
#print 2nd topics
print(book['topics'][2])
book['topics'][2] = 'aabbcc'
# book['chapters'][2] = 10
print(book)
