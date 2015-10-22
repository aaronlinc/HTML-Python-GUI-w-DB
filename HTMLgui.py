from tkinter import *
from tkinter import ttk
import HTML_Drill as HTML
import bodyDB

class HTMLapp:

    def __init__(self, master):

        # Frame
        self.frame = ttk.Frame(master)
        self.frame.grid(row=0, column=0)
        self.frame.config(relief = RIDGE, padding = (30,15))
        
        
        # Labels
        self.label = ttk.Label(self.frame, text = "Insert Body of Site:")
        self.label.grid(row = 0, column = 0)
        self.label = ttk.Label(self.frame, text = "Choose Body:")
        self.label.grid(row = 1, column = 0)

        # Buttons
        self.submit = ttk.Button(self.frame, text = 'Submit',
                                 command = self.submitBody)
        self.submit.grid(row =0, column = 2)
        self.addDB =  ttk.Button(self.frame, text = "Add to DB",
                                 command = self.addToDB)
        self.addDB.grid(row= 0, column = 3)

        # Text Entry
        self.bodyEntry = ttk.Entry(self.frame, width = 60)
        self.bodyEntry.grid(row = 0, column = 1)

        # Combo Box with Body Choices
        self.body = StringVar()
        self.bodyChoices = ttk.Combobox(self.frame, textvariable = self.body)
        self.bodyChoices.grid(row = 1, column = 1, pady = 10)
        self.bodyChoices.config(values = (bodyDB.strList()), width = 58)
        self.bodyChoices.bind("<<ComboboxSelected>>", self.selectedBox)

    def selectedBox(self, event):
        print("test")
        self.bodyEntry.delete(0, END)
        self.bodyEntry.insert(0, self.bodyChoices.get())

    # Create HTML Body        
    def submitBody(self):
        bodyStr = self.bodyEntry.get()
        if bodyStr == '':
            print("No info")
        else:
            HTML.createHTML(bodyStr)
            print("Created")

    def addToDB(self):
        bodyStr = self.bodyEntry.get()
        if bodyStr == '':
            print("No infro")
        else:
            bodyDB.newRecordMan(bodyStr)
            self.bodyChoices.config(values = (bodyDB.strList()))
        

def main():
    root = Tk()
    root.option_add('*tearOff', False)
    app = HTMLapp(root)
    root.mainloop()

if __name__ == "__main__": main()
