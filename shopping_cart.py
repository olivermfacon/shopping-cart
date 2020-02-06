import datetime

def to_usd(price):
    price_usd = "${0:.2f}".format(price)
    return price_usd


products = [
    {"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50},
    {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99},
    {"id":3, "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49},
    {"id":4, "name": "Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce", "department": "frozen", "aisle": "frozen meals", "price": 6.99},
    {"id":5, "name": "Green Chile Anytime Sauce", "department": "pantry", "aisle": "marinades meat preparation", "price": 7.99},
    {"id":6, "name": "Dry Nose Oil", "department": "personal care", "aisle": "cold flu allergy", "price": 21.99},
    {"id":7, "name": "Pure Coconut Water With Orange", "department": "beverages", "aisle": "juice nectars", "price": 3.50},
    {"id":8, "name": "Cut Russet Potatoes Steam N' Mash", "department": "frozen", "aisle": "frozen produce", "price": 4.25},
    {"id":9, "name": "Light Strawberry Blueberry Yogurt", "department": "dairy eggs", "aisle": "yogurt", "price": 6.50},
    {"id":10, "name": "Sparkling Orange Juice & Prickly Pear Beverage", "department": "beverages", "aisle": "water seltzer sparkling water", "price": 2.99},
    {"id":11, "name": "Peach Mango Juice", "department": "beverages", "aisle": "refrigerated", "price": 1.99},
    {"id":12, "name": "Chocolate Fudge Layer Cake", "department": "frozen", "aisle": "frozen dessert", "price": 18.50},
    {"id":13, "name": "Saline Nasal Mist", "department": "personal care", "aisle": "cold flu allergy", "price": 16.00},
    {"id":14, "name": "Fresh Scent Dishwasher Cleaner", "department": "household", "aisle": "dish detergents", "price": 4.99},
    {"id":15, "name": "Overnight Diapers Size 6", "department": "babies", "aisle": "diapers wipes", "price": 25.50},
    {"id":16, "name": "Mint Chocolate Flavored Syrup", "department": "snacks", "aisle": "ice cream toppings", "price": 4.50},
    {"id":17, "name": "Rendered Duck Fat", "department": "meat seafood", "aisle": "poultry counter", "price": 9.99},
    {"id":18, "name": "Pizza for One Suprema Frozen Pizza", "department": "frozen", "aisle": "frozen pizza", "price": 12.50},
    {"id":19, "name": "Gluten Free Quinoa Three Cheese & Mushroom Blend", "department": "dry goods pasta", "aisle": "grains rice dried goods", "price": 3.99},
    {"id":20, "name": "Pomegranate Cranberry & Aloe Vera Enrich Drink", "department": "beverages", "aisle": "juice nectars", "price": 4.25}
] # based on data from Instacart: https://www.instacart.com/datasets/grocery-shopping-2017

product_id_list = []
price_usd = ""
total_price = tax_expense = subtotal = 0
tax_rate = 0.0875
error_message = "You haver entered an invalid ID. Please try again."
divider = "------------------------------"
store_name = "PYTHON GROCERIES"
web_address = "www.pythongroceries.com"
phone = "+1(202)763-2634"
thank_you_note = "Thank you for choosing Python Groceries! Please come again soon."

while True:
    product_id = input("Please input a product identifier: ") 
    if product_id == "DONE":
        break
    elif product_id != "DONE" and not 1 <= product_id <= len(products):
        print(error_message)
    else:
        product_id_list.append(product_id)

print(divider)
print(store_name)
print(divider)
print("Web: " + web_address)
print("Phone: " + phone)
print("Checkout time: " + str(datetime.datetime.now()))
print(divider)
print("Shopping Cart Items: ")

for product_id in product_id_list:
    matching_products = [product for product in products if str(product["id"]) == str(product_id)]
    matching_product = matching_products[0]
    subtotal = subtotal + matching_product["price"]
    item_price = "(" + to_usd(matching_product["price"]) + ")"
    print(" + " + matching_product["name"] + " " + item_price)

print(divider)

tax_expense = subtotal * tax_rate
total_price = subtotal + tax_expense

# subtotal = " ${0:.2f}".format(subtotal)
# tax_expense = " ${0:.2f}".format(tax_expense)
# total_price = " ${0:.2f}".format(total_price)

print("SUBTOTAL: " + to_usd(subtotal))
print("Plus NYC Sales Tax (8.75%): " + to_usd(tax_expense))
print("TOTAL PRICE: " + to_usd(total_price))
print(divider)
print(thank_you_note)


# Write a program that asks the user to input one or more product identifiers, 
# then looks up the prices for each, then prints an itemized customer receipt 
# including the total amount owed.