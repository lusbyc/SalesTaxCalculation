print("Exercise 2: Sales Tax")
#Refactoring may be needed for lines 5-6 and 9-10. Unsure why I'm unable to do the calculations and formatting at the same time without getting an error.

price = float(input("Please enter the price of your product before tax? "))
price_formatted = format(price,".2f") 
sales_tax = int(input("What is the sales tax? "))
decimal_sales_tax = sales_tax * .01
sales_tax_in_dollars = price * decimal_sales_tax
sales_tax_in_dollars_formatted = format(sales_tax_in_dollars,".2f")
total_cost = format(price + sales_tax_in_dollars,".2f")

print(f"""
Price: ${price_formatted}
Sales Tax: {sales_tax}%
Sales Tax in Dollars: ${sales_tax_in_dollars_formatted}
Total Cost: ${total_cost}""")
