
venue = int(input("Enter venue cost: "))
equipment = int(input("Enter equipment cost: "))
catering = int(input("Enter catering cost: "))
transport = int(input("Enter transport cost: "))
certificate = int(input("Enter certificate cost: "))
sponsor = int(input("Enter sponsorship amount: "))
fee = int(input("Enter registration fee: "))
total = venue + equipment + catering + transport + certificate
shortfall = max(0, total - sponsor)
participants = shortfall / fee
print("Total Event Cost:", total)
print("Sponsorship Shortfall:", shortfall)
print("Participant Contribution:", fee)
print("Minimum Registrations:", int(participants) + (participants % 1 > 0))
