from tkinter import *
from tkinter import messagebox
from Components.Button import *
from BackGroundPage import *
from Components.Table import SimpleTable
from DatabaseHelper import *
from Query.Admin import Query


class AdminHomePage:
    def __init__(self, root):
        self.root = root
        self.Manager_window = Toplevel()
        self.root.title("Sales")
        self.f = Frame(self.Manager_window, height=150, width=700, bg="white")
        self.f.pack()
        l4 = Label(self.f, text="Manager View Or Add Details", font=('Times New Roman', 30, 'bold'), background='white')
        l4.place(x=80, y=50)
        self.f1 = Frame(self.Manager_window, height=550, width=700, background='light blue')
        self.add_buttons()
        self.f1.pack()

    def add_data(self):

        name=self.productname_entry.get()
        price=self.productprice_entry.get()
        quantity=self.productquantity_entry.get()
        print(name)
        print(price)
        print(quantity)

        query=Query.ADD_DETAILS
        parameters= (name,price,quantity)

        DatabaseHelper.execute_query(query,parameters)

        messagebox.showinfo('Inserted Succesfully', "Done")
        #self.Manager_window.destroy()


    def add_labels(self):
        self.productname_label = Label(self.f1,font=("Times New Roman", 12),text="Product Name", width=20,background='light blue')
        self.productname_label.place(x=150, y=200)
        self.productname_entry=Entry(self.f1,font=('Times New Roman',12))#textvariable=product_name)
        self.productname_entry.place(x=300,y=200)

        self.productprice_label = Label(self.f1,font=("Times New Roman", 12), text="Product Price", width=20, background='light blue')
        self.productprice_label.place(x=150, y=250)
        self.productprice_entry = Entry(self.f1, font=('Times New Roman', 12))
        self.productprice_entry.place(x=300, y=250)

        self.productquantity_label = Label(self.f1,font=("Times New Roman", 12), text="Product Quantity", width=20,background='light blue')
        self.productquantity_label.place(x=150, y=350)
        self.productquantity_entry = Entry(self.f1, font=('Times New Roman', 12))
        self.productquantity_entry.place(x=300, y=350)

        self.submit_button = WhiteButton(self.f1, "Submit",self.add_data)
        self.submit_button.place(x=250, y=450)


    def add_extrabutton(self):


        self.addproducts_button=WhiteButton(self.f1, "Add Products", self.add_products)
        self.addproducts_button.place(x=170, y=80)


        # self.submit_button=WhiteButton(self.f, "Submit", self.add_products)
        # self.submit_button.place(x=250, y=500)



    def add_buttons(self):
        self.productdetails_button = WhiteButton(self.f1, "View Products", self.view_productdetails)
        self.productdetails_button.place(x=170, y=80)

        self.logout= WhiteButton(self.f1, "Logout", self.admin_logout, width=10)
        self.logout.place(x=400, y=80)

        #self.addproducts_button=WhiteButton(self.f, "Add Products", self.view_productdetails)
        #self.productdetails_button.place(x=150, y=150)


    def view_productdetails(self):

        query= Query.PRODUCT_DETAILS
        result = DatabaseHelper.get_all_data(query)
        self.products_table = SimpleTable(self.f1, rows=len(result), columns=len(result[0]), height=330, width=350)
        self.products_table.place(x=150, y=180)
        self.products_table.grid_propagate(0)
        self.productdetails_button.destroy()
        self.add_extrabutton()

        for r in range(len(result)):
            for c in range(len(result[0])):
                self.products_table.set(row=r, column=c, value=result[r][c])


    def add_products(self):
        self.products_table.destroy()
        self.add_labels()

    def admin_logout(self):
        import MainPage as main
        self.f.destroy()
        self.f1.destroy()
        main.MainPage(self.root)
        self.root.destroy()




if (__name__ == "__main__"):
    root = Tk()
    a = AdminHomePage(root)
    root.mainloop()