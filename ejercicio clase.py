def p1():
    print("datos = (10, 20, 30)")
    print("datos[1] = 99")
    print("print(datos)")
    print("\nResultado:")
    datos = (10, 20, 30)
    try:
        datos[1] = 99
        print(datos)
    except TypeError as e:
        print("TypeError:", e)


def p2():
    print("a = [1, 2, 3]")
    print("b = a")
    print("b[0] = 5")
    print("print(a)")
    print("\nResultado:")
    a = [1, 2, 3]
    b = a
    b[0] = 5
    print(a)


def p3():
    print('frase = "aprendo Python en TEC"')
    print("print(len(frase.split()))")
    print("\nResultado:")
    frase = "aprendo Python en TEC"
    print(len(frase.split()))


def p4():
    print("print(int(9.99))")
    print("\nResultado:")
    print(int(9.99))


def p5():
    print("print(type(10.0))")
    print("\nResultado:")
    print(type(10.0))


def p6():
    print("suma = 0")
    print("for n in range(1, 5):")
    print("    if n % 2 != 0:")
    print("        continue")
    print("    suma += n")
    print("print(suma)")
    print("\nResultado:")
    suma = 0
    for n in range(1, 5):
        if n % 2 != 0:
            continue
        suma += n
    print(suma)


def p7():
    print("print([n ** 2 for n in [1, 2, 3, 4] if n % 2 == 0])")
    print("\nResultado:")
    print([n ** 2 for n in [1, 2, 3, 4] if n % 2 == 0])


def p8():
    print("for i in range(1, 10, 3):")
    print('    print(i, end=" ")')
    print("\nResultado:")
    for i in range(1, 10, 3):
        print(i, end=" ")
    print()


def p9():
    print("for i in range(3, 0, -1):")
    print('    print(i, end=" ")')
    print("\nResultado:")
    for i in range(3, 0, -1):
        print(i, end=" ")
    print()


def p10():
    print("saldo = 350")
    print("if saldo >= 1000:")
    print('    print("Oro")')
    print("elif saldo >= 100:")
    print('    print("Plata")')
    print("else:")
    print('    print("Básica")')
    print("\nResultado:")
    saldo = 350
    if saldo >= 1000:
        print("Oro")
    elif saldo >= 100:
        print("Plata")
    else:
        print("Básica")


def p11():
    print("Pida números enteros con input() hasta que el usuario escriba fin.")
    print("Guárdelos en una lista y con comprensiones cree una lista de pares")
    print("y otra de impares. Muestre ambas ordenadas y la suma de cada una.")
    print("\nResultado:")
    numeros = []
    while True:
        t = input("Número entero (fin para terminar): ")
        if t.lower() == "fin":
            break
        try:
            numeros.append(int(t))
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
        v = input(mensaje).strip()
        if v in validas:
            return v
        print("Opción inválida.")


def mostrar(i):
    titulo, func = PREGUNTAS[i]
    print(f"\nPregunta {i + 1}: {titulo}\n")
    func()


def menu_preguntas():
    salir, volver = str(len(PREGUNTAS) + 1), str(len(PREGUNTAS) + 2)
    validas = [str(n) for n in range(1, len(PREGUNTAS) + 3)]
    while True:
        print("\nMenú de preguntas")
        for i, (titulo, _) in enumerate(PREGUNTAS, 1):
            print(f"{i}. {titulo}")
        print(f"{salir}. Salir\n{volver}. Regresar al menú principal")
        op = pedir("Opción: ", validas)
        if op == salir:
            return True
        if op == volver:
            return False
        mostrar(int(op) - 1)
        pedir("\n1. Regresar al menú\nOpción: ", ("1",))


print("¡Bienvenido al menú de ejercicios de Python!")
nombre = ""
while True:
    print("\nMenú principal\n1. Ingresar nombre\n2. Menú de preguntas\n3. Salir")
    op = pedir("Opción: ", ("1", "2", "3"))
    if op == "1":
        nombre = input("Nombre: ").strip()
        print(f"Hola, {nombre}.")
    elif op == "2":
        if menu_preguntas():
            break
    else:
        break
print(f"¡Hasta luego{', ' + nombre if nombre else ''}!")