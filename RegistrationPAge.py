from tkinter import *
from tkinter import messagebox
from DatabaseHelper import *

class Registration:
    def __init__(self,root):
        self.root=root
        self.registration_window=Toplevel()
        self.root.title("Registration Form")
        self.f=Frame(self.registration_window,width=700,height=150,background='White')
        l5 = Label(self.f, text="Registration Form", font=('Times New Roman', 30, 'bold'), background='white')
        l5.place(x=200, y=50)
        self.f1 = Frame(self.registration_window, width=700, height=550,background='light blue')
        l1 = Label(self.f1, width=20, text="Enter Name: ",font=('Times New Roman', 12),background='light blue')
        l2 = Label(self.f1, width=20, text="Enter Username: ",font=('Times New Roman', 12),background='light blue')
        l3 = Label(self.f1, width=20, text="Enter EmailID: ",font=('Times New Roman', 12),background='light blue')
        l4 = Label(self.f1, width=20, text="Enter Password: ",font=('Times New Roman', 12),background='light blue')
        self.e_name = Entry(self.f1, width=30, fg='black', bg='white')
        self.e_name.focus_set()
        self.e_username = Entry(self.f1, width=30, fg='black', bg='white')
        self.e_email=Entry(self.f1,width=30,fg='black',bg='white')
        self.e_password = Entry(self.f1, width=30, fg='black', bg='white', show='*')
        l1.place(x=200, y=150)
        l2.place(x=200, y=200)
        l3.place(x=200, y=250)
        l4.place(x=200, y=300)

        self.e_name.place(x=350,y=150)
        self.e_username.place(x=350,y=200)
        self.e_email.place(x=350, y=250)
        self.e_password.place(x=350, y=300)
        b1 = Button(self.f1, text="Submit", height=2, width=10,command=self.validate)
        b1.place(x=325,y=360)
        self.f.pack()
        self.f1.pack()

    def validate(self):
        username=self.e_username.get()
        password=self.e_password.get()
        query=""
        if (username == "" or password == ""):
            messagebox.showwarning("Mandatory fields", "Please fill all the fields")
            self.registration_window.tkraise()
        else:
            query = "Insert into Customer_Login(username, password) Values (%s,%s)"
            parameters=(username,password)
            DatabaseHelper.execute_query(query,parameters)
            messagebox.showinfo("Success", "User registered successfully. Please login")
            self.registration_window.destroy()

if __name__ == '__main__':
    root = Tk()
    g = Registration(root)

    root.mainloop()
