def mostrar_codigo(codigo):
    print(codigo)
    print("\nResultado:")


def p1():
    mostrar_codigo("""datos = (10, 20, 30)
datos[1] = 99
print(datos)""")
    datos = (10, 20, 30)
    try:
        datos[1] = 99
        print(datos)
    except TypeError as e:
        print("TypeError:", e)


def p2():
    mostrar_codigo("""a = [1, 2, 3]
b = a
b[0] = 5
print(a)""")
    a = [1, 2, 3]
    b = a
    b[0] = 5
    print(a)


def p3():
    mostrar_codigo("""frase = "aprendo Python en TEC"
print(len(frase.split()))""")
    frase = "aprendo Python en TEC"
    print(len(frase.split()))


def p4():
    mostrar_codigo("print(int(9.99))")
    print(int(9.99))


def p5():
    mostrar_codigo("print(type(10.0))")
    print(type(10.0))


def p6():
    mostrar_codigo("""suma = 0
for n in range(1, 5):
    if n % 2 != 0:
        continue
    suma += n
print(suma)""")
    suma = 0
    for n in range(1, 5):
        if n % 2 != 0:
            continue
        suma += n
    print(suma)


def p7():
    mostrar_codigo("print([n ** 2 for n in [1, 2, 3, 4] if n % 2 == 0])")
    print([n ** 2 for n in [1, 2, 3, 4] if n % 2 == 0])


def p8():
    mostrar_codigo("""for i in range(1, 10, 3):
    print(i, end=" ")""")
    for i in range(1, 10, 3):
        print(i, end=" ")
    print()


def p9():
    mostrar_codigo("""for i in range(3, 0, -1):
    print(i, end=" ")""")
    for i in range(3, 0, -1):
        print(i, end=" ")
    print()


def p10():
    mostrar_codigo("""saldo = 350
if saldo >= 1000:
    print("Oro")
elif saldo >= 100:
    print("Plata")
else:
    print("Básica")""")
    saldo = 350
    if saldo >= 1000:
        print("Oro")
    elif saldo >= 100:
        print("Plata")
    else:
        print("Básica")


def p11():
    mostrar_codigo("""Pida números enteros con input() hasta que el usuario escriba fin.
Guárdelos en una lista y con comprensiones cree una lista de pares
y otra de impares. Muestre ambas ordenadas y la suma de cada una.""")
    numeros = []
    while True:
        texto = input("Número entero (fin para terminar): ")
        if texto.lower() == "fin":
            break
        try:
            numeros.append(int(texto))
        except ValueError:
            print("Entrada inválida.")
    pares = sorted([n for n in numeros if n % 2 == 0])
    impares = sorted([n for n in numeros if n % 2 != 0])
    print("Pares:", pares, "Suma:", sum(pares))
    print("Impares:", impares, "Suma:", sum(impares))


PREGUNTAS = [
    ("Tupla inmutable", p1),
    ("Copia de listas", p2),
    ("split() y len()", p3),
    ("int() con decimal", p4),
    ("Tipo de 10.0", p5),
    ("continue en for", p6),
    ("Comprensión de listas", p7),
    ("range con paso 3", p8),
    ("range descendente", p9),
    ("if / elif / else", p10),
    ("Ejercicio 9: pares e impares", p11),
]


def pedir(mensaje, validas):
    while True:
        opcion = input(mensaje).strip()
        if opcion in validas:
            return opcion
        print("Opción inválida.")
        
def menu_preguntas():
    total = len(PREGUNTAS)
    salir = str(total + 1)
    volver = str(total + 2)
    validas = [str(n) for n in range(1, total + 3)]

    while True:
        print("\nMenú de preguntas")
        for i in range(total):
            print(f"{i + 1}. {PREGUNTAS[i][0]}")
        print(f"{salir}. Salir")
        print(f"{volver}. Regresar al menú principal")

        opcion = pedir("Opción: ", validas)
        if opcion == salir:
            return True
        if opcion == volver:
            return False

        titulo, funcion = PREGUNTAS[int(opcion) - 1]
        print(f"\nPregunta {opcion}: {titulo}\n")
        funcion()
        pedir("\n1. Regresar al menú\nOpción: ", ["1"])


def main():
    print("¡Bienvenido al menú de ejercicios de Python!")
    nombre = ""

    while True:
        print("\nMenú principal")
        print("1. Ingresar nombre")
        print("2. Menú de preguntas")
        print("3. Salir")
        opcion = pedir("Opción: ", ["1", "2", "3"])

        if opcion == "1":
            nombre = input("Nombre: ").strip()
            print(f"Hola, {nombre}.")
        elif opcion == "2":
            if menu_preguntas():
                break
        else:
            break

    if nombre == "":
        print("¡Hasta luego!")
    else:
        print(f"¡Hasta luego, {nombre}!")


main()