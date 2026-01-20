''' 
    write a program to calculate & display gross annual income, tax and net income from  given monthly income as per below income tax rule 
    ---------------------------------------------------------------------------------
    annual income                           Tax Rate
    Above Rs. 24,00,000                     30%
    From Rs. 20,00,001 to Rs. 24,00,000	    25%
    From Rs. 16,00,001 to Rs. 20,00,000	    20%
    From Rs. 12,00,000 to Rs. 16,00,000	    15%
    below 12,00,000                          0%

    steps 
    1) accept monthly income 
    2) calculate annual income 
    3) calculate tax as per rule
    4) calculate net income using gross annual income and tax 
    5) display gross income, tax, net income
'''   
monthly_income = float(input("Enter monthly income"))
gross_income = monthly_income * 12 #expression
tax = None 
if gross_income<1200000:
    tax = 0
elif gross_income>=1200000 and gross_income<=1600000:
    tax = gross_income * 0.15
elif gross_income>1600000 and gross_income<=2000000:
    tax = gross_income * 0.20
elif gross_income>2000000 and gross_income<=2400000:
    tax = gross_income * 0.25
else:
    tax = gross_income * 0.30

net_income = gross_income - tax 
print(f"gross income = {gross_income} tax = {tax} net income = {net_income}")



