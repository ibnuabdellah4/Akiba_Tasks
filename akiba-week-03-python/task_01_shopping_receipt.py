def calculate_subtotal(items):
    total = 0
    for item in items:
        if item["price"] < 0 or item["quantity"] < 0:
            return "Error: Price and quantity cannot be negative."
        total += item["price"] * item["quantity"]
    return total

def calculate_discount(subtotal):
    if subtotal >= 3000:
        return subtotal * 0.1
    elif 1000 <= subtotal < 3000:
        return subtotal * 0.05
    else:
        return 0

def calculate_tax(amount, tax_rate):
    if tax_rate < 0 or tax_rate > 1:
        return "Error: Invalid tax rate."
    return amount * tax_rate

def generate_receipt(items, tax_rate):
    subtotal = calculate_subtotal(items)
    
    
    if isinstance(subtotal, str):
        return subtotal
        
    discount = calculate_discount(subtotal)
    discounted_amount = subtotal - discount
    
    tax = calculate_tax(discounted_amount, tax_rate)
    

    if isinstance(tax, str):
        return tax
    
    final_total = discounted_amount + tax
    
    receipt = {
        "Subtotal": subtotal,
        "Discount": discount,
        "Tax": tax,
        "Total": final_total
    }
    return receipt

items = [
    {"name": "Notebook", "price": 800, "quantity": 3},
    {"name": "Pen", "price": 15, "quantity": 5}
]

print(generate_receipt(items, 0.15))