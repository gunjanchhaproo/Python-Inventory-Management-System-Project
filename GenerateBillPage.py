from tkinter import *
from tkinter import ttk
from DatabaseHelper import *
from Components.Table import *

class GenerateBill:
    def __init__(self,root,total,productName,productQty,pricPerkg):
        self.root=root
        self.total=total
        self.productName=productName
        self.producQtyy=productQty
        self.pricePerKg=pricPerkg
        self.generate=Toplevel()
        self.root.title("Generate Bill")
        self.f = Frame(self.generate, height=150, width=700, background='white')
        l4 = Label(self.f, text="Purchase Bill", font=('Times New Roman', 30, 'bold'), background='white')
        l4.place(x=225, y=50)
        self.f1 = Frame(self.generate, height=550, width=700, background='light blue')
        self.f.pack()
        self.f1.pack()
        l1 = Label(self.f1, width=20, text="Your Bill "+str(total), font=('Times New Roman', 20,'bold'), background='light blue')
        l1.place(x=200,y=50)
        self.products_table = SimpleTable(self.f1, rows=len(self.productName), columns=3, height=330, width=350)
        self.products_table.place(x=150, y=180)
        self.products_table.grid_propagate(0)
        # for r in range(len(self.productName)):
        #     for c in range(3):
        #         if(c==0):
        #          self.products_table.set(row=r, column=c, value=self.productName[r])
        #         elif(c==1):
        #             self.products_table.set(row=r, column=c, value=self.productName[r])

        for r in range(len(self.productName)):
             self.products_table.set(row=r, column=0, value=self.productName[r])
        for r in range(len(self.productName)):
             self.products_table.set(row=r, column=1, value=self.producQtyy[r])
        for r in range(len(self.productName)):
             self.products_table.set(row=r, column=2, value=self.pricePerKg[r])


if __name__ == '__main__':
    root = Tk()
    g = GenerateBill(root)

    root.mainloop()