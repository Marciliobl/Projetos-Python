from random import randint
from time import sleep

pc = randint(0, 5)
print('-=-' * 20)
print('VAMOS JOGAR, TENTE ADIVINHAR O NUMERO QUE EU PENSEI')
print('-=-' * 20)
jogador = int(input('Digite um numero entre 0 e 5:'))
print('PROCESSANDO...')
sleep(3)
if jogador == pc:
    print('PARABENS, VOCE ACERTOU')
else:
    print('EU GANHEI, na verdade eu pensei no numero {} e nao no {}'.format(pc, jogador))
