num01 = int(input('Informe o primeiro valor - : '))
num02 = int(input('Informe o segundo valor - : '))
num03 = int(input('Informe o ultimo valor - : '))

# Verificando o valor menor
menor = num01
if num02 < num01 and num02 < num03:
    menor = num02
if num03 < num01 and num03 < num02:
    menor = num03

# Verifica o valor maior
maior = num01
if num02 > num01 and num02 > num03:
    maior = num02
if num03 > num01 and num03 > num02:
    maior = num03


print('O menor numero digitado foi {}'.format(menor))
print('P=O maior valor digitado foi {}'.format(maior))

