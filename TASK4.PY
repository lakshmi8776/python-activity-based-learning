
name = input("Enter employee name: ")
basic = int(input("Enter basic pay: "))
allowance = int(input("Enter allowances: "))
overtime = int(input("Enter overtime pay: "))
incentive = int(input("Enter incentives: "))
gross = basic + allowance + overtime + incentive
if gross > 30000:
    deduction = gross * 0.10
else:
    deduction = gross * 0.05
net = gross - deduction
print("\n--- Salary Statement ---")
print("Employee Name:", name)
print("Gross Salary:", gross)
print("Deduction:", deduction)
print("Net Salary:", net)
