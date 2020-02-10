import datetime 

def to_usd(price):
    return "${0:.2f}".format(price)

products = [
    {"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50, "price_per_pound": 0},
    {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99, "price_per_pound": 0},
    {"id":3, "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49, "price_per_pound": 0},
    {"id":4, "name": "Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce", "department": "frozen", "aisle": "frozen meals", "price": 6.99, "price_per_pound": 0},
    {"id":5, "name": "Green Chile Anytime Sauce", "department": "pantry", "aisle": "marinades meat preparation", "price": 7.99, "price_per_pound": 0},
    {"id":6, "name": "Dry Nose Oil", "department": "personal care", "aisle": "cold flu allergy", "price": 21.99, "price_per_pound": 0},
    {"id":7, "name": "Pure Coconut Water With Orange", "department": "beverages", "aisle": "juice nectars", "price": 3.50, "price_per_pound": 0},
    {"id":8, "name": "Cut Russet Potatoes Steam N' Mash", "department": "frozen", "aisle": "frozen produce", "price": 4.25, "price_per_pound": 0},
    {"id":9, "name": "Light Strawberry Blueberry Yogurt", "department": "dairy eggs", "aisle": "yogurt", "price": 6.50, "price_per_pound": 0},
    {"id":10, "name": "Sparkling Orange Juice & Prickly Pear Beverage", "department": "beverages", "aisle": "water seltzer sparkling water", "price": 2.99, "price_per_pound": 0},
    {"id":11, "name": "Peach Mango Juice", "department": "beverages", "aisle": "refrigerated", "price": 1.99, "price_per_pound": 0},
    {"id":12, "name": "Chocolate Fudge Layer Cake", "department": "frozen", "aisle": "frozen dessert", "price": 18.50, "price_per_pound": 0},
    {"id":13, "name": "Saline Nasal Mist", "department": "personal care", "aisle": "cold flu allergy", "price": 16.00, "price_per_pound": 0},
    {"id":14, "name": "Fresh Scent Dishwasher Cleaner", "department": "household", "aisle": "dish detergents", "price": 4.99, "price_per_pound": 0},
    {"id":15, "name": "Overnight Diapers Size 6", "department": "babies", "aisle": "diapers wipes", "price": 25.50, "price_per_pound": 0},
    {"id":16, "name": "Mint Chocolate Flavored Syrup", "department": "snacks", "aisle": "ice cream toppings", "price": 4.50, "price_per_pound": 0},
    {"id":17, "name": "Rendered Duck Fat", "department": "meat seafood", "aisle": "poultry counter", "price": 9.99, "price_per_pound": 0},
    {"id":18, "name": "Pizza for One Suprema Frozen Pizza", "department": "frozen", "aisle": "frozen pizza", "price": 12.50, "price_per_pound": 0},
    {"id":19, "name": "Gluten Free Quinoa Three Cheese & Mushroom Blend", "department": "dry goods pasta", "aisle": "grains rice dried goods", "price": 3.99, "price_per_pound": 0},
    {"id":20, "name": "Pomegranate Cranberry & Aloe Vera Enrich Drink", "department": "beverages", "aisle": "juice nectars", "price": 4.25, "price_per_pound": 0},
    {"id":21, "name": "Organic Bananas", "price": 0, "price_per_pound": 0.79}, # Organic Bananas and Apples were added for the extra challenges section
    {"id":22, "name": "Organic Apples", "price": 0, "price_per_pound": 0.6}
] # based on data from Instacart: https://www.instacart.com/datasets/grocery-shopping-2017

num_pounds_items = []
product_id_list = []
total_price = tax_expense = subtotal = 0
tax_rate = 0.0875
divider = "------------------------------"
error_message = "You haver entered an invalid ID. Please try again."
store_name = "PYTHON GROCERIES"
web_address = "www.pythongroceries.com"
phone = "+1(202)763-2634"
thank_you_note = "Thank you for choosing Python Groceries! Please come again soon."

while True:
    match = False
    product_id = input("Please input a product identifier: ") 
    if type(product_id) == str:
        product_id = product_id.lower().title() 
    if product_id == "Done":
        break
    elif not 1 <= product_id <= len(products):
        print(error_message)
    else:
        count = 0
        if products[product_id-1]["price_per_pound"] > 0:
                weight = input("Enter the amount of " + products[product_id-1]["name"] + " in pounds: ")
        for ident in product_id_list:
            if product_id == ident: 
                match = True
                if products[product_id-1]["price_per_pound"] > 0:
                    num_pounds_items[count] += weight
                    products[product_id-1]["price"] = products[product_id-1]["price_per_pound"] * num_pounds_items[count]
                else:
                    num_pounds_items[count] += 1
            count += 1
        if match == False:
            product_id_list.append(product_id)
            if products[product_id-1]["price_per_pound"] == 0:
                num_pounds_items.append(1) 
            else:
                num_pounds_items.append(weight)
                products[product_id-1]["price"] = products[product_id-1]["price_per_pound"] * num_pounds_items[count]
        
        
print(divider)
print(store_name)
print(divider)
print("Web: " + web_address)
print("Phone: " + phone)
print("Checkout Time: " + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))) # https://stackoverflow.com/questions/7999935/python-datetime-to-string-without-microsecond-component
print(divider)
print("Shopping Cart Items: ")

count = 0

for product_id in product_id_list:
    matching_products = [product for product in products if str(product["id"]) == str(product_id)]
    matching_product = matching_products[0]
    subtotal = subtotal + matching_product["price"]
    item_price = "(" + to_usd(matching_product["price"]) + ")"
    if matching_product["price_per_pound"] > 0:
        print(" + (" + str(num_pounds_items[count]) + "lbs) " + matching_product["name"] + " " + item_price)
    elif num_pounds_items[count] > 1:
        print(" + " + str(num_pounds_items[count]) + "x " + matching_product["name"] + " " + item_price)
    else:
        print(" + " + matching_product["name"] + " " + item_price)
    count += 1 

print(divider)

tax_expense = subtotal * tax_rate
total_price = subtotal + tax_expense

print("SUBTOTAL: " + to_usd(subtotal))
print("Plus NYC Sales Tax (8.75%): " + to_usd(tax_expense))
print("TOTAL PRICE: " + to_usd(total_price))
print(divider)
print(thank_you_note)
print(divider)

















