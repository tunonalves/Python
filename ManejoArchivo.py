from io import open 

arch_text = open("archivo.txt","w")

frase="Estupendo dia para estudiar Python \n el miercoles"

arch_text.write((frase))

arch_text.close()


arch_text2 = open("archivo.txt","r")

texto = arch_text2.read()

print(texto)

arch_text2.close()