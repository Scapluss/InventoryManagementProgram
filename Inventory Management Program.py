# Step 1: Create the inventory
inventory = {}

# Add some items
inventory["apple"] = (10, 2.5)
inventory["banana"] = (20, 1.2)

# Step 2: Print welcome message and current inventory
print("Welcome to the Inventory Manager!")
print("Current inventory:")

for item in inventory:
    quantity = inventory[item][0]
    price = inventory[item][1]
    print(f"Item: {item}, Quantity: {quantity}, Price: ${price}")

# Step 3: Add a new item (mango)
print("Adding a new item: mango")
inventory["mango"] = (15, 3.0)

# Step 4: Print updated inventory
print("Updated inventory:")
for item in inventory:
    quantity = inventory[item][0]
    price = inventory[item][1]
    print(f"Item: {item}, Quantity: {quantity}, Price: ${price}")

# Step 5: Calculate total value
total_value = 0

for item in inventory:
    quantity = inventory[item][0]
    price = inventory[item][1]
    total_of_item = quantity * price
    total_value += total_of_item

print(f"Total value of inventory: ${total_value}")