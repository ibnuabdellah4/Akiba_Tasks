def check_min_length(password, min_length=8):
    if len(password) >= min_length:
        return True, f"Pass: Meets minimum length of {min_length}."
    else:
        return False, f"Fail: Too short (needs at least {min_length} characters)."

def check_uppercase(password):
    has_upper = False
    for char in password:
        if char.isupper():
            has_upper = True
            break
            
    if has_upper:
        return True, "Pass: Contains uppercase letter."
    else:
        return False, "Fail: Missing uppercase letter."

def check_lowercase(password):
    has_lower = False
    for char in password:
        if char.islower():
            has_lower = True
            break
            
    if has_lower:
        return True, "Pass: Contains lowercase letter."
    else:
        return False, "Fail: Missing lowercase letter."

def check_digit(password):
    has_digit = False
    for char in password:
        if char.isdigit():
            has_digit = True
            break
            
    if has_digit:
        return True, "Pass: Contains a digit."
    else:
        return False, "Fail: Missing a digit."

def check_special(password):
    special_chars = "!@#$%^&*()_+-=[]{}\\|;':\",./<>?"
    has_special = False
    for char in password:
        if char in special_chars:
            has_special = True
            break
            
    if has_special:
        return True, "Pass: Contains special character."
    else:
        return False, "Fail: Missing special character."

def analyze_password(password, min_length=8):
    report = []
    
    # Collect results from all checks without stopping early
    report.append(check_min_length(password, min_length))
    report.append(check_uppercase(password))
    report.append(check_lowercase(password))
    report.append(check_digit(password))
    report.append(check_special(password))
    
    return report

# Testing with 5 fictional passwords
passwords_to_test = [
    "password",
    "Password1",
    "P@ssw0rd123",
    "short",
    "A1!b"
]

print("--- Password Analysis Report ---")
for pwd in passwords_to_test:
    print(f"\nPassword: '{pwd}'")
    results = analyze_password(pwd)
    for passed, message in results:
        print("  *", message)