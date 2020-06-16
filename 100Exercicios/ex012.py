preco = float(input('Difite o preço: '))
desconto = float(input('Informe o desconto: '))
valorDesconto =  preco * (desconto /100)
valorFinal = preco - valorDesconto
print('Valor do desconto: R$ {:.2f}' .format(valorDesconto))
print('Valor do produto com o desconto de {:.2f} % é R$ {:.2f}' .format(desconto, valorFinal))
