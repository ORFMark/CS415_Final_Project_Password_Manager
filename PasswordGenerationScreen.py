import tkinter as tk
import tkinter.font as tkFont

from PasswordStorageAndRetrevial import writePasswordSet
from passwordGeneration import generatePassword


class PasswordGenerationScreen:
    def __init__(self, root, appInfo, nextFrame):
        self.appInfo = appInfo
        self.appInfo.setNumberOfInstances(self.appInfo.getNumberOfInstances() + 1)
        print(self.appInfo.getNumberOfInstances())
        self.nextFrame = nextFrame
        #setting title
        #setting window size

        passwordGenerationButton = tk.Button(root)
        passwordGenerationButton["bg"] = "#efefef"
        ft = tkFont.Font(family='Times', size=10)
        passwordGenerationButton["font"] = ft
        passwordGenerationButton["fg"] = "#000000"
        passwordGenerationButton["justify"] = "center"
        passwordGenerationButton["text"] = "Generate Password"
        passwordGenerationButton.place(x=60, y=150, width=140, height=25)
        passwordGenerationButton["command"] = self.passwordGenerationButton

        self.URLTextBox = tk.Entry(root)
        self.URLTextBox["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=10)
        self.URLTextBox["font"] = ft
        self.URLTextBox["fg"] = "#333333"
        self.URLTextBox["justify"] = "center"
        self.URLTextBox["text"] = "URL"
        self.URLTextBox.place(x=130, y=40, width=140, height=25)

        self.usernameTextBox = tk.Entry(root)
        self.usernameTextBox["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=10)
        self.usernameTextBox["font"] = ft
        self.usernameTextBox["fg"] = "#333333"
        self.usernameTextBox["justify"] = "center"
        self.usernameTextBox["text"] = "Username"
        self.usernameTextBox.place(x=130, y=80, width=140, height=25)

        self.passwordDisplayMessage = tk.Label(root)
        ft = tkFont.Font(family='Times', size=10)
        self.passwordDisplayMessage["font"] = ft
        self.passwordDisplayMessage["fg"] = "#333333"
        self.passwordDisplayMessage["justify"] = "left"
        self.passwordDisplayMessage["text"] = " "
        self.passwordDisplayMessage.place(x=300,y=300)

        URLTextLabel = tk.Label(root)
        ft = tkFont.Font(family='Times', size=10)
        URLTextLabel["font"] = ft
        URLTextLabel["fg"] = "#333333"
        URLTextLabel["justify"] = "center"
        URLTextLabel["text"] = "Website URL"
        URLTextLabel.place(x=0, y=40, width=97, height=30)

        usernameLabel = tk.Label(root)
        ft = tkFont.Font(family='Times', size=10)
        usernameLabel["font"] = ft
        usernameLabel["fg"] = "#333333"
        usernameLabel["justify"] = "center"
        usernameLabel["text"] = "Username"
        usernameLabel.place(x=10, y=80, width=70, height=25)

        passwordLabel = tk.Label(root)
        ft = tkFont.Font(family='Times', size=10)
        passwordLabel["font"] = ft
        passwordLabel["fg"] = "#333333"
        passwordLabel["justify"] = "center"
        passwordLabel["text"] = "Your Password:"
        passwordLabel.place(x=200, y=300, width=101, height=30)

        minLowerCaseLabel = tk.Label(root)
        ft = tkFont.Font(family='Times', size=10)
        minLowerCaseLabel["font"] = ft
        minLowerCaseLabel["fg"] = "#333333"
        minLowerCaseLabel["justify"] = "center"
        minLowerCaseLabel["text"] = "Minimum Lower Case Letters"
        minLowerCaseLabel.place(x=300, y=30)

        minUpperCaseLetterLabel = tk.Label(root)
        ft = tkFont.Font(family='Times', size=10)
        minUpperCaseLetterLabel["font"] = ft
        minUpperCaseLetterLabel["fg"] = "#333333"
        minUpperCaseLetterLabel["justify"] = "center"
        minUpperCaseLetterLabel["text"] = "Minimum Upper Case letters"
        minUpperCaseLetterLabel.place(x=300, y=70)

        minNumberLabel = tk.Label(root)
        ft = tkFont.Font(family='Times', size=10)
        minNumberLabel["font"] = ft
        minNumberLabel["fg"] = "#333333"
        minNumberLabel["justify"] = "center"
        minNumberLabel["text"] = "Minimum Numbers"
        minNumberLabel.place(x=300, y=110)

        minSpeciaLCharLabel = tk.Label(root)
        ft = tkFont.Font(family='Times', size=10)
        minSpeciaLCharLabel["font"] = ft
        minSpeciaLCharLabel["fg"] = "#333333"
        minSpeciaLCharLabel["justify"] = "right"
        minSpeciaLCharLabel["text"] = "Minimum Special Characters"
        minSpeciaLCharLabel.place(x=300, y=150)

        self.minLowerCaseEntry = tk.Spinbox(root,from_=0.0, to=50.0)
        self.minLowerCaseEntry["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=10)
        self.minLowerCaseEntry["font"] = ft
        self.minLowerCaseEntry["fg"] = "#333333"
        self.minLowerCaseEntry["justify"] = "center"
        self.minLowerCaseEntry["text"] = "minLow"
        self.minLowerCaseEntry.place(x=480, y=30, width=70, height=25)

        self.minUpperCaseEntry = tk.Spinbox(root, from_=0.0, to=50.0)
        self.minUpperCaseEntry["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=10)
        self.minUpperCaseEntry["font"] = ft
        self.minUpperCaseEntry["fg"] = "#333333"
        self.minUpperCaseEntry["justify"] = "center"
        self.minUpperCaseEntry["text"] = "minUp"
        self.minUpperCaseEntry.place(x=480, y=70, width=70, height=25)

        self.minNumberEntry = tk.Spinbox(root, from_=0.0, to=50.0)
        self.minNumberEntry["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=10)
        self.minNumberEntry["font"] = ft
        self.minNumberEntry["fg"] = "#333333"
        self.minNumberEntry["justify"] = "center"
        self.minNumberEntry["text"] = "minNum"
        self.minNumberEntry.place(x=480, y=110, width=70, height=25)

        self.minSpecialEntry = tk.Spinbox(root, from_=0.0, to=50.0)
        self.minSpecialEntry["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=10)
        self.minSpecialEntry["font"] = ft
        self.minSpecialEntry["fg"] = "#333333"
        self.minSpecialEntry["justify"] = "right"
        self.minSpecialEntry["text"] = "minSpec"
        self.minSpecialEntry.place(x=480, y=150, width=70, height=25)

        disallowedCharactersLabel = tk.Label(root, )
        ft = tkFont.Font(family='Times', size=10)
        disallowedCharactersLabel["font"] = ft
        disallowedCharactersLabel["fg"] = "#333333"
        disallowedCharactersLabel["justify"] = "right"
        disallowedCharactersLabel["text"] = "Illegal Characters"
        disallowedCharactersLabel.place(x=300, y=190)

        disallowedCharactersEntry = tk.Entry(root)
        disallowedCharactersEntry["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=10)
        disallowedCharactersEntry["font"] = ft
        disallowedCharactersEntry["fg"] = "#333333"
        disallowedCharactersEntry["justify"] = "center"
        disallowedCharactersEntry["text"] = "noChars"
        disallowedCharactersEntry.place(x=480, y=190, width=70, height=25)
        goBack = tk.Button(root, text = "go back", command = self.goBackButton)
        goBack.place(x=60, y=175, width=140, height=25)
    def passwordGenerationButton(self):
        userPass = generatePassword(minLowercase=int(self.minLowerCaseEntry.get()), minNum=int(self.minNumberEntry.get()),
                                    minUpperCase=int(self.minUpperCaseEntry.get()), minSpecial=int(self.minSpecialEntry.get())
                                    )
        self.appInfo.getPasswords()[self.URLTextBox.get()] = [self.usernameTextBox.get(), userPass]
        self.passwordDisplayMessage['text'] = userPass

    def goBackButton(self):
        writePasswordSet(self.appInfo.getUser(), self.appInfo.getPasswords())
        self.nextFrame.tkraise()



