from tkinter import *
from tkinter import ttk
import sqlite3

class App(Tk):
    def __init__(self):
        super().__init__()
        self.title("Sqlite3 with tkinter real-time searching.")
        self.defaultString = StringVar(value="Enter the data.") # first text show in input
    
        self.conn = sqlite3.connect("Person.db") # make connection to database
        self.c = self.conn.cursor() # ready to execute code
        
        self.create_widgets() # create widgets
        self.ent.bind("<KeyRelease>", self.search) # whenever key the keyboard
        
        
    def create_widgets(self):
        frameLeft = ttk.Frame(self)
        frameRight = ttk.Frame(self)
        
        # frame left
        ttk.Label(frameLeft, text="Enter the date: ", font=("Calibri", 25)).pack(anchor="w")
        self.ent = ttk.Entry(frameLeft, textvariable=self.defaultString, font=("Calibri", 25))
        self.ent.pack(pady=10)
        
        # frame right
        self.textArea = Text(frameRight, width=50, height=10, font=("Calibri", 18), state="disabled")
        self.textArea.pack()
        
        frameLeft.grid(row=0, column=0)
        frameRight.grid(row=0, column=1)
        
    def search(self, event):
        get = self.ent.get() # take value from input
        self.textArea.configure(state='normal')
        self.textArea.delete("1.0", "end") # clear text area
        
        self.c.execute("SELECT * FROM persons") 
        dbList = self.c.fetchall() # take all select to the variable (list of tuple)
        
        for data in dbList: # a data in list
            data = [str(item) for item in data] # take all data to string
            for col in data: # data in column
                if get in col: # if input in some data
                    self.textArea.insert("end", f"{' , '.join(data)}\n") # insert data to text area
                    break # aware same word
        
        self.textArea.configure(state='disabled')
        self.conn.commit() # commit sql code
        
if __name__ == "__main__":
    app = App()
    app.mainloop()
    app.conn.close() # disconnect to database