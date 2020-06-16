base = float(input('Informe a largura da base da parede: '))
altura = float(input('Informe a altura da parede: '))
area = base * altura
print('Area = {}' .format(area))
latas = area / 2
#print('Latas = {}' .format(latas))
resto = area % 2
#print('Resto = {}' .format(resto))
total = latas + resto
#print('Final = {}' .format(total))
print('Para pintar a area total da parede, precisamos: {} '
      'latas de tinta' .format(total))
