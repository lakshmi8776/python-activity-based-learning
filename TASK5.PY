
budget = int(input("Enter your budget: "))
usage = int(input("Enter data usage in GB: "))
days = int(input("Enter required validity: "))
plans = [(199, 2, 28), (299, 3, 56), (399, 5, 84)]
best = None
for price, data, validity in plans:
    extra = max(0, usage - data) * 20
    total = price + extra

    if validity >= days and total <= budget:
        if best == None or total < best:
            best = total
            plan = price

if best != None:
    print("Best Plan:", plan)
    print("Total Cost:", best)
else:
    print("No suitable plan available")
