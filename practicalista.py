#listas

lista = [10, 8, 9,5]
print(lista)
lista.append(20)
lista.insert(1,10)
print (max(lista))
print (sum(lista))
print (min(lista))
print (len(lista))
lista.remove(9)
lista.sort()
print(lista)
print(lista[-1])
print(lista[1])
print(lista[0])
print(lista[2:])
print(lista[:2])
print(lista[-2])
print(lista[-1])

#tupla
meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
print(meses)
print(meses[0])

#meses[3] = 45

#diccionario de datos

estudiante = {
    
    "cedula": "0102030405",
    "nombre": "Gerardo Perez",
    "correo": "juan.perez@example.com",
    "celular": "0999999999",
    "notas": [10, 9, 5, 4]
}
print(estudiante.keys())
print(estudiante["nombre"])

conjuntoA = {1, 5, 4, 6, 8}
conjunoB = {1, 9, 6, 5, 4}
ConjuntoC = conjuntoA.intersection(conjunoB)
print(ConjuntoC)
