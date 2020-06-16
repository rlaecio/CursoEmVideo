velocidade = float(input('Informe a velocidade do veiculo : '))

if (velocidade <= 80):
    print('Parabéns, você respeita os limites de velocidade')
else:
    print('Você excedeu os limites da velocidade com {}km/h.'.format(velocidade))
    print('Será multado no valor de R${:.2f}, pelos {}kms excedidos'.format((velocidade - 80) * 7, velocidade-80))

