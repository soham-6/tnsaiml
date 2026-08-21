'''
The Problem: Store Checkout System
You are building a backend system for a local grocery store. You are provided with a raw list of newly arrived inventory items. Each item in the list is a tuple containing (product_name, price, quantity). 
Your goal is to process this raw data, build a structured inventory, check product availability, and generate a customer receipt.
Given Input Data
Copy this raw list into your Python environment:
# Raw stock delivery data
raw_delivery = [
    ("Apple", 0.75, 50),
    ("Banana", 0.40, 100),
    ("Milk", 2.50, 15),
    ("Bread", 1.80, 20),
    ("Apple", 0.75, 30),  # Extra stock of apples arriving
]

# Customer shopping cart (List of products they want to buy)
shopping_cart = ["Apple", "Apple", "Milk", "Dragonfruit", "Bread"]
Your Tasks
1.	Build the Inventory (Dictionary):
Write a function to convert the raw_delivery list of tuples into a dictionary.
o	The keys must be the product names.
o	The values must be another dictionary containing {"price": float, "stock": int}.
o	Note: If a product appears more than once in the raw data (like "Apple"), sum up its stock quantities.
2.	Process the Shopping Cart:
Iterate through the shopping_cart list. Check your inventory dictionary for each item:
o	If the item exists and is in stock, decrease its stock by 1 and record the sale.
o	If the item exists but is out of stock, print a message: "[Product] is sold out!".
o	If the item does not exist in the inventory, print a message: "[Product] is not carried in this store". 
3.	Generate the Receipt (Tuple & List):
Create a list of tuples representing the customer's final receipt. Each tuple should be structured as (product_name, price). Print out the total price at the end.
'''

raw_delivery = [
    ("Apple", 0.75, 50),
    ("Banana", 0.40, 100),
    ("Milk", 2.50, 15),
    ("Bread", 1.80, 20),
    ("Apple", 0.75, 30),  # Extra stock of apples arriving
]

shopping_cart = ["Apple", "Apple", "Milk", "Dragonfruit", "Bread"]

def build_inventory(delivery_data):
    inventory = {}
    for prod, price, stock in delivery_data:
        if prod in inventory:
            inventory[prod]["stock"] += stock
        else:
            inventory[prod] = {"price": price, "stock": stock}
    return inventory

def process_cart(cart, inventory):
    receipt = []
    
    for item in cart:
        if item not in inventory:
            print(f"{item} is not carried in this store")
        elif inventory[item]["stock"] == 0:
            print(f"{item} is sold out")
        else:
            inventory[item]["stock"] -= 1
            item_price = inventory[item]["price"]
            receipt.append((item, item_price))           
    return receipt

inventory_dict = build_inventory(raw_delivery)
print("Inventory:")
print(inventory_dict)

print()
receipt = process_cart(shopping_cart, inventory_dict)

print("\nCustomer Receipt")
total_price = 0
for product, price in receipt:
    print(f"{product}: ${price:.2f}")
    total_price += price
print(f"Total: ${total_price:.2f}")