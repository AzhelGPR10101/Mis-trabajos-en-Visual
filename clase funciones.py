"""
#declaracion de funciones

def saludar ():
    print ("Hola Gerard ")

saludar()

#funcion con parametros

def calcular_la_edad (anio_actual, anio_nacimiento):
    print ("la edad actual es: ", anio_nacimiento - anio_actual)

a = int (input ("ingrese su año de nacimiento: "))
b = int (input("ingrese el año actual: "))

calcular_la_edad (a, b)

#funciones con retorno

def calcular_iva (precio, iva = 0.15):
    return precio*iva

resultado = calcular_iva (10)
print ("el valor del iva es: ", resultado)

resultado = calcular_iva (100,0.14)

# calcular lista

def calcular_par (numeros):
    for i in numeros:
        if numeros % 2 == 0:
            print (i, "Es par")
        else:
            print (i, "Es impar")

lista_numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
calcular_par ()

lista_numeros = range (0, 1000)
calcular_par (lista_numeros)

lista_numeros = range (0, 1000, 2)
calcular_par (lista_numeros)

lista_numeros = range (5, 0, -1)
calcular_par (lista_numeros)

#funciones con tuplas

def suma_de_numeros (*a):
    return sum (a)
print (suma_de_numeros (1,2,3))
"""
#funciones con diccionarios

def estudiantes (**lista_esudiantes):
    suma_total = 0
    for nombre, edad in lista_esudiantes.items():
        print ("El estudiante: ", nombre, "tiene: ", edad, " años")
        suma_total += edad
    print ("la suma de las edades de los estudiante es:", suma_total)

estudiantes(Santiago=20 , Gerard= 21, Mayte=20, Camilo=30, Pablo=34, David=20, Juan=21)

