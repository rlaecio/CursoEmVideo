seuNome = str(input('Digite seu nome: ')).upper().strip()

letra = 'A'
numVezes = seuNome.count('A')
posicaoInicio = seuNome.find('A')+1
posicaoFim = seuNome.rfind('A')+1

print('A letra {} aparece {} vezes no nome.'.format(letra, numVezes))
print('A primeira latra {} apareceu na posiçao {}'.format(letra, posicaoInicio))
print('A última letra {} apareceu na posiçao {}'.format(letra, posicaoFim))