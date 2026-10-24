customer_name = input("Enter customer name: ")
product_name = input("Enter product name: ")
product_price = float(input("Enter product price: "))
quantity = int(input("Enter quantity: "))
total_price = product_price * quantity
receipt = f'''
=========================
     RECEIPT
=========================
Customer: {customer_name}
Product    Price    Qty
-------------------------
{product_name}    {product_price:.2f}    {quantity}
-------------------------
Total: {total_price:.2f} birr

Thank you for shopping!
=========================
'''
print(receipt)
