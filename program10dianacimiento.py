print("Inicio programa dia de nacimiento")
print("Escribe el dia de nacimiento")
dianacimiento = int(input())
print("Escribe el mes de nacimiento")
mesnacimiento = int(input())
print("Escribe el año de nacimiento")
anyonacimiento = int(input())
if (mesnacimiento == 1 or mesnacimiento == 2):
    mesnacimiento = mesnacimiento + 12
    anyonacimiento = anyonacimiento - 1
ope1 = ((mesnacimiento + 1) * 3) // 5
ope2 = anyonacimiento // 4
ope3 = anyonacimiento // 100
ope4 = anyonacimiento // 400
ope5 = dianacimiento + (mesnacimiento * 2) + anyonacimiento + ope1 + ope2 - ope3 + ope4 + 2
ope6 = ope5 // 7
ope7 = ope5 - (ope6 * 7)

if ope7 == 0:
    print("Has nacido un Sábado")
elif ope7 == 1:
    print("Has nacido un Domingo")
elif ope7 == 2:
    print("Has nacido un Lunes")
elif ope7 == 3:
    print("Has nacido un Martes")
elif ope7 == 4:
    print("Has nacido un Miércoles")
elif ope7 == 5:
    print("Has nacido un Jueves")
else:
    print("Has nacido un Viernes")