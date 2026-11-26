print("¿Positivo o negativo?")
print("Introduce el numero:")
num = int(input())
if (num > 0):
    print(f"{num} es positivo")
elif (num < 0):
    print(f"{num} es negativo")
else:
    print(f"El numero es cero")