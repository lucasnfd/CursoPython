"""
Interpolação básica de strings

s - string
d e i -int
f - float
x e X - Hexadecimal (ABCDEF0123456789)

"""
nome = 'Lucas'
preco = 1000.05834834
variavel = '%s, o preço é R$%.5f' % (nome, preco)
print(variavel)
print('O Hexadecimal de %d é %08x' % (1500, 1500))