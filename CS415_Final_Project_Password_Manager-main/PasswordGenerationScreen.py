import tkinter as tk
import tkinter.font as tkFont

class PasswordGenerationScreen:
    def __init__(self, root):
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

        GButton_522=tk.Button(root)
        GButton_522["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_522["font"] = ft
        GButton_522["fg"] = "#000000"
        GButton_522["justify"] = "center"
        GButton_522["text"] = "Generate Password"
        GButton_522.place(x=60,y=150,width=70,height=25)
        GButton_522["command"] = self.GButton_522_command

        GLineEdit_565=tk.Entry(root)
        GLineEdit_565["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_565["font"] = ft
        GLineEdit_565["fg"] = "#333333"
        GLineEdit_565["justify"] = "center"
        GLineEdit_565["text"] = "Entry"
        GLineEdit_565.place(x=130,y=40,width=70,height=25)

        GLineEdit_499=tk.Entry(root)
        GLineEdit_499["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_499["font"] = ft
        GLineEdit_499["fg"] = "#333333"
        GLineEdit_499["justify"] = "center"
        GLineEdit_499["text"] = "Entry"
        GLineEdit_499.place(x=130,y=80,width=70,height=25)

        GMessage_71=tk.Message(root)
        ft = tkFont.Font(family='Times',size=10)
        GMessage_71["font"] = ft
        GMessage_71["fg"] = "#333333"
        GMessage_71["justify"] = "center"
        GMessage_71["text"] = " "
        GMessage_71.place(x=120,y=110,width=80,height=25)

        GLabel_201=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_201["font"] = ft
        GLabel_201["fg"] = "#333333"
        GLabel_201["justify"] = "center"
        GLabel_201["text"] = "Website URL"
        GLabel_201.place(x=0,y=40,width=97,height=30)

        GLabel_449=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_449["font"] = ft
        GLabel_449["fg"] = "#333333"
        GLabel_449["justify"] = "center"
        GLabel_449["text"] = "Username"
        GLabel_449.place(x=10,y=80,width=70,height=25)

        GLabel_249=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_249["font"] = ft
        GLabel_249["fg"] = "#333333"
        GLabel_249["justify"] = "center"
        GLabel_249["text"] = "Your Password:"
        GLabel_249.place(x=0,y=110,width=101,height=30)

    def GButton_522_command(self):
        print("command")
