
n = int(input("Enter number of passengers: "))
for i in range(n):
    name = input("Enter passenger name: ")
    age = int(input("Enter age: "))
    distance = int(input("Enter distance in km: "))
    cls = input("Enter class (Sleeper/AC): ")
    if distance <= 100:
        fare = distance * 1
    else:
        fare = 100 + (distance - 100) * 2

    if cls == "AC":
        fare = fare + 200

    if age >= 60:
        fare = fare * 0.5

    fare = fare + 50
    cancel = input("Cancel ticket? (yes/no): ")
    if cancel == "yes":
        fare = fare * 0.5
    print("Passenger:", name)
    print("Final Fare:", fare)
