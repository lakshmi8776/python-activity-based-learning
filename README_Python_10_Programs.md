# Python Programs -- 10 Problem Statements

**Note:** These are beginner-friendly examples. Rates, limits, and
policies are assumed for practice and can be changed as required.

------------------------------------------------------------------------

## 1. University Scholarship Allocation

### Problem Statement

Evaluate students using aggregate marks, subject marks, attendance, and
family income. Display eligible students in rank order. If aggregate
marks are equal, higher attendance gets the higher rank.

### Algorithm

1.  Read the number of students.
2.  Read each student's name, aggregate marks, subject marks,
    attendance, and income.
3.  Check all eligibility conditions.
4.  Store eligible students.
5.  Sort by aggregate marks, then attendance.
6.  Display the ranked list.

### Flowchart

``` mermaid
flowchart TD
    A([Start]) --> B[Enter student details]
    B --> C{Meets all eligibility rules?}
    C -->|Yes| D[Add student to eligible list]
    C -->|No| E[Skip student]
    D --> F{More students?}
    E --> F
    F -->|Yes| B
    F -->|No| G[Sort by marks and attendance]
    G --> H[Display ranking]
    H --> I([Stop])
```

### Source Code

``` python
n = int(input("Number of students: "))
eligible = []

for i in range(n):
    name = input("Name: ")
    marks = int(input("Aggregate marks: "))
    subject = int(input("Minimum subject marks: "))
    attendance = int(input("Attendance: "))
    income = int(input("Family income: "))

    if marks >= 75 and subject >= 40 and attendance >= 75 and income <= 200000:
        eligible.append((name, marks, attendance))

eligible.sort(key=lambda x: (x[1], x[2]), reverse=True)

print("Eligible students:")
for s in eligible:
    print(s[0], s[1], s[2])
```

### Sample Input

``` text
Number of students: 2
Name: Ravi
Aggregate marks: 85
Minimum subject marks: 60
Attendance: 90
Family income: 150000
Name: Rani
Aggregate marks: 90
Minimum subject marks: 70
Attendance: 95
Family income: 180000
```

### Sample Output

``` text
Eligible students:
Rani 90 95
Ravi 85 90
```

------------------------------------------------------------------------

## 2. Progressive Electricity Billing

### Problem Statement

Calculate monthly electricity bills using two consumption slabs, fixed
charges, surcharge, and rebate. Compare bills and identify increases
greater than 20%.

### Algorithm

1.  Read electricity units for three months.
2.  Calculate slab charges.
3.  Add fixed charge and 5% surcharge.
4.  Subtract the rebate.
5.  Store and display each bill.
6.  Identify increases greater than 20% from the previous month.

### Flowchart

``` mermaid
flowchart TD
    A([Start]) --> B[Enter monthly units]
    B --> C{Units <= 100?}
    C -->|Yes| D[Charge units at rate 2]
    C -->|No| E[First 100 at 2 and remaining at 5]
    D --> F[Add fixed charge and surcharge]
    E --> F
    F --> G[Subtract rebate and store bill]
    G --> H{More months?}
    H -->|Yes| B
    H -->|No| I[Compare consecutive bills]
    I --> J[Display bills and unusual increases]
    J --> K([Stop])
```

### Source Code

``` python
bills = []

for month in range(1, 4):
    units = int(input("Enter units: "))

    if units <= 100:
        charge = units * 2
    else:
        charge = 100 * 2 + (units - 100) * 5

    bill = (charge + 50) * 1.05 - 20
    bills.append(bill)
    print("Bill:", round(bill, 2))

for i in range(1, 3):
    if bills[i] > bills[i - 1] * 1.20:
        print("Unusual increase in month", i + 1)
```

### Sample Input

``` text
Enter units: 80
Enter units: 120
Enter units: 200
```

### Sample Output

``` text
Bill: 198.0
Bill: 408.0
Bill: 828.0
Unusual increase in month 2
Unusual increase in month 3
```

------------------------------------------------------------------------

## 3. Hospital Billing and Patient Classification

### Problem Statement

Calculate consultation, diagnostic, and treatment charges. Give a 10%
concession when the bill is at least ₹5,000, validate payment, and
classify the patient as Paid or Pending.

### Algorithm

1.  Read patient name and three charges.
2.  Check that charges and payment are not negative.
3.  Calculate the total bill.
4.  Apply a 10% concession if the bill is at least ₹5,000.
5.  Compare payment with the final bill.
6.  Display bill, status, and balance.

### Flowchart

``` mermaid
flowchart TD
    A([Start]) --> B[Enter patient charges and payment]
    B --> C{Any value negative?}
    C -->|Yes| D[Display invalid billing details]
    C -->|No| E[Add all charges]
    E --> F{Total >= 5000?}
    F -->|Yes| G[Apply 10 percent concession]
    F -->|No| H[Keep total bill]
    G --> I[Calculate final bill]
    H --> I
    I --> J{Payment >= final bill?}
    J -->|Yes| K[Paid]
    J -->|No| L[Pending]
    K --> M[Display bill and balance]
    L --> M
    D --> N([Stop])
    M --> N
```

### Source Code

``` python
name = input("Patient name: ")
consult = float(input("Consultation charge: "))
diagnostic = float(input("Diagnostic charge: "))
treatment = float(input("Treatment charge: "))
payment = float(input("Payment: "))

if min(consult, diagnostic, treatment, payment) < 0:
    print("Invalid billing details")
else:
    total = consult + diagnostic + treatment

    if total >= 5000:
        total = total * 0.90

    balance = max(0, total - payment)

    if payment >= total:
        status = "Paid"
    else:
        status = "Pending"

    print("Patient:", name)
    print("Final Bill:", round(total, 2))
    print("Status:", status)
    print("Balance:", round(balance, 2))
```

### Sample Input

``` text
Patient name: Ravi
Consultation charge: 1000
Diagnostic charge: 2000
Treatment charge: 3000
Payment: 4000
```

### Sample Output

``` text
Patient: Ravi
Final Bill: 5400.0
Status: Pending
Balance: 1400.0
```

------------------------------------------------------------------------

## 4. Employee Payroll and Deduction Analysis

### Problem Statement

Calculate gross salary from basic pay, allowances, overtime, and
incentives. Apply a simple progressive deduction: 5% on the first
₹30,000 and 10% on the amount above ₹30,000.

### Algorithm

1.  Read employee details and salary components.
2.  Calculate gross salary.
3.  Calculate deduction using the two salary slabs.
4.  Calculate net salary.
5.  Display the salary statement.

### Flowchart

``` mermaid
flowchart TD
    A([Start]) --> B[Enter salary components]
    B --> C[Calculate gross salary]
    C --> D{Gross salary <= 30000?}
    D -->|Yes| E[Deduction = 5 percent of gross]
    D -->|No| F[Deduct 5 percent on 30000 and 10 percent on balance]
    E --> G[Calculate net salary]
    F --> G
    G --> H[Display salary statement]
    H --> I([Stop])
```

### Source Code

``` python
name = input("Employee name: ")
basic = float(input("Basic pay: "))
allowance = float(input("Allowances: "))
overtime = float(input("Overtime pay: "))
incentive = float(input("Incentives: "))

gross = basic + allowance + overtime + incentive

if gross <= 30000:
    deduction = gross * 0.05
else:
    deduction = 30000 * 0.05 + (gross - 30000) * 0.10

net = gross - deduction

print("Employee:", name)
print("Gross Salary:", round(gross, 2))
print("Deduction:", round(deduction, 2))
print("Net Salary:", round(net, 2))
```

### Sample Input

``` text
Employee name: Ravi
Basic pay: 20000
Allowances: 5000
Overtime pay: 2000
Incentives: 3000
```

### Sample Output

``` text
Employee: Ravi
Gross Salary: 30000.0
Deduction: 1500.0
Net Salary: 28500.0
```

------------------------------------------------------------------------

## 5. Multi-Plan Telecommunications Cost Optimization

### Problem Statement

Compare mobile plans using data usage, validity, and budget. Add an
excess-data charge and select the lowest-cost plan that meets the
requirements.

### Algorithm

1.  Read required data, validity, and budget.
2.  Store available plan details.
3.  Calculate excess-data charges for each plan.
4.  Check validity and budget.
5.  Select the eligible plan with the lowest total cost.
6.  Display the selected plan or a no-plan message.

### Flowchart

``` mermaid
flowchart TD
    A([Start]) --> B[Enter usage, validity and budget]
    B --> C[Check each mobile plan]
    C --> D[Calculate excess data charge]
    D --> E{Validity and budget satisfied?}
    E -->|Yes| F{Cheaper than current best?}
    E -->|No| G[Skip plan]
    F -->|Yes| H[Save this plan]
    F -->|No| G
    H --> I{More plans?}
    G --> I
    I -->|Yes| C
    I -->|No| J[Display cheapest eligible plan]
    J --> K([Stop])
```

### Source Code

``` python
budget = int(input("Budget: "))
usage = int(input("Data needed in GB: "))
days = int(input("Validity needed in days: "))

plans = [(199, 2, 28), (299, 3, 56), (399, 5, 84)]
best_cost = None

for price, data, validity in plans:
    extra = max(0, usage - data) * 20
    total = price + extra

    if validity >= days and total <= budget:
        if best_cost is None or total < best_cost:
            best_cost = total
            best_plan = price

if best_cost is None:
    print("No suitable plan")
else:
    print("Best Plan Price:", best_plan)
    print("Total Cost:", best_cost)
```

### Sample Input

``` text
Budget: 400
Data needed in GB: 3
Validity needed in days: 28
```

### Sample Output

``` text
Best Plan Price: 299
Total Cost: 299
```

------------------------------------------------------------------------

## 6. Railway Fare and Reservation Calculator

### Problem Statement

Calculate fares for multiple passengers using distance slabs, travel
class, senior-citizen concession, reservation fee, and cancellation
penalty.

### Algorithm

1.  Read the number of passengers.
2.  Read each passenger's name, age, distance, and class.
3.  Calculate distance-based fare.
4.  Add AC charge if applicable.
5.  Apply senior-citizen concession.
6.  Add reservation fee.
7.  Apply cancellation penalty if cancelled.
8.  Display each passenger's fare.

### Flowchart

``` mermaid
flowchart TD
    A([Start]) --> B[Enter passenger details]
    B --> C[Calculate distance fare]
    C --> D{AC class?}
    D -->|Yes| E[Add AC charge]
    D -->|No| F[Continue]
    E --> G{Age >= 60?}
    F --> G
    G -->|Yes| H[Apply 50 percent concession]
    G -->|No| I[No concession]
    H --> J[Add reservation fee]
    I --> J
    J --> K{Ticket cancelled?}
    K -->|Yes| L[Apply 50 percent cancellation penalty]
    K -->|No| M[Display fare]
    L --> M
    M --> N{More passengers?}
    N -->|Yes| B
    N -->|No| O([Stop])
```

### Source Code

``` python
n = int(input("Number of passengers: "))

for i in range(n):
    name = input("Passenger name: ")
    age = int(input("Age: "))
    distance = int(input("Distance in km: "))
    cls = input("Class (Sleeper/AC): ")

    if distance <= 100:
        fare = distance
    else:
        fare = 100 + (distance - 100) * 2

    if cls == "AC":
        fare = fare + 200

    if age >= 60:
        fare = fare * 0.50

    fare = fare + 50
    cancel = input("Cancel ticket? (yes/no): ")

    if cancel == "yes":
        fare = fare * 0.50

    print(name, "Final Fare:", round(fare, 2))
```

### Sample Input

``` text
Number of passengers: 1
Passenger name: Ravi
Age: 65
Distance in km: 150
Class (Sleeper/AC): AC
Cancel ticket? (yes/no): no
```

### Sample Output

``` text
Ravi Final Fare: 250.0
```

------------------------------------------------------------------------

## 7. Retail Billing with Multiple Discount Rules

### Problem Statement

Process multiple products using price, quantity, category tax, threshold
discount, and a maximum discount limit. Display an itemized bill.

### Algorithm

1.  Read the number of products.
2.  Read product name, price, quantity, and category.
3.  Calculate item amount.
4.  Apply 10% discount when amount is at least ₹1,000, with a maximum
    discount of ₹200.
5.  Apply category tax.
6.  Display each item total and the grand total.

### Flowchart

``` mermaid
flowchart TD
    A([Start]) --> B[Enter product details]
    B --> C[Calculate price times quantity]
    C --> D{Amount >= 1000?}
    D -->|Yes| E[Apply 10 percent discount up to 200]
    D -->|No| F[No discount]
    E --> G{Food category?}
    F --> G
    G -->|Yes| H[Apply 5 percent tax]
    G -->|No| I[Apply 10 percent tax]
    H --> J[Calculate final item amount]
    I --> J
    J --> K[Add to grand total]
    K --> L{More products?}
    L -->|Yes| B
    L -->|No| M[Display grand total]
    M --> N([Stop])
```

### Source Code

``` python
n = int(input("Number of products: "))
total = 0

for i in range(n):
    name = input("Product name: ")
    price = float(input("Price: "))
    qty = int(input("Quantity: "))
    category = input("Category (food/other): ")

    amount = price * qty

    if amount >= 1000:
        discount = min(amount * 0.10, 200)
    else:
        discount = 0

    tax_rate = 5 if category == "food" else 10
    final = (amount - discount) * (1 + tax_rate / 100)

    print(name, "Final Amount:", round(final, 2))
    total = total + final

print("Total Bill:", round(total, 2))
```

### Sample Input

``` text
Number of products: 2
Product name: Rice
Price: 500
Quantity: 2
Category (food/other): food
Product name: Bag
Price: 800
Quantity: 1
Category (food/other): other
```

### Sample Output

``` text
Rice Final Amount: 945.0
Bag Final Amount: 880.0
Total Bill: 1825.0
```

------------------------------------------------------------------------

## 8. Manufacturing Cost and Profitability Analysis

### Problem Statement

Calculate production cost using material, labour, wastage, and machine
costs. Compare profit with a given profit target.

### Algorithm

1.  Read all production costs.
2.  Read selling price and profit target.
3.  Calculate total production cost.
4.  Calculate profit.
5.  Check whether profit meets the target.
6.  Display the result.

### Flowchart

``` mermaid
flowchart TD
    A([Start]) --> B[Enter production costs]
    B --> C[Calculate total cost]
    C --> D[Enter selling price and target]
    D --> E[Calculate profit]
    E --> F{Profit >= target?}
    F -->|Yes| G[Target achieved]
    F -->|No| H[Target not achieved]
    G --> I[Display cost and profit]
    H --> I
    I --> J([Stop])
```

### Source Code

``` python
material = float(input("Material cost: "))
labour = float(input("Labour cost: "))
wastage = float(input("Wastage cost: "))
machine = float(input("Machine cost: "))
selling = float(input("Selling price: "))
target = float(input("Profit target: "))

cost = material + labour + wastage + machine
profit = selling - cost

print("Total Cost:", cost)
print("Profit:", profit)

if profit >= target:
    print("Profit Target Achieved")
else:
    print("Profit Target Not Achieved")
```

### Sample Input

``` text
Material cost: 5000
Labour cost: 2000
Wastage cost: 500
Machine cost: 1000
Selling price: 10000
Profit target: 1000
```

### Sample Output

``` text
Total Cost: 8500.0
Profit: 1500.0
Profit Target Achieved
```

------------------------------------------------------------------------

## 9. Multi-Currency Travel Budget Analysis

### Problem Statement

Convert travel expenses into Indian Rupees using supplied exchange
rates. Add a conversion fee, compare total spending with the budget, and
find the largest expense category.

### Algorithm

1.  Read the travel budget in INR.
2.  Read expenses for food, travel, and shopping.
3.  Convert each expense using its supplied exchange rate.
4.  Add a 2% conversion fee.
5.  Calculate total expenses.
6.  Find the largest expense category.
7.  Compare expenses with the budget.

### Flowchart

``` mermaid
flowchart TD
    A([Start]) --> B[Enter budget]
    B --> C[Enter expense amounts]
    C --> D[Convert using exchange rates]
    D --> E[Add 2 percent conversion fee]
    E --> F[Calculate total expenses]
    F --> G[Find largest category]
    G --> H{Total <= budget?}
    H -->|Yes| I[Within budget]
    H -->|No| J[Over budget]
    I --> K[Display result]
    J --> K
    K --> L([Stop])
```

### Source Code

``` python
budget = float(input("Budget in INR: "))
categories = ["Food", "Travel", "Shopping"]
rates = [83, 90, 1]
expenses = []

for i in range(3):
    amount = float(input(categories[i] + " expense: "))
    cost = amount * rates[i]
    cost = cost * 1.02
    expenses.append(cost)

total = sum(expenses)
largest = expenses.index(max(expenses))

print("Total Expense:", round(total, 2))
print("Largest Category:", categories[largest])

if total <= budget:
    print("Within Budget")
else:
    print("Over Budget")
```

### Sample Input

``` text
Budget in INR: 20000
Food expense: 20
Travel expense: 50
Shopping expense: 1000
```

### Sample Output

``` text
Total Expense: 7473.0
Largest Category: Shopping
Within Budget
```

------------------------------------------------------------------------

## 10. Campus Event Financial Planning

### Problem Statement

Calculate venue, equipment, catering, transport, and certificate costs.
Find the sponsorship shortfall and minimum number of registrations
needed to cover the remaining cost.

### Algorithm

1.  Read all event expenses.
2.  Read sponsorship and registration fee.
3.  Calculate total event cost.
4.  Calculate sponsorship shortfall.
5.  Calculate minimum registrations using rounding up.
6.  Display the results.

### Flowchart

``` mermaid
flowchart TD
    A([Start]) --> B[Enter event expenses]
    B --> C[Calculate total event cost]
    C --> D[Enter sponsorship and registration fee]
    D --> E[Calculate sponsorship shortfall]
    E --> F[Calculate minimum registrations]
    F --> G[Display results]
    G --> H([Stop])
```

### Source Code

``` python
import math

venue = float(input("Venue cost: "))
equipment = float(input("Equipment cost: "))
catering = float(input("Catering cost: "))
transport = float(input("Transport cost: "))
certificate = float(input("Certificate cost: "))

sponsor = float(input("Sponsorship amount: "))
fee = float(input("Registration fee per person: "))

total = venue + equipment + catering + transport + certificate
shortfall = max(0, total - sponsor)

if fee > 0:
    registrations = math.ceil(shortfall / fee)
    print("Minimum Registrations:", registrations)
else:
    print("Registration fee must be greater than zero")

print("Total Event Cost:", total)
print("Sponsorship Shortfall:", shortfall)
```

### Sample Input

``` text
Venue cost: 5000
Equipment cost: 2000
Catering cost: 8000
Transport cost: 3000
Certificate cost: 2000
Sponsorship amount: 10000
Registration fee per person: 200
```

### Sample Output

``` text
Minimum Registrations: 50
Total Event Cost: 20000.0
Sponsorship Shortfall: 10000.0
```

------------------------------------------------------------------------

**End of README**
