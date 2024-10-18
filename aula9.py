# Usando a função inpuit para coletar dados do usuários.

# nome = input('Qual o seu Nome? ')
# print(f'O seu nome é {nome}')

# Esse modelo de converssão não e uma boa pratica
#numero_1 = int(input('Digite um número: '))
#numero_2 = int(input('Digite outro númeor: '))

numero_1 = input('Digite um número: ')
numero_2 = input('Digite outro númeor: ')

int_numero_1 = int(numero_1)
int_numero_2 = int(numero_2)

print(f'A soma dos números é: {int_numero_1 + int_numero_2}')