
budget = float(input("Enter budget in INR: "))
categories = ["Food", "Travel", "Shopping"]
rates = [83, 90, 1]
expenses = []
for i in range(3):
    amount = float(input("Enter " + categories[i] + " expense: "))
    cost = amount * rates[i]
    cost = cost + cost * 0.02
    expenses.append(cost)
total = sum(expenses)
print("Total Expense:", total)
print("Largest Expense:", categories[expenses.index(max(expenses))])
if total <= budget:
    print("Within Budget")
else:
    print("Over Budget")
