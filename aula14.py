# Operadores lógicos 
# and (e) or (ou) not (não)
'''
and - Todas as condições precisam ser verdadeiras
Se qualquer valor for considerado falso,
a expressão inteira será avaliada naquele valor 
São considerados falsy 
Exwmplos: 0 0.0 '' False
Também existe o tipo none que é 
usado para representar um não valor
'''

# entrada = input('[E]ntrar [S]air: ')
# senha_digitada = input('Senha: ')


# senha_permitida = '123456'


# if entrada == 'E' and senha_digitada == senha_permitida:
#         print('Entrar')
# else:
#         print('Sair')


# # Avaliação de curti circuito
# if 1 and 1:
#     print(True and 1 and False)

# Operadores lógicos 
# and (e) or (ou) not (não)
'''
or - Qualquer condição verdadeira avalia toda
a expressão como verdadeira.
Se qualquer valor for considerado verdadeiro, 
a expressão inteira será avaliada naquele valor.
São considerados falsy 
Exemplos: 0 0.0 '' = false 
tembém existem o tipo none que é 
usado para representar um não valor 
'''
# entrada = input('[E]ntrar [S]air: ')
# senha_digitada = input('Senha: ')


# senha_permitida = '123456'


# if (entrada == 'E' or  entrada == 'e' ) and senha_digitada == senha_permitida:
#         print('Entrar')
# else:
#         print('Sair')

# Avaliação de curti circuito
senha = input('Senha: ')  or 'Sem senha'
print(senha)


