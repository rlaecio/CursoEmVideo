from math import trunc

num = float(input('Digite um numero: '))
porInteira = trunc(num)

print('O valor digital foi {}, e sua porçao inteira é {}'.format(num, porInteira))
print('A porção inteira é {:.0f}'.format(num))

