nome = str(input('Digite seu nome completo : '))

print('----- A N A L I S A N D O   S E U   N O M E ---------')
print('Seu nome em maiusculas é {}'.format(nome.upper()))
print('Seu nome em minusculas é {}'.format(nome.lower()))
print('O seu nome possui {} letras'.format(len(nome.strip()) - nome.count(' ')))
print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))


