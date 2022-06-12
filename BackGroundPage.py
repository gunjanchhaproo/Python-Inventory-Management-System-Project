from tkinter import *

class BackGroundPage:
    def __init__(self,root):
        #self.root=Toplevel()
        self.root=root
        self.root.state('normal')
        #self.root.geometry('800x800')
        self.f=Frame(self.root,width=700,height=150,background='white')
        self.f1 = Frame(self.root, width=700, height=550,background='light blue')
        self.root.title('Inventory Management System')
        self.f.pack()
        self.f1.pack()
        l2 = Label(self.f,  text="Inventory Management System", font=('Times New Roman', 25, 'bold'),background='white')
        l2.place(x=135, y=50)
        self.f.pack_propagate(0)


if __name__=="__main__":
    root=Tk()
    bg=BackGroundPage(root)
    root.mainloop()