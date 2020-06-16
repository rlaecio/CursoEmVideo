nome = input('Qual o seu nome? ')
real = float(input('Digite os valores em Reais: '))
dollar = float(input('Cotação do dolar hoje: '))
conversao = real / dollar
print('Olá {}! \n Pela cotação de hoje, você pode comprar {:.2f} '
      'dolares com os seus {:.2f} reais' .format(nome, conversao, real))
