
name = input("Enter patient name: ")
category = input("Enter patient category (normal/senior/insurance): ").lower()

consultation = float(input("Enter consultation fee: "))
diagnostic = float(input("Enter diagnostic charges: "))
treatment = float(input("Enter treatment cost: "))

total = consultation + diagnostic + treatment

if category == "senior":
    discount = total * 0.20
elif category == "insurance":
    discount = total * 0.30
else:
    discount = 0

payable = total - discount

minimum = 100
maximum = 5000

if payable < minimum:
    payable = minimum

if payable > maximum:
    payable = maximum

if payable <= 1000:
    tier = "Basic"
elif payable <= 3000:
    tier = "Standard"
else:
    tier = "Premium"

if payable == 0:
    status = "Fully Paid"
else:
    status = "Payment Required"

print("\n--- Hospital Billing Report ---")
print("Patient Name:", name)
print("Patient Category:", category)
print("Total Bill:", total)
print("Discount:", discount)
print("Final Payable:", payable)
print("Payment Tier:", tier)
print("Discharge Status:", status)
