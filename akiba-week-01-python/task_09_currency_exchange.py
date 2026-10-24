usd = float(input("Enter amount in USD: "))
exchange_rate = 150
birr = usd * exchange_rate
msg= f'''
================================
    CURRENCY EXCHANGE
================================
USD Amount: ${usd:.2f}

Exchange Rate: 1 USD = 150 ETB

ETB Amount: {birr:.2f}birr
================================
'''
print(msg)
