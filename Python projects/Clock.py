from tkiner import *
from tkinter.ttk import *
from time import strftime

root = TK()
root.title('Clock')

def time():
        string = strftime('%H:%M:%S:%P')
        lbl.config(text=string)
        lbl.after(1000, time)
        
lbl = Label(root, font=('calibri', 40, 'bold'),background='purple',foreground='white')
lbl.pack(anchor='centre')
time()

mainloop()                          
