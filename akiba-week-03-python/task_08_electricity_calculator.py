def validate_units(units):
    if units < 0:
        print("Error: Units cannot be negative.")
        return False
    return True

def calculate_tier_charges(units):
    if units <= 50:
        charge = units * 0.50
    elif units <= 150:
        charge = (50 * 0.50) + ((units - 50) * 0.75)
    else:
        charge = (50 * 0.50) + (100 * 0.75) + ((units - 150) * 1.20)
    return charge

def calculate_total_bill(units, service_fee=0):
    if not validate_units(units):
        return 0
    
    electricity_cost = calculate_tier_charges(units)
    total = electricity_cost + service_fee
    return total

def generate_billing_summary(units, service_fee=0):
    if not validate_units(units):
        return
        
    electricity_cost = calculate_tier_charges(units)
    total = calculate_total_bill(units, service_fee)
    
    print("===== ELECTRICITY BILL =====")
    print("Units Used:", units)
    print("Electricity Cost:", electricity_cost, "Birr")
    if service_fee > 0:
        print("Service Fee:", service_fee, "Birr")
    print("Total Amount Due:", total, "Birr")
    print("============================")

generate_billing_summary(180, service_fee=10)