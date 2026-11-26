print("Ejemplo salario por hora")
print("Escriba el numero de horas trabajadas: ")
numhoras = int(input())
print("Escriba el precio por hora: ")
preciohora = int(input())
salario = numhoras * preciohora
if(numhoras <= 0):
    print("No hay datos del ultimo mes trabajado")
elif(numhoras <= 36):
    salario = numhoras * preciohora
    print(f"Salario total: {salario} €")
else:
    horasextra = numhoras - 36
    salario = (36 * preciohora) + (horasextra * (preciohora + 2))
    print(f"Salario total: {salario} €")
print("Fin del programa")