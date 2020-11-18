import passwordGeneration
import PasswordStorageAndRetrevial
from InfoClass import InfoClass
from LoginScreen import LoginScreen
from PasswordGenerationScreen import PasswordGenerationScreen
import tkinter as tk

from PasswordSelectionScreen import PasswordSelectionScreen

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("700x700")
    userInfo = InfoClass()
    root.title = "Password Manager"
    f1 = tk.Frame(root)
    f2 = tk.Frame(root)
    f3 = tk.Frame(root)

    for frame in (f1, f2, f3):
        frame.place(width = 700, height = 700)
    LoginScreen(f1, userInfo, f2)
    PasswordSelectionScreen(f2, userInfo, f3)
    PasswordGenerationScreen(f3, userInfo, f2)
    f1.tkraise()
    root.mainloop()

