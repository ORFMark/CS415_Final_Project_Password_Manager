from tkinter import *
from tkinter import ttk
root = Tk()
root.title("Password Generator");
root.geometry("388x240")

Label(root, text="").grid(row=10, columnspan=2)
Label(root, text="Your Password:").grid(row=11, columnspan=2)
T = Text(root, height=1, width=48).grid(row=12, columnspan=2)

def callback():
    print("Generated!")

    T.delete("1.0", END)
    T.insert(END, LCLVal.get(), END, UCLVal.get(),
             END, NumVal.get(), END, SpCharVal.get())

# Website Entry box
Label(root, text="Website URL").grid(row=2, column=0, sticky=W)
webEntry = Entry(root, width=45).grid(row=2, column=1)

# Spinbox for Lower Case Letters
Label(root, text="Lower Case Count").grid(row=3, column=0, sticky=W)
LCLVal = Spinbox(root, from_=0.0, to=50.0).grid(row=3, column=1, sticky=E)

# Spinbox for Upper Case Letters
Label(root, text="Upper Case Count").grid(row=4, column=0, sticky=W)
UCLVal = Spinbox(root, from_=0.0, to=50.0).grid(row=4, column=1, sticky=E)

# Spinbox for Numbers
Label(root, text="Number Count").grid(row=5, column=0, sticky=W)
NumVal = Spinbox(root, from_=0.0, to=50.0).grid(row=5, column=1, sticky=E)

# Spinbox for Special Characters
Label(root, text="Sp. Character Count").grid(row=6, column=0, sticky=W)
SpCharVal = Spinbox(root, from_=0.0, to=50.0).grid(row=6, column=1, sticky=E)

# Excluded characters Entry box
Label(root, text="Excluded Characters").grid(row=7, column=0, sticky=W)
excludeEntry = Entry(root, width=45).grid(row=7, column=1)

#Generate password button
Label(root, text="").grid(row=8)
b = Button(root, text="Generate", command=callback, width=48, bg='dark gray').grid(row=9, columnspan=2)

root.mainloop()
