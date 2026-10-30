n = int(input("Enter number of students: "))
students = []

for i in range(n):
    name = input("Enter name: ")
    marks = int(input("Enter aggregate marks: "))
    subject = int(input("Enter subject marks: "))
    attendance = int(input("Enter attendance: "))
    income = int(input("Enter family income: "))

    if marks >= 75 and subject >= 40 and attendance >= 75 and income <= 200000:
        students.append((name, marks))

students.sort(key=lambda x: x[1], reverse=True)

print("\nEligible Students:")
for s in students:
    print(s[0], s[1])
