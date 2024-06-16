## metodos de listas

lista = [1, 3, 12, 8, 2]

# append
lista.append(3)
print(lista)

# insert
lista.insert(2, 10)
print(lista)

# extend
lista2 = [1, 2, 3]
lista.extend(lista2)

# pop
lista.pop()
print(lista)

lista.pop(1)

# remove
lista.remove(3)
print(lista)

# count
print(lista.count(2))

# index
print(lista.index(5))

# sort
lista.sort()
print(lista)


# funções para lista

# len
print(len(lista))

# sum
print(sum(lista))

# max
print(max(lista))
