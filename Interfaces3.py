from tkinter import *
from tkinter import messagebox as MessageBox

raiz = Tk()
raiz.title("INDEX")
raiz.resizable(0,0)
raiz.geometry("800x600")
raiz.config(bg="gray")

miframe=Frame(raiz, bg="darkgrey")
miframe.pack()

minombre=StringVar()

milable1=Label(miframe,text="Nombre: ")
milable1.grid(row=1,column=0,sticky="w",padx=10,pady=10)
nombre_text=Entry(miframe,textvariable=minombre)
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

milable6=Label(miframe,text="Texto: ")
milable6.grid(row=6,column=0,sticky="w",padx=10,pady=10)
text_text=Text(miframe,width="25",height="15")
text_text.grid(row=6,column=1)

miscrollvertical=Scrollbar(miframe,command=text_text.yview)
miscrollvertical.grid(row="6",column="2",sticky="nsew")
text_text.config(yscrollcommand=miscrollvertical.set)

def funcionboton():
	
	MessageBox.showinfo("Informacion",nombre_text.get()+" "+apellido_text.get())

boton_enviar=Button(raiz,text="Submit",command=funcionboton)
boton_enviar.pack()

raiz.mainloop()