## for

for variavel in range(10):
    print(variavel)


for variavel in range(1, 11):
    print(variavel)

for variavel in range(1, 12, 3):
    print(variavel)


## exemplo 2

soma = 0

for i in range(3):
    nota = float(input(f'Informe a sua nota {i}: '))

    soma = soma + nota

print('A media das notas é: ', soma/3)