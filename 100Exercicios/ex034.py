
salario = float(input('informe o salario do funcionário : R$ '))

if salario <= 1250:
    print('O valor do seu salario será R${:.2f}'.format(salario + salario * 0.15))
else:
    print('O valor do seu salário será R${:.2f}'.format(salario + salario * 0.10))
