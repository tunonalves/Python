from io import open 

arch_text = open("archivo.txt","w")

frase="Estupendo dia para estudiar Python \n el miercoles"

arch_text.write((frase))

arch_text.close()


arch_text2 = open("archivo.txt","r")

texto = arch_text2.read()

print(texto)

arch_text2.close()


arch_text3 = open("archivo.txt","r")

lineas_text = arch_text3.readlines() #guarda en formato lista 

arch_text3.close()

print(lineas_text[0])


arch_text4 = open("archivo.txt","a")

arch_text4.write("\nHola Mundo")

arch_text4.close()