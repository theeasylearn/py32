person = {'name':'rahul sharma','age':40,'weight':74.22,'gender':True,'isMarried':False}
print(person)
print(person['name']) # rahul sharma
#update 
person['name'] = "mohal lal"

#we can add new key value pair 
person['city'] = 'Delhi'
person['pincode'] = 123456

#delete
del person['isMarried']
print(person)