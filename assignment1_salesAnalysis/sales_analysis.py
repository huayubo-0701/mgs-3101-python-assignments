shop_name = "Lower Manhattan"
number_of_drinks_sold = 1541
price_per_drink = 3.75
number_of_pastries_sold = 1031
price_per_pastry = 3.75
drink_revenue = number_of_drinks_sold * price_per_drink
pastry_revenue = number_of_pastries_sold * price_per_pastry

with open("sales_analysis.txt", "r") as file:
    written_analysis = file.read()
    print(written_analysis)
