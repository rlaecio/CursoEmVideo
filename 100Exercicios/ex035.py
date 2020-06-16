reta01 = float(input('Informe o valor da reta 1 : '))
reta02 = float(input('Informe o valor da reta 2 : '))
reta03 = float(input('Informe o valor da reta 3 : '))


if reta01 <= reta02 + reta03 and reta02 <= reta01 + reta03 and reta01 <= reta01 + reta02:
    print('É possivel criar um retangulo com as relas {}, {} e {}'.format(reta01, reta02, reta03))
else:
    print('Não é possivel formar um triangulo')
