print('\033[0:30:41m Teste! \033[m')

print('\033[0:30:41m Teste! \033[m')

print('\033[4:33:44m Teste! \033[m')

print('\033[1:33:43m Teste! \033[m')

print('\033[30:42m Teste! \033[m')

print('\033[m Teste! \033[m')

print('\033[7:30m Teste! \033[m')

nome = 'Guanabara'
# exemplo 1
print('Olá! Muito prazer em te conhecer, {}{}{}'.format('\033[4;34m', nome, '\033[m'))

#exemplo 02
cores = {'limpa':'\033[m',
         'azul':'\033[4;34m',
         'amarelo':'\033[33m',
         'pretoebranco':'\033[7;30m'
         }

print('Olá! Muito prazer em te conhecer, {}{}{}'.format(cores['azul'], nome, cores['limpa']))
print('Olá! Muito prazer em te conhecer, {}{}{}'.format(cores['amarelo'], nome, cores['limpa']))
print('Olá! Muito prazer em te conhecer, {}{}{}'.format(cores['pretoebranco'], nome, cores['limpa']))
