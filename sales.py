from tkinter import *
from tkinter import ttk
from DatabaseHelper import *

class Sales():
     def __init__(self,root,result):
         self.root=root
         self.name1=[]
         self.qtyy=[]
         self.total=0
         self.price=[]
         self.latest=[]
         self.sales_Window=Toplevel()
         self.root.title("Sales")
         self.f=Frame(self.sales_Window,height=150,width=700,bg="white")
         self.f.pack()
         l4 = Label(self.f, text="Sales", font=('Times New Roman', 30, 'bold'), background='white')
         l4.place(x=300, y=50)
         self.f1 = Frame(self.sales_Window, height=550, width=700, background='light blue')
         self.f1.pack()
         customer_name=Label(self.f1,text="Customer Name :",fg="black",bg="light blue",font=("Times New Roman",12))
         customer_name.place(x=30,y=80)
         self.customer_name_entry=Entry(self.f1, width=30, fg='black', bg='white')
         self.customer_name_entry.place(x=150,y=80)
         self.customer_name_entry.focus_set()

         customer_contact=Label(self.f1,text="Contact_no :",fg="black",bg="light blue",font=("Times New Roman",12))
         customer_contact.place(x=400,y=80)
         self.customer_contact_entry = Entry(self.f1, width=30, fg='black', bg='white')
         self.customer_contact_entry.place(x=500, y=80)

         product_select=Label(self.f1,text="Product Selection :",bg="light blue",font=("Times New Roman",20,"bold"))
         product_select.place(x=250,y=180)

         product_name=Label(self.f1,text="Product Name:",bg="light blue",font=("Times New Roman",12))
         product_name.place(x=200,y=250)
         res=self.validate()
         name_var= StringVar()
         self.name_combobox = ttk.Combobox(self.f1, textvariable=name_var)
         self.name_combobox['values']=res
         self.name_combobox.place(x=350,y=250)

         product_quantity = Label(self.f1, text="Product Quantity:", bg="light blue", font=("Times New Roman", 12))
         product_quantity.place(x=200, y=325)
         res1=self.validate2()
         quantity_var = StringVar()
         self.quantity_combobox = ttk.Combobox(self.f1, textvariable=quantity_var)
         self.quantity_combobox['values']=res1
         self.quantity_combobox.place(x=350, y=325)

         add_button=Button(self.f1,text="Add to cart",font=("Times New Roman", 12),command=self.addtocart)
         add_button.place(x=225,y=400)

         generatebill_button = Button(self.f1, text="Generate Bill", font=("Times New Roman", 12),command=self.generatebill)
         generatebill_button.place(x=375, y=400)


     def validate(self):
         query="select ProductName from inventory.ProductMenu"
         result=DatabaseHelper.get_data_combo(query)
         return result

     def validate2(self):
         query1="select ProductQuantity from inventory.ProductMenu"
         result = DatabaseHelper.get_data_combo(query1)
         return result

     def addtocart(self):
         name=self.name_combobox.get()
         qty=self.quantity_combobox.get()
         self.name1.append(name)
         self.qtyy.append(qty)
         print(self.name1)
         print(self.qtyy)

     def generatebill(self):
         for i in self.name1:
             query2 = "select ProductPricePerKG from inventory.ProductMenu where ProductName=%s"
             parameters = i
             res = DatabaseHelper.get_data(query2, parameters)
             x=res[0]
             print(x)
             self.price.append(x)
         # for j in self.price:
         #     self.latest.append(j.values())
        # print(self.latest)
         j=0
         for i in self.qtyy:
             #indexi = self.qtyy.index(i)
             x=self.price[j]
             qty=int(i)
             self.total =self.total+(x*qty)
             print(self.total)
             j+=1
         print(self.price)
         self.sales_Window.destroy()
         import GenerateBillPage as gp
         gp.GenerateBill(self.root,self.total,self.name1,self.qtyy,self.price)






if(__name__=="__main__"):
    root=Tk()
    m=Sales(root,)
    root.mainloop()









