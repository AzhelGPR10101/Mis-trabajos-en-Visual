for i in range(5):
    print(i)
print("++++++++++++++++++")
for i in range(10):
    print(i)
print("++++++++++++++++++")
for i in range(2, 10):
    print(i)
print("++++++++++++++++++")

for i in range(2, 10, 3):
    print(i)

print("++++++++++++++++++")
for i in range(10, 0, -1):
    print(i)

for i in range(0, 101):
    if i % 2 == 0:
        print("El número es par: ", i)
    else:
        print("El número es impar: ", i)

notas = [6,8,9,10,3]
for elemento in notas:
    print("El elemento es: ", elemento)