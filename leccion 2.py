# Primera pregunta - ¿Qué ocurre al ejecutar el siguiente código?
datos = (10, 20, 30)
datos[1] = 99
print(datos)

# Segunda pregunta - ¿Qué imprime el siguiente código?
a = [1, 2, 3]
b = a
b[0] = 5
print(a)

# tercera pregunta - ¿Qué imprime el siguiente código?
frase = "aprendo Python en TEC"
print(len(frase.split()))

#cuarta pregunta - ¿Qué imprime el siguiente código?
print(int(9.99))

#quinta pregunta - ¿Qué imprime el siguiente código?
print(type(10.0))

#Sexta pregunta - ¿Qué imprime el siguiente código?
suma = 0
for n in range(1, 5):
    if n % 2 != 0:
        continue
    suma += n
print(suma)

#septima pregunta - ¿Qué imprime el siguiente código?
print([n ** 2 for n in [1, 2, 3, 4] if n % 2 == 0])

#octava pregunta - ¿Qué imprime el siguiente código?
for i in range(1, 10, 3):
    print(i, end=" ")

#novena pregunta - ¿Qué imprime el siguiente código?
for i in range(3, 0, -1):
    print(i, end=" ")

#decima pregunta - ¿Qué imprime el siguiente código?
saldo = 350
if saldo >= 1000:
    print("Oro")
elif saldo >= 100:
    print("Plata")
else:
    print("Básica")


#onceava - ¿Qué imprime el siguiente código?

numeros = []
while True:
    dato = input("Ingrese un número entero (fin para terminar): ")
    if dato == "fin":
        break
    numeros.append(int(dato))

pares = sorted([n for n in numeros if n % 2 == 0])
impares = sorted([n for n in numeros if n % 2 != 0])

print(f"Pares: {pares}")
print(f"Suma de pares: {sum(pares)}")
print(f"Impares: {impares}")
print(f"Suma de impares: {sum(impares)}")