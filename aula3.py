"""TIPOS DE DADOS"""

# DocString
# Python = Linguagem de programação 
# Tipo de tipagem = Dinâmica / Forte
# str -> string -> texto
# Strings são textos que estão dentro de aspas
# O que significa tipagem dinâmina em Python?
# res: Que o tipo pode ser atribuido dinnamicamente pelo Python.

# Asps simples 
print('Lucas Daniel')

#Aspas duplas
print("Lucas Daniel")

# Escape
print("Lucas \"Danie\"")

#r
print(r"Lucas \"Danie\"")

# Tipos int e float
# int -> Número inteiro
# O tipo int representa qualquer número 
# positivo ou negativo. int sem sinal é positivo.

print(11) # int
print(-11) # int
print(0) # int

# float -> Número com ponto flutuante.
# O tipo float representa qualquer número
# positivo ou negativo com ponto flutuante 
# float sem sinal é considerado positivo

print(1.1, 10.11) # float
print(0.0, -1.5) # float

# A função type mostra o tipo que o Python 
# inferiu ao valor.
print(type('lucas'))
print(type(1))
print(type(-2))
print(type(1.1), type(0.0))

# Tipos de dados bool (boolean)
# Ao questionar algo em uim programa, 
# só existem duas resposta possiveis:
# sim (True) ou não (False)
# Existem vários operadores para "questionar".
# Dentre eles o ==, que é um operador lógico que 
# questiona se um valor é igual a outro.

print(10 == 10) # sim => True (Verdadeiro)
print(10 == 11) # não => (Falso)
print(type(10 == 11))

# Conversão de tipos, coerção
# type convertion, typecasting, coercion
# é o ato de converter um tipo em outro
# tipos imutáveis e primitivos:
# str, int, float, bool

print(1 + 1) # irá realizar a soma
print('a' + 'b') # irá concatenar ou seja juntar as duas string.
#print('a' + 1) Gera um erro por que ele só pode concatenar string(str) com string(str) e não com inteiro(int).
print(int('1'), type(int('1'))) # convertendo str em um int.
print(float('1') + 1)
print(type(float('1') + 1))
print(bool(''))
print(str(11) + 'b')
