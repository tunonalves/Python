from tkinter import *

root = Tk()
miframe = Frame(root,width=500,height=450)
miframe.pack()

milable = Label(miframe,text="Bienvenidos")
milable.place(x=120,y=120)

Label(miframe, text="HOLA MUNDO").place(x=200,y=200)

root.mainloop()