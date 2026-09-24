shop_name = "Lower Manhattan"
number_of_drinks_sold = 1541
price_per_drink = 3.75
number_of_pastries_sold = 1031
price_per_pastry = 3.75
drink_revenue = number_of_drinks_sold * price_per_drink
pastry_revenue = number_of_pastries_sold * price_per_pastry
total_revenue = drink_revenue + pastry_revenue
sales_difference = number_of_drinks_sold - number_of_pastries_sold
revenue_difference = drink_revenue - pastry_revenue

file = open("sales_analysis.txt", "r")
written_analysis = file.read()
print(written_analysis)
file.close()

if total_revenue >= 500:
    print("Total revenue is at least $500.")
else:
    print("Total revenue is less than $500.")

print("Latte units sold:", number_of_drinks_sold)
print("Chocolate Croissant units sold:", number_of_pastries_sold)
print("Latte revenue: $", drink_revenue)
print("Chocolate Croissant revenue: $", pastry_revenue)
print("Sales difference:", sales_difference)
print("Revenue difference: $", revenue_difference)
