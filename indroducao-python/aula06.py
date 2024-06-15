## while

numero_sorteado = 15
numero_escolhido = int(input('Informe um numero entre 1 e 20: '))

while numero_escolhido != numero_sorteado:
    print('Você errou o numero, tente novamente...')

    numero_escolhido = int(input('Informe um numero entre 1 e 20: '))

print('você acertou!')


## exemplo 2

contador = 0

while contador < 5:
    print(contador)

    contador = contador + 1