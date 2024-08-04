N = 100
Suma = 0
C = 0

print("")
T = int(input("Cuantas temperaturas desea ingresar: "))
print("")

Temp = [0] * T

for i in range(T):
    cantidad = i + 1
    Temp[i] = float(input("Ingrese el valor de las temperaturas: "))
    Suma = Suma + Temp[i]

print("")
print(Temp)

Media = Suma/N

for i in range(T):
    if Temp[i] >= Media:
     C = C + 1

print("")
print("La media es de: ")
print(Media)
print("")
print("Total de temperatura >= Media es de: ")
print(C)
print("")