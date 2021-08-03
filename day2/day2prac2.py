name = str(input("Enter Name: "))
math = int(input("Enter Math: "))
science = int(input("Enter Science: "))
english = int(input("Enter English: "))

aveGrade = (math + science + english) / 3
print(f"Average Grade: %.2f" % aveGrade)

if aveGrade >= 75:
    print("\nCongratulations!")
    print("You passed the semester")
    if math < 75:
        print("but you need to retake the following subject(s):\nMath")
        if science < 75:
            print("Science")
        if english < 75:
            print("English")
    elif science < 75:
        print("but you need to retake the following subject(s):\nScience")
        if math < 75:
            print("Math")
        if english < 75:
            print("English")
    elif english < 75:
        print("but you need to retake the following subject(s):\nEnglish")
        if math < 75:
            print("Math")
        if science < 75:
            print("Science")
else:
    print("You failed the semester")
