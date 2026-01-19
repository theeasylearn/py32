# write a program to find out which is cheaper product to purchase from 2 product's weight and price. 
# also display how much cheaper per gram 
price1 = float(input('enter 1st product price'))
weight1 = float(input('enter 1st product weight'))

price2 = float(input('enter 2nd product price'))
weight2 = float(input('enter 2nd product weight'))

#calculate price per gram 
product1_price_per_gram = price1 / weight1
product2_price_per_gram = price2 / weight2 

if product1_price_per_gram<product2_price_per_gram:
    print("1st product is cheaper ",(product2_price_per_gram - product1_price_per_gram))
else:
    print("2nd product is cheaper ",(product1_price_per_gram - product2_price_per_gram))

print("Good bye....")