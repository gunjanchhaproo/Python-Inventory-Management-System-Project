from tkinter import *
from tkinter import messagebox
from DatabaseHelper import *

class Login:
    def __init__(self, login_type, main_page,root):
        self.root=root
        self.login_type = login_type
        self.main_page = main_page
        self.login_window = Toplevel()
        self.root.title(login_type)
        self.f = Frame(self.login_window, height=150, width=700,background='white')
        l4 = Label(self.f, text="Login", font=('Times New Roman', 30, 'bold'), background='white')
        l4.place(x=300, y=50)
        self.f1 = Frame(self.login_window, height=550, width=700,background='light blue')
        l1 = Label(self.f1, width=20, text="Enter Username: ",font=('Times New Roman',12),background='light blue')
        l2 = Label(self.f1, width=20, text="Enter Password: ",font=('Times New Roman',12),background='light blue')
        self.e_username = Entry(self.f1, width=30, fg='black', bg='white')
        self.e_password = Entry(self.f1, width=30, fg='black', bg='white', show='*')
        self.e_username.focus_set()
        l1.place(x=150,y=150)
        l2.place(x=150,y=200)
        self.e_username.place(x=350,y=150)
        self.e_password.place(x=350,y=200)
        b1 = Button(self.f1, text="Submit", height=2, width=10,command=self.validate)
        b1.place(x=300,y=300)
        self.f.pack()
        self.f1.pack()

    def validate(self):
        username = self.e_username.get()
        pwd = self.e_password.get()
        query=""
        if (self.login_type == "Manager"):
            query = "Select * from inventory.Admin_Login where username= %s and password=%s"
        else:
            query = "Select * from inventory.Customer_Login where username= %s and password=%s"
        parameters = (username, pwd)
        result=DatabaseHelper.get_data(query, parameters)
        print(username)
        print(pwd)
        print(query)
        if (result is None):
            messagebox.showerror("Login Failed", "Incorrect credentials")
            self.login_window.tkraise()
            # self.reset()
            self.e_username.focus()
        else:
            messagebox.showinfo('Login Success', "Login successfuly completed")

            self.login_window.destroy()
            if(self.login_type=='Consumer'):
                import sales as s
                s.Sales(self.root,result)
            else:
                import MangerHomePage as mp
                mp.AdminHomePage(self.root)



if __name__ == '__main__':
    root = Tk()
    g = Login(root, "Manager",root)

    root.mainloop()