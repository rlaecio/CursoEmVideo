from math import radians, cos, sin, tan

angulo = float(input('Informe o angulo para o calculo : '))
ang = radians(angulo)
coss = cos(ang)
senn = sin(ang)
tang = tan(ang)
print('O cosseno de  {:.0f} é {:.2f} '.format(angulo, coss))
print('O seno de {:.0f} é {:.2f}'.format(angulo, senn))
print('A tangente de  {:.0f} é {:.2f}'.format(angulo, tang))