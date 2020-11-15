import passwordGeneration
import PasswordStorageAndRetrevial
from PasswordGenerationScreen import PasswordGenerationScreen
import tkinter as tk
if __name__ == "__main__":
    root = tk.Tk()
    passwordDict = dict()
    app = PasswordGenerationScreen(root, passwordDict)
    root.mainloop()

