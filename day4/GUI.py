from tkinter import *

# def compute():
    # hf = float()

window = Tk()
window.geometry("600x600")
window.resizable(0, 0)
window.title("BMI Calculator")

# result = stringVar()
titleL = Label(window, text="Body Mass Index Calculator")
titleL.place(x=180, y=10)

hfL = Label(window, text="Height in feet:", font="Tahoma")
hfL.place(x=150, y=100)

hfE = Entry(window, bd=3)
hfE.place(x=260, y=100)

hiL = Label(window, text="Height in inches:", font="Tahoma")
hiL.place(x=130, y=150)

hiE = Entry(window, bd=3)
hiE.place(x=260, y=150)

wkgL = Label(window, text="Weight in kilogram:", font="Tahoma")
wkgL.place(x=110, y=200)

wkgE = Entry(window, bd=3)
wkgE.place(x=260, y=200)

calc = Button(window, text="Calculate", width=8)
calc.place(x=250, y=250)

clear = Button(window, text="Clear", width=8)
clear.place(x=330, y=250)

bmiE = Entry(window, bd=3)
bmiE.place(x=260, y=300)

window.mainloop()

