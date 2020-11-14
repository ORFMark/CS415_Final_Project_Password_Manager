import tkinter as tk
import tkinter.font as tkFont

from passwordGeneration import generatePassword


class PasswordGenerationScreen:
    def __init__(self, root, passwordDict):
        #setting title
        root.title("undefined")
        #setting window size
        width=600
        height=500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        passwordGenerationButton=tk.Button(root)
        passwordGenerationButton["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        passwordGenerationButton["font"] = ft
        passwordGenerationButton["fg"] = "#000000"
        passwordGenerationButton["justify"] = "center"
        passwordGenerationButton["text"] = "Generate Password"
        passwordGenerationButton.place(x=60,y=150,width=70,height=25)
        passwordGenerationButton["command"] = self.passwordGenerationButton

        URLTextBox=tk.Entry(root)
        URLTextBox["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        URLTextBox["font"] = ft
        URLTextBox["fg"] = "#333333"
        URLTextBox["justify"] = "center"
        URLTextBox["text"] = "Entry"
        URLTextBox.place(x=130,y=40,width=70,height=25)

        usernameTextBox=tk.Entry(root)
        usernameTextBox["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        usernameTextBox["font"] = ft
        usernameTextBox["fg"] = "#333333"
        usernameTextBox["justify"] = "center"
        usernameTextBox["text"] = "Entry"
        usernameTextBox.place(x=130,y=80,width=70,height=25)

        passwordDisplayMessage=tk.Message(root)
        ft = tkFont.Font(family='Times',size=10)
        passwordDisplayMessage["font"] = ft
        passwordDisplayMessage["fg"] = "#333333"
        passwordDisplayMessage["justify"] = "center"
        passwordDisplayMessage["text"] = " "
        passwordDisplayMessage.place(x=120,y=110,width=80,height=25)

        URLTextLabel=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        URLTextLabel["font"] = ft
        URLTextLabel["fg"] = "#333333"
        URLTextLabel["justify"] = "center"
        URLTextLabel["text"] = "Website URL"
        URLTextLabel.place(x=0,y=40,width=97,height=30)

        usernameLabel=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        usernameLabel["font"] = ft
        usernameLabel["fg"] = "#333333"
        usernameLabel["justify"] = "center"
        usernameLabel["text"] = "Username"
        usernameLabel.place(x=10,y=80,width=70,height=25)

        passwordLabel=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        passwordLabel["font"] = ft
        passwordLabel["fg"] = "#333333"
        passwordLabel["justify"] = "center"
        passwordLabel["text"] = "Your Password:"
        passwordLabel.place(x=0,y=110,width=101,height=30)

    def passwordGenerationButton(self):
        userPass = generatePassword()
        passWordDict[URLTextBox]

