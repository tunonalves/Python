misdatos=("Federico",15,12,1986)
nombre,dia,mes,agno = misdatos

misdatoslista=list(misdatos)
misdatostupla=tuple(misdatoslista)

print(misdatos)
print(misdatoslista)
print(misdatostupla)
print(15 in misdatostupla)
print(misdatos.count("Federico"))
print(len(misdatos))
print(nombre)
print(dia)
print(mes)
print(agno)
