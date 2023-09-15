distancia = float(input('Qual a distancia da sua viagem?:'))
print('Voce estar preste a começar uma viagem de {}km'.format(distancia))
if distancia <= 200:
    preço = distancia * 0.50
    print('Sua viagem vai ficar no valor total de {}$'.format(preço))
else:
    preço = distancia * 0.45
    print('Sua Viagem vai custar {}$'.format(preço))
