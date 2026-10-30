
n = int(input("Enter number of products: "))
total = 0
for i in range(n):
    name = input("Enter product name: ")
    price = float(input("Enter price: "))
    qty = int(input("Enter quantity: "))
    category = input("Enter category: ")
    amount = price * qty
    if amount >= 1000:
        discount = min(amount * 0.10, 200)
    else:
        discount = 0

    if category == "food":
        tax = 5
    else:
        tax = 10
    final = amount - discount
    final = final + final * tax / 100
    print(name, "Amount:", amount, "Discount:", discount, "Final:", final)
    total = total + final
print("Total Bill:", total)
