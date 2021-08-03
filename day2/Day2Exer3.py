# age = int(input("Enter your age: "))
#
# if age >= 1:
#     if age > 112:
#         print("Age is out-of-range")
#     elif age >= 60: #age range 60-112
#         print("Senior Citizen")
#     else:
#         print("Not a Senior Citizen")
# else:
#     print("Age is out-of-range")

# number = int(input("Enter a number: "))
#
# if number > 0:
#     print("Positive")
#     if number % 2 == 0:
#         print("Even")
#     else:
#         print("Odd")
# else:
#     print("Negative")

number = int(input("Enter a number: "))
if number > 0:
    print("Positive")
if number % 2 == 0:
    print("Even")
if number < 0:
    print("Negative")
if number % 2 != 0:
    print("Odd")
