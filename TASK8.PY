
material = int(input("Enter material cost: "))
labour = int(input("Enter labour cost: "))
wastage = int(input("Enter wastage cost: "))
machine = int(input("Enter machine cost: "))
selling = int(input("Enter selling price: "))
target = int(input("Enter profit target: "))
cost = material + labour + wastage + machine
profit = selling - cost
print("Total Cost:", cost)
print("Profit:", profit)
if profit >= target:
    print("Profit Target Achieved")
else:
    print("Profit Target Not Achieved")
