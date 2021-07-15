arch_text2 = open("archivo.txt","r")

arch_text2.seek(len(arch_text2.read())/2)

print(arch_text2.read())

arch_text2.close()

