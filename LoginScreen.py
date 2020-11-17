import tkinter as tk
import tkinter.font as tkFont
from copy import copy

from InfoClass import InfoClass


class LoginScreen:
    appInfo = InfoClass()
    usernameEntry = 0
    def __init__(self, root, appInfo):
        self.appInfo = copy(appInfo);
        #setting title
        root.title("Login")
        #setting window size
        usernameLabel = tk.Label(root, text = "Username")
        usernameLabel.grid()
        self.usernameEntry = tk.Entry(root, text="Username")
        self.usernameEntry.grid()
        passwordLabel = tk.Label(root, text="Password")
        passwordLabel.grid()
        passwordEntry = tk.Entry(root, text="Password")
        passwordEntry.grid()
        passwordGenerationButton = tk.Button(root)
        passwordGenerationButton["bg"] = "#efefef"
        ft = tkFont.Font(family='Times', size=10)
        passwordGenerationButton["font"] = ft
        passwordGenerationButton["fg"] = "#000000"
        passwordGenerationButton["justify"] = "center"
        passwordGenerationButton["text"] = "login"
        passwordGenerationButton.grid()
        passwordGenerationButton["command"] = self.login

    def login(self):
        print("login!")
        self.appInfo.setUser(self.usernameEntry.get())





