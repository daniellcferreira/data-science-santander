## funções 

# inicial

def saudacao():
    print('Seja bem vindo(a)!')
    print('Ola é prazer em fazer parte desse curso!')

saudacao()

# com parâmetros

def saudacao(nome, curso):
    print(f'Seja bem vindo(a), {nome}!')
    print(f'Ola é prazer em fazer parte do curso de {curso}!')

saudacao('Daniel', 'Python')

# com parâmetros dafault

def saudacao(nome, curso='Python'):
    print(f'Seja bem vindo(a), {nome}!')
    print(f'Ola é prazer em fazer parte do curso de {curso}!')

saudacao('Daniel')

# com retorno

def soma(num1, num2):
    return num1 + num2

resultado = soma(5, 7)
print('O resultado da soma é', resultado)


# exemplo 2

def calculadora(num1, num2, operacao='+'):
    if operacao == '+':
        return num1 + num2
    elif operacao == '-':
        return num1 - num2
    
resultado = calculadora(10, 25, '-')
print(resultado)


