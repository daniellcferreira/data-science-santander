# dicionarios

# criando dicionarios

dicionario = {}
dicionario = dict()

dicionario = {'nome': 'Daniel',
              'idade': '36',
              'altura': 1.80}

print(dicionario)
print(dicionario['idade'])

# adicionando elementos no dicionario

dicionario['progrmador'] = True
print(dicionario)


# iterando sobre um dicionario

for variavel in dicionario:
    print(variavel, dicionario[variavel])