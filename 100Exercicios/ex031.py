num = int(input('informe a distancia em KM, para o destino : '))

if(num <= 200):
    print('O valor da passagem será R${:.2f}'.format(num * 0.50))

else:
    print('O valor da passagem será R${:.2f}'.format(num * 0.45))
