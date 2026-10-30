bills = []

for month in range(1, 4):
    units = int(input("Enter units: "))

    if units <= 100:
        bill = units * 2
    else:
        bill = 100 * 2 + (units - 100) * 5

    bill = bill + 50
    bill = bill + bill * 0.05
    bill = bill - 20
    bills.append(bill)
    print("Electricity Bill:", bill)

for i in range(1, 3):
    if bills[i] > bills[i-1] * 1.2:
        print("Unusual increase in month", i+1)
