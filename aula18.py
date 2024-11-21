"""
Formatação básica de strings

s - string
d - int
f - float
.<número de digitos>f
x ou X - Hexadecimal 
(Caractere)(><^)(quantidade)
> - Esquerda
< - Direita
^ - Centro
Sinal - + ou -
Ex.: 0>-100, 1f
Conversion flags - !r !s !a
"""

variavel = 'ABC'
print(f'{variavel}')
print(f'{variavel: >10}')
print(f'{variavel: <10}')
print(f'{variavel:%^10}')
print(f'{1000.0139441393403:0>+10.3f}')
