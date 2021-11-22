print("Exercise 2: Sales Tax")
#Refactoring may be needed for lines 5-6 and 9-10. Unsure why I'm unable to do the calculations and formatting at the same time without getting an error.

price = float(input("Please enter the price of your product before tax? "))
priceFormatted = format(price,".2f") 
salesTax = int(input("What is the sales tax? "))
decimalSalesTax = salesTax * .01
salesTax_in_Dollars = price * decimalSalesTax
salesTax_in_Dollars_Formatted = format(salesTax_in_Dollars,".2f")
totalCost = format(price + salesTax_in_Dollars,".2f")

print(f"""
Price: ${priceFormatted}
Sales Tax: {salesTax}%
Sales Tax in Dollars: ${salesTax_in_Dollars_Formatted}
Total Cost: ${totalCost}""")
