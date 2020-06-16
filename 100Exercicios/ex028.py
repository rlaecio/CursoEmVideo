import random
numeroMemoria = random.randrange(1, 50)

numeroUsuario = int(input('Digite um numero de 1 a 50: '))

if (numeroMemoria == numeroUsuario):
    print('Parabens, você acertou')
else:
    print('Você errou, o numero pensado foi {}'.format(numeroMemoria))
