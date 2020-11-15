import tkinter as tk
import tkinter.font as tkFont

from passwordGeneration import generatePassword


class PasswordGenerationScreen:
    URLTextBox = 0
    passwordDict = dict()
    usernameTextBox = 0
    passwordDisplayMessage = 0
    def __init__(self, root, passwordDict):
        self.passwordDict = passwordDict
        #setting title
        root.title("Password Generation")
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
        passwordGenerationButton.place(x=60,y=150,width=140,height=25)
        passwordGenerationButton["command"] = self.passwordGenerationButton

        self.URLTextBox=tk.Entry(root)
        self.URLTextBox["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        self.URLTextBox["font"] = ft
        self.URLTextBox["fg"] = "#333333"
        self.URLTextBox["justify"] = "center"
        self.URLTextBox["text"] = "URL"
        self.URLTextBox.place(x=130,y=40,width=140,height=25)

        self.usernameTextBox=tk.Entry(root)
        self.usernameTextBox["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        self.usernameTextBox["font"] = ft
        self.usernameTextBox["fg"] = "#333333"
        self.usernameTextBox["justify"] = "center"
        self.usernameTextBox["text"] = "Username"
        self.usernameTextBox.place(x=130,y=80,width=140,height=25)

        self.passwordDisplayMessage=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        self.passwordDisplayMessage["font"] = ft
        self.passwordDisplayMessage["fg"] = "#333333"
        self.passwordDisplayMessage["justify"] = "left"
        self.passwordDisplayMessage["text"] = " "
        self.passwordDisplayMessage.place(x=220,y=300)

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
        passwordLabel.place(x=200,y=300,width=101,height=30)

        minLowerCaseLabel=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        minLowerCaseLabel["font"] = ft
        minLowerCaseLabel["fg"] = "#333333"
        minLowerCaseLabel["justify"] = "center"
        minLowerCaseLabel["text"] = "Minimum Lower Case Letters"
        minLowerCaseLabel.place(x=300,y=30)

        minUpperCaseLetterLabel=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        minUpperCaseLetterLabel["font"] = ft
        minUpperCaseLetterLabel["fg"] = "#333333"
        minUpperCaseLetterLabel["justify"] = "center"
        minUpperCaseLetterLabel["text"] = "Minimum Upper Case letters"
        minUpperCaseLetterLabel.place(x=300,y=70)

        minNumberLabel=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        minNumberLabel["font"] = ft
        minNumberLabel["fg"] = "#333333"
        minNumberLabel["justify"] = "center"
        minNumberLabel["text"] = "Minimum Numbers"
        minNumberLabel.place(x=300,y=110)

        minSpeciaLCharLabel=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        minSpeciaLCharLabel["font"] = ft
        minSpeciaLCharLabel["fg"] = "#333333"
        minSpeciaLCharLabel["justify"] = "right"
        minSpeciaLCharLabel["text"] = "Minimum Special Characters"
        minSpeciaLCharLabel.place(x=300,y=150)

        minLowerCaseEntry=tk.Entry(root)
        minLowerCaseEntry["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        minLowerCaseEntry["font"] = ft
        minLowerCaseEntry["fg"] = "#333333"
        minLowerCaseEntry["justify"] = "center"
        minLowerCaseEntry["text"] = "minLow"
        minLowerCaseEntry.place(x=480,y=30,width=70,height=25)

        minUpperCaseEntry=tk.Entry(root)
        minUpperCaseEntry["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        minUpperCaseEntry["font"] = ft
        minUpperCaseEntry["fg"] = "#333333"
        minUpperCaseEntry["justify"] = "center"
        minUpperCaseEntry["text"] = "minUp"
        minUpperCaseEntry.place(x=480,y=70,width=70,height=25)

        minNumberEntry=tk.Entry(root)
        minNumberEntry["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        minNumberEntry["font"] = ft
        minNumberEntry["fg"] = "#333333"
        minNumberEntry["justify"] = "center"
        minNumberEntry["text"] = "minNum"
        minNumberEntry.place(x=480,y=110,width=70,height=25)

        minSpecialEntry=tk.Entry(root)
        minSpecialEntry["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        minSpecialEntry["font"] = ft
        minSpecialEntry["fg"] = "#333333"
        minSpecialEntry["justify"] = "right"
        minSpecialEntry["text"] = "minSpec"
        minSpecialEntry.place(x=480,y=150,width=70,height=25)

        disallowedCharactersLabel=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        disallowedCharactersLabel["font"] = ft
        disallowedCharactersLabel["fg"] = "#333333"
        disallowedCharactersLabel["justify"] = "right"
        disallowedCharactersLabel["text"] = "Illegal Characters"
        disallowedCharactersLabel.place(x=300,y=190)

        disallowedCharactersEntry=tk.Entry(root)
        disallowedCharactersEntry["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        disallowedCharactersEntry["font"] = ft
        disallowedCharactersEntry["fg"] = "#333333"
        disallowedCharactersEntry["justify"] = "center"
        disallowedCharactersEntry["text"] = "noChars"
        disallowedCharactersEntry.place(x=480,y=190,width=70,height=25)

    def passwordGenerationButton(self):
        userPass = generatePassword()
        self.passwordDict[self.URLTextBox.get()] = [self.usernameTextBox.get(), userPass]
        self.passwordDisplayMessage['text'] = userPass


