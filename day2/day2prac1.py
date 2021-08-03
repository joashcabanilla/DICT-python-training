name = str(input("Enter Name: "))
math = float(input("Enter Math: "))
science = float(input("Enter Science: "))
english = float(input("Enter English: "))

aveGrade = (math + science + english) / 3

print(f"Average Grade: %.2f" % aveGrade)

if aveGrade >= 75:
    print("\nCongratulations!")
    print(f"You passed the semester.")
else:
    print("\nYou failed the semester")
