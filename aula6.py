# Operadores aritméticos (matemática)

adicao = 10 + 10
print('adição', adicao)

subtracao = 10 - 5
print('Subtração', subtracao)

multiplicacao = 10 * 10 
print('Multiplicação', multiplicacao)

divisao = 10 / 2.2 # float
print('Divisão', divisao)

divisao_inteira = 10 // 2.2
print('Divisão inteira', divisao_inteira)

exponeciacao = 2 ** 10
print('Exponeciação', exponeciacao)

modulo = 55 % 2 # resto da divisão
print('Módulo', modulo)

# Ex de uso do modulo
print(10 % 8 == 0) 
print(16 % 8 == 0)
print(10 % 2 == 0)

#COncatenação:

concatenacao = 'A' + 'B' + 'C'
print(concatenacao)

a_dez_vezes = 'A'* 10
tres_vezes_luiz = 3 * 'Luiz'
print(a_dez_vezes)
print(tres_vezes_luiz)

# Precedendica entre os operadores aritiméticos,

# 1. (n + n) 
# 2. **
# 3. * / // %
# 4. + - 
conta_1 = 1 + 1 ** 5 + 5  
print(conta_1)