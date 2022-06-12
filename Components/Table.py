from tkinter import *
from Components.scrollableframe import *

class SimpleTable(VerticalScrolledFrame):
    def __init__(self, parent, rows=15, columns=4,**kwargs):
        super().__init__(parent, background="#f2efe6",**kwargs)
        self.header_color="#DEA057"
        self.even_color="#c2bfb8"
        self.odd_color="#ebe6d8"
        self._widgets = []
        for row in range(rows):
            current_row = []
            if(row==0):
              bg=self.header_color
              label = Label(self, text="-",borderwidth=0, height=3,bg=bg,wraplength=400,fg='black')
            elif(row%2==0):
                bg=self.even_color
            else:
                bg=self.odd_color
            for column in range(columns):
                if (row == 0):
                    label = Label(self, text="-", borderwidth=0, height=3, bg=bg, wraplength=400, fg='white')
                    label.grid(row=row, column=column, sticky="nsew", padx=1, pady=1)
                    current_row.append(label)
                else:
                    label = Label(self, text="-",borderwidth=0, height=3,bg=bg,wraplength=400)
                    label.grid(row=row, column=column, sticky="nsew", padx=1, pady=1)
                    current_row.append(label)
            self._widgets.append(current_row)

    def set(self, row, column, value,widget=None,**kwargs):
        widget_ref = self._widgets[row][column]

        if(widget is not None):
            if(row%2==0):
                widget.configure(bg=self.even_color)
            else:
                widget.configure(bg=self.odd_color)
            widget.grid(row=row, column=column, sticky="nsew", padx=1, pady=1)
            self._widgets[row][column]=widget
            widget_ref.configure(text=str(value), **kwargs)
            widget_ref=widget
        widget_ref.configure(text=str(value),**kwargs)

if __name__ == "__main__":
    root = Tk()
    t = SimpleTable(root, rows=10, columns=4,width=200)
    t.pack(side=TOP, fill=X)
    t.set(0, 0, "Hello, world avc c sd ")
    root.mainloop()