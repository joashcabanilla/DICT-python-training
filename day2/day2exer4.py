yearService = int(input("Enter years in service: "))
office = str(input("Enter office: "))

if office.upper() == "IT":
    if yearService >= 10:
        print("Amount given: 10,000")
    elif yearService < 10:
        print("Amount given: 5,000")
elif office.upper() == "ACCT":
    if yearService >= 10:
        print("Amount given: 12,000")
    elif yearService < 10:
        print("Amount given: 6,000")
elif office.upper() == "HR":
    if yearService >= 10:
        print("Amount given: 15,000")
    elif yearService < 10:
        print("Amount given: 7,500")
