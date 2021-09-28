from tkinter import *

raiz = Tk()

raiz.title("INDEX")
raiz.resizable(1,1)
raiz.geometry("800x600")
raiz.config(bg="darkgrey")

miframe = Frame()

miframe.pack()
miframe.config(bg="gray")
miframe.config(width="500",height="300")
miframe.pack(side="top",anchor="n",fill="x")

raiz.mainloop()

