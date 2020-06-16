from math import hypot
co = float(input('Informe o cateto oposto '))
ca = float(input('Informe o cateto adjacente '))
hipotenusa = (co ** 2 + ca ** 2) ** (1/2)
print('Modo 1 - O valor da hipotenusa {:.2f}'.format(hipotenusa))
hipotenusa = hypot(co, ca)
print('Modo 2 - O valor da hipotenusa {:.2f}'.format(hipotenusa))
