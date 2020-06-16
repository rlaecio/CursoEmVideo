diasAlugados = int(input('Informe o numero de dias alugados: '))
kmRodados = float(input('Informe os Km rodados: '))
valorAPagar = (diasAlugados * 60) + (kmRodados * 0.15)
print('O valor a pagar é R${:.2f}'.format(valorAPagar))
