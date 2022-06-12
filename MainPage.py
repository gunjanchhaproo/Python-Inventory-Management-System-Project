from BackGroundPage import *
from tkinter import messagebox
from Components.Button import *
from LoginWindowPAge import *
from DatabaseHelper import *
from RegistrationPAge import *

class MainPage(BackGroundPage):
    def __init__(self,root):
        super().__init__(root)
        self.root.title("Inventory Management System")
        self.root.geometry('700x700')
        self.add_widgets()

    def add_widgets(self):
        self.manager_button=GrayButton(self.f1,"Manager Login",font=('Times New Roman',12),command= lambda: Login("Manager", self.f1,self.root))
        self.manager_button.place(x=60,y=175)

        self.consumer_button = GrayButton(self.f1, "Consumer Login",font=('Times New Roman',12),command=lambda: Login("Consumer", self.f1,self.root))
        self.consumer_button.place(x=360, y=175)

        self.manager_button = GrayButton(self.f1, "New User Sign Up?",font=('Times New Roman',12),command= lambda: Registration(self.root))
        self.manager_button.place(x=210, y=280)


if(__name__=="__main__"):
    root=Tk()
    m=MainPage(root)
    root.mainloop()
