## listas

notas = [7.9, 9.7, 8.2]

# criando lista

lista = []
lista = list()
lista = [26, 'exemplo', 3.14159, True]
lista_de_lista = [10, [1, 2, 3]]

# indexação e slices (fatiamento)

lista = [26, 'exemplo', 3.14159, True]

print(lista[0])
print(lista[-1])

# slices

lista = [10, 50, 30, 40, 25, 60, 5]

print(lista[0:3])
print(lista[2:])
print(lista[2:6:2])


# interações utilizando os próprios elementos da lista

for elemento in lista:
    print(elemento)

# utilizando os indices

for i in range(len(lista)):
    print(lista[i])