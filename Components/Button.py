from tkinter import *

class GrayButton(Button):
    def __init__(self,parent,text,command,**kwargs):
        super().__init__(parent,text=text,width=30,height=4,activebackground='gray',activeforeground='white',command=command)
        self.configure(**kwargs)

class WhiteButton(Button):
    def __init__(self,parent,text,command,**kwargs):
        super().__init__(parent,text=text,width=30,height=4,activebackground='white',activeforeground='gray',command=command)
        self.configure(**kwargs)


if __name__=='__main__':
    root=Tk()
    g=GrayButton(root,"GrayButton",command="")
    g.pack(padx=10, pady=10)

    w = WhiteButton(root, "White button", command="")
    w.pack(padx=10, pady=10)

    root.mainloop()