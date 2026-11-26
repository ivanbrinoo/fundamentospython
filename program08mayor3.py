print("Programa mayor de 3 numeros")
print("Escriba el primer numero")
num1 = int(input())
print("Escriba el segundo numero")
num2 = int(input())
print("Escriba el tercer numero")
num3 = int(input())
suma = num1 + num2 + num3
media = suma / 3
mayor = 0
if (num1 > num2) and (num1 > num3):
    print("El numero mayor es: ", num1)
elif (num2 > num1) and (num2 > num3):
    print("El numero mayor es: ", num2)
else:
    print("El numero mayor es: ", num3)
print(f"Suma: {suma}")
print(f"Media: {media}")
print("Fin del programa")

