ag = float(input("Enter average grade: "))

if ag > 100:
    print("Grade out-of-range")
elif ag >= 95:
    print("Excellent")
elif ag >= 90:
    print("Outstanding")
elif ag >= 85:
    print("Very Good")
elif ag >= 80:
    print("Good")
elif ag >= 75:
    print("Poor")
elif ag >= 0:
    print("Failed")
elif ag < 0:
    print("Grade out-of-range")
