from datetime import date

ano = int(input('Que ano quer analisar? coloque ) para analisar o ano atual: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 or ano % 100 == 0:
    print('O ano {} é BISEXTO'.format(ano))
else:
    print('O ano {} NÃO é BISEXTO'.format(ano))
