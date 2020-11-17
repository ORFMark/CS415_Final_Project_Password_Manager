import passwordGeneration
import PasswordStorageAndRetrevial
from InfoClass import InfoClass
from LoginScreen import LoginScreen
from PasswordGenerationScreen import PasswordGenerationScreen
import tkinter as tk
if __name__ == "__main__":
    root = tk.Tk()
    passwordDict = dict()
    userInfo = InfoClass()
    app = LoginScreen(root, userInfo)
    i = 0
    root.mainloop()


