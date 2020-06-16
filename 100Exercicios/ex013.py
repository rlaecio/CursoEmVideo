nome = input('Informe o seu nome: ')
salario = float(input('Informe salario atual: '))
aumento = float(input('Percentual de aumento: '))
valorAumento = salario * (aumento / 100)
salarioFinal = salario + valorAumento
print('{}, você tera um aumento de R$ {} no seu salario \n'
          'ficando assim com R$ {} no final do mês' .format(nome, valorAumento, salarioFinal))
