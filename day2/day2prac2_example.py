# ag = int(input("Enter average grade: "))
# if ag > 100:
#     print("Average Grade is out of range")
# elif ag >= 95 and ag <= 100:
#     print("Excellent")
# elif ag >= 90 and ag <= 94:
#     print("Outstanding")
# elif ag >= 85 and ag <= 89:
#     print("Very Good")
# elif ag >= 80 and ag <= 84:
#     print("Good")
# elif ag >= 75 and ag <= 79:
#     print("Poor")
# elif ag >= 0 and ag <= 74:
#     print("Failed")
# elif ag < 0:
#     print("Average Grade is out of range")

name = str(input("Enter name: "))
math = int(input("Enter Math Grade: "))
sci = int(input("Enter Science Grade: "))
eng = int(input("Enter English Grade: "))
ag = (math+sci+eng) / 3
print(f"Average Grade: {round(ag,2)}")
if ag >= 75:
    print("Congratulations!\nYou Passed the semester")
    if math < 75 or sci < 75 or eng < 75:
        print("but you need to retake the following subject(s):")
        if math < 75:
            print("-Math")
        if sci < 75:
            print("-Science")
        if eng < 75:
            print("-English")
else:
    print("You failed the semester")
