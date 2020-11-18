import tkinter as tk
import tkinter.font as tkFont
from tkinter import ttk

class PasswordSelectionScreen:
    def __init__(self, root, appInfo, nextFrame):
        self.nextFrame = nextFrame
        self.appInfo = appInfo
        self.root = root
        print(self.appInfo.getPasswords())
        self.appInfo.setNumberOfInstances(self.appInfo.getNumberOfInstances() + 1)
        print(self.appInfo.getNumberOfInstances())
        self.WebsiteOptionList = list(appInfo.getPasswords().keys())
        self.WebsiteOptionList.insert(0, "")
        self.usernameOptionList = list()
        self.usernameOptionList.insert(0, "")
        websiteVar = tk.StringVar(root)
        websiteVar.set( self.WebsiteOptionList[0])
        userVar = tk.StringVar(root)
        userVar.set( self.WebsiteOptionList[0])
        webstiteLabel = tk.Label(root, text='Website: ')
        webstiteLabel.grid()
        self.websiteSelectionMenu = ttk.Combobox(root, values = self.WebsiteOptionList)
        self.websiteSelectionMenu.set("Pick an Option")
        self.websiteSelectionMenu.grid()
        userNameLabel = tk.Label(root, text='UserName: ')
        userNameLabel.grid()
        self.userNameDisplayLabel = tk.Label(root, text = "")
        self.userNameDisplayLabel.config(width=90, font=('Helvetica', 12))
        self.userNameDisplayLabel.grid()

        self.passwordDisplayLabel = tk.Label(root, text="", font=('Helvetica', 12))
        self. passwordDisplayLabel.grid()

        LoadDataButton = tk.Button(root)
        LoadDataButton["bg"] = "#efefef"
        ft = tkFont.Font(family='Times', size=10)
        LoadDataButton["font"] = ft
        LoadDataButton["fg"] = "#000000"
        LoadDataButton["justify"] = "center"
        LoadDataButton["text"] = "Load Data"
        LoadDataButton.grid()
        LoadDataButton["command"] = self.loadData

        getPasswordButton = tk.Button(root)
        getPasswordButton["bg"] = "#efefef"
        ft = tkFont.Font(family='Times', size=10)
        getPasswordButton["font"] = ft
        getPasswordButton["fg"] = "#000000"
        getPasswordButton["justify"] = "center"
        getPasswordButton["text"] = "getPassword"
        getPasswordButton.grid()
        getPasswordButton["command"] = self.getPassword

        generatePasswordButton = tk.Button(root)
        generatePasswordButton["bg"] = "#efefef"
        ft = tkFont.Font(family='Times', size=10)
        generatePasswordButton["font"] = ft
        generatePasswordButton["fg"] = "#000000"
        generatePasswordButton["justify"] = "center"
        generatePasswordButton["text"] = "Generate a new Password"
        generatePasswordButton.grid()
        generatePasswordButton["command"] = self.generatePassword

        copyPasswordButton = tk.Button(root)
        copyPasswordButton["bg"] = "#efefef"
        ft = tkFont.Font(family='Times', size=10)
        copyPasswordButton["font"] = ft
        copyPasswordButton["fg"] = "#000000"
        copyPasswordButton["justify"] = "center"
        copyPasswordButton["text"] = "Copy Password to Clipboard"
        copyPasswordButton.grid()
        copyPasswordButton["command"] = self.copyPasswordToClipboard
    def loadData(self):
        self.WebsiteOptionList = self.appInfo.getPasswords().keys()
        print(self.WebsiteOptionList)
        self.websiteSelectionMenu.configure(values  = list(self.WebsiteOptionList))
    def getPassword(self):
        self.userNameDisplayLabel.configure(text = "Username = " + self.appInfo.getPasswords()[self.websiteSelectionMenu.get()][0])
        self.passwordDisplayLabel.configure(text= "Password = " +  self.appInfo.getPasswords()[self.websiteSelectionMenu.get()][1])
    def copyPasswordToClipboard(self):
        self.userNameDisplayLabel.configure(text = "Username = " + self.appInfo.getPasswords()[self.websiteSelectionMenu.get()][0])
        self.root.clipboard_clear()
        self.root.clipboard_append(self.appInfo.getPasswords()[self.websiteSelectionMenu.get()][1])
        self.root.update()
    def generatePassword(self):
        self.nextFrame.tkraise()






