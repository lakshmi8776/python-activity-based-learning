
name = input("Enter patient name: ")
consultation = int(input("Consultation charge: "))
diagnostic = int(input("Diagnostic charge: "))
treatment = int(input("Treatment charge: "))
payment = int(input("Enter payment amount: "))

total = consultation + diagnostic + treatment

if total >= 5000:
    total = total - total * 0.10

print("Final Bill:", total)

if payment < 0:
    print("Invalid payment")
elif payment >= total:
    print("Patient Classification: Paid")
else:
    print("Patient Classification: Pending")

print("Patient Name:", name)
print("Balance:", max(0, total - payment))
