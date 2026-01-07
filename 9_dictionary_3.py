person = {'name':'rahul sharma','age':40,'weight':74.22,'gender':True,'isMarried':False}
print(person)
print(person['name']) # rahul sharma
print(person.get('age')) # 40
print(person.get('city')) #error
# person2 = person #bad way
person2 = person.copy()
person2.clear() # remove all key value pair from person2
print(person,person2)
#display only keys
print(person.keys()) # name age weight gender isMarried
print(person.values()) #rahul sharma 40 74.22 True False
print(person.items())
book = ['name','author','pages','price','isbnno']
python_book = dict.fromkeys(book)
print(python_book)
python_book['name'] = "Mastering Python" #update
python_book['author'] = "the easylearn" #update
python_book['publisher'] = "ABC" #create
print("now python book has",python_book)
python_book.pop('price')
python_book.pop('country',False)
python_book.popitem() #remove last key value pair
# person2.popitem() #error
print(python_book)
print("good bye")
