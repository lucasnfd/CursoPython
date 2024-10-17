# # Introdução a f-strings (formatação de strings)
nome = 'Lucas Daniel' #str
altura = 1.80 #float
peso = 95
imc = peso / altura ** 2 # IMC = peso /(altura *altura)

linha_1 = f'{nome} tem {altura:.2f} de altura' # f-strings (formatação de strings)
linha_2 = f'pesa {peso} quilos em seu IMC é'
linha_3 = f'{imc:.2f}'

print(linha_1)
print(linha_2)
print(linha_3)

# print(nome, 'tem', altura, 'altura')
# print('pesa', peso, 'quilos em seu IMC é',)
# print(imc)