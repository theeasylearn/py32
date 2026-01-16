#write a program to findout profit or loss amount from user given purchase and sell price of project
#input purchase & sell price
purchase_price = float(input("Enter purchase price"))
sale_price = float(input("Enter sale price"))
#calculate difference
difference = sale_price - purchase_price

if difference>0:
    print("profit amount is ",difference)

if difference<0:
    print("loss amount is ",difference)

if difference==0:
    print("no loss no profit")

print("Good bye")