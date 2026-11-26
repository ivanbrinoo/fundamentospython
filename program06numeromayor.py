print("Programa Numero mayor")
print("Introduce el primer numero:")
numero1 = int(input())
print("Introduce el segundo numero:")
numero2 = int(input())
if (numero1 > numero2):
    print(f"{numero1} es mayor")
elif (numero1 < numero2):
    print(f"{numero2} es menor")
else:
    print(f"Los numeros son iguales")