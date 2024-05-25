# filename: bill_and_tax_calculator.py

# Function to calculate the total amount including tax
def calculate_total_bill_amount(subtotal, tax_rate):
    tax_amount = subtotal * tax_rate
    total_amount = subtotal + tax_amount
    return total_amount

# Asking the user for input
subtotal = float(input("Enter the subtotal amount: $"))
tax_rate = float(input("Enter the tax rate (in decimal form): "))

# Calculating the total bill amount
total_bill = calculate_total_bill_amount(subtotal, tax_rate)

# Displaying the total bill amount
print(f"Total bill amount including tax: ${total_bill}")