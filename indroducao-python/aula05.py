## estruturas condicionais

# exemplo 1

idade = 20

if idade >= 18:
    print('Maior de idade')
else:
    print('Menor de idade')


# exemplo 2

media = float(input('Informe a media do estudante: '))

if media >= 7:
    print('Aprovado')
elif media >= 5:
    print('Recuperação')
else:
    print('Reprovado')


# exemplo 3

media = 10
precensa = 100

if media >= 7 and precensa >= 70:
    print('aprovado')
else:
    print('reprovado')