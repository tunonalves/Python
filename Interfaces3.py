from tkinter import *

raiz = Tk()
raiz.title("INDEX")
raiz.resizable(0,0)
raiz.geometry("500x500")
raiz.config(bg="darkgrey")

miframe=Frame(raiz)
miframe.pack()

milable1=Label(miframe,text="Nombre: ")
milable1.grid(row=1,column=0,sticky="w",padx=10,pady=10)
nombre_text=Entry(miframe)
nombre_text.grid(row=1,column=1)

milable2=Label(miframe,text="Apellido: ")
milable2.grid(row=2,column=0,sticky="w",padx=10,pady=10)
apellido_text=Entry(miframe)
apellido_text.grid(row=2,column=1)

milable3=Label(miframe,text="DNI: ")
milable3.grid(row=3,column=0,sticky="w",padx=10,pady=10)
dni_text=Entry(miframe)
dni_text.grid(row=3,column=1)

milable4=Label(miframe,text="Email: ")
milable4.grid(row=4,column=0,sticky="w",padx=10,pady=10)
email_text=Entry(miframe)
email_text.grid(row=4,column=1)

milable5=Label(miframe,text="Contraseña: ")
milable5.grid(row=5,column=0,sticky="w",padx=10,pady=10)
pass_text=Entry(miframe)
pass_text.config(show="*")
pass_text.grid(row=5,column=1)

raiz.mainloop()
