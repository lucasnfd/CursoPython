# Operadores in e not in
# String são iteráveis 
# 0 1 2 3 4 5 
# L u c a s 
# -6-5-4-3-2-1

nome = 'Lucas'
print(nome[2])

print('a' in nome)
print('zero' in nome)
print('vio' not in nome)


nome = input('Digite seu nome: ')
encontrar = input('Digite o que deseja encontrar: ')

if encontrar in nome:
    print(f'{encontrar} está em {nome}')
else:
    print(f'{encontrar} não está e {nome}')

#Pergunta 1:
#Qual o resultado do código abaixo?

variavel_a = 1 or 0
variavel_b = 0 or 1
print(variavel_a, variavel_a)

#Pergunta 2:
#Qual o resultado do código abaixo?

nome = 'Maria Carmo'
 
if ' ' in nome:
    print(f'O nome {nome} tem espaços.')
else:
    print(f'O nome {nome} NÃO tem espaços.')

#Pergunta 3:
#É possível adicionar um if dentro de outro fazendo várias condições aninhadas. Com isso em mente, o que você acha que o código abaixo exibe na tela?

numero = 10
 
if numero > 1:
    if numero > 2:
        if numero > 3:
            print('Número maior que 3')
        else:
            print('Número menor que 3')
    else:
        print('Número menor que 2')
else:
    print('Número menor que 1')