inventory = []

def add_product(name, price, stock):
    if name == "":
        print("Error: Product name cannot be empty.")
        return
    for p in inventory:
        if p["name"].lower() == name.lower():
            print("Error: Product already exists!")
            return
    if price < 0 or stock < 0:
        print("Error: Price and stock cannot be negative.")
        return

    product = {
        "name": name,
        "price": price,
        "stock": stock
    }
    inventory.append(product)
    print("Added product:", name)

def search_product(name):
    for p in inventory:
        if p["name"].lower() == name.lower():
            print("Found:", p)
            return p
    print("Product not found.")
    return None

def update_price(name, new_price):
    if new_price < 0:
        print("Error: Price cannot be negative.")
        return
    
    p = search_product(name)
    if p:
        p["price"] = new_price
        print("Updated price for", name, "to", new_price)

def increase_stock(name, amount):
    if amount < 0:
        print("Error: Cannot add negative stock.")
        return
        
    p = search_product(name)
    if p:
        p["stock"] = p["stock"] + amount
        print("Increased stock for", name, "New stock:", p["stock"])

def sell_product(name, amount):
    if amount < 0:
        print("Error: Invalid sale amount.")
        return
        
    p = search_product(name)
    if p:
        if amount > p["stock"]:
            print("Error: Not enough stock available!")
        else:
            p["stock"] = p["stock"] - amount
            print("Sold", amount, "units of", name)

def calculate_total_inventory_value():
    total = 0
    for p in inventory:
        total = total + (p["price"] * p["stock"])
    print("Total inventory value:", total)
    return total

def generate_low_stock_report(threshold=5):
    print("\n--- Low Stock Report (Threshold:", threshold, ") ---")
    found = False
    for p in inventory:
        if p["stock"] < threshold:
            print("-", p["name"], "has only", p["stock"], "units left.")
            found = True
    if not found:
        print("No low stock products.")

add_product("Pen", 15, 10)
add_product("Notebook", 50, 3)
add_product("Eraser", 5, 20)

print("\n--- Testing Actions ---")
increase_stock("Pen", 5)
sell_product("Notebook", 2)
update_price("Eraser", 8)

calculate_total_inventory_value()
generate_low_stock_report()