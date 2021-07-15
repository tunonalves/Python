arch_text2 = open("archivo.txt","r")

print(arch_text2.read())

arch_text2.seek(10)

print(arch_text2.read())

arch_text2.close()

