from tkinter import *

raiz = Tk()
raiz.config(background="darkgray")
raiz.title("CALCULADORA")
raiz.resizable(0,0)
raiz.geometry("300x250")

miframe=Frame(raiz)
miframe.pack()

operacion=""
digitodisplay = StringVar()

digitodisplay.set("0")

def pulsaciones_numeros(numero):
	global operacion
	if operacion != "":
		digitodisplay.set(numero)
		operacion = ""
	else:
		if numero == "0" and digitodisplay.get()=="0":
			digitodisplay.set("0")
		elif numero == "." and digitodisplay.get()=="0":
			digitodisplay.set(digitodisplay.get()+numero)
		elif numero != "0" and digitodisplay.get()=="0":
			digitodisplay.set(numero)
		else:
			digitodisplay.set(digitodisplay.get()+numero)

def suma():
	global operacion
	operacion = "+"

def resta():
	global operacion
	operacion = "-"

def multiplicacion():
	global operacion
	operacion = "*"

def divicion():
	global operacion
	operacion = "/"

display=Entry(miframe, textvariable=digitodisplay,font="Arial 30")
display.grid(row=1,column=1,columnspan=4,padx=10,pady=10)
display.config(background="gray",fg="black",justify="right",width=10)

boton7=Button(miframe,text="7",width=5,pady=10,padx=1,command=lambda:pulsaciones_numeros("7"))
boton7.grid(row=2,column=1)
boton8=Button(miframe,text="8",width=5,pady=10,padx=1,command=lambda:pulsaciones_numeros("8"))
boton8.grid(row=2,column=2)
boton9=Button(miframe,text="9",width=5,pady=10,padx=1,command=lambda:pulsaciones_numeros("9"))
boton9.grid(row=2,column=3)
botondiv=Button(miframe,text="/",width=5,pady=10,padx=1,command=lambda:divicion("/"))
botondiv.grid(row=2,column=4)

boton4=Button(miframe,text="4",width=5,pady=10,padx=1,command=lambda:pulsaciones_numeros("4"))
boton4.grid(row=3,column=1)
boton5=Button(miframe,text="5",width=5,pady=10,padx=1,command=lambda:pulsaciones_numeros("5"))
boton5.grid(row=3,column=2)
boton6=Button(miframe,text="6",width=5,pady=10,padx=1,command=lambda:pulsaciones_numeros("6"))
boton6.grid(row=3,column=3)
botonmult=Button(miframe,text="*",width=5,pady=10,padx=1,command=lambda:multiplicacion("*"))
botonmult.grid(row=3,column=4)

boton1=Button(miframe,text="1",width=5,pady=10,padx=1,command=lambda:pulsaciones_numeros("1"))
boton1.grid(row=4,column=1)
boton2=Button(miframe,text="2",width=5,pady=10,padx=1,command=lambda:pulsaciones_numeros("2"))
boton2.grid(row=4,column=2)
boton3=Button(miframe,text="3",width=5,pady=10,padx=1,command=lambda:pulsaciones_numeros("3"))
boton3.grid(row=4,column=3)
botonsum=Button(miframe,text="+",width=5,pady=10,padx=1,command=lambda:suma("+"))
botonsum.grid(row=4,column=4)

boton0=Button(miframe,text="0",width=5,pady=10,padx=1,command=lambda:pulsaciones_numeros("0"))
boton0.grid(row=5,column=1)
botoncoma=Button(miframe,text=".",width=5,pady=10,padx=1,command=lambda:pulsaciones_numeros("."))
botoncoma.grid(row=5,column=2)
botonigual=Button(miframe,text="=",width=5,pady=10,padx=1)
botonigual.grid(row=5,column=3)
botonrestar=Button(miframe,text="-",width=5,pady=10,padx=1,command=lambda:resta("-"))
botonrestar.grid(row=5,column=4)

raiz.mainloop()