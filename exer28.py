from random import randint
from time import sleep

computador = randint (0, 5) #faz o computador sortear o numero
print('-=-'* 20)
print('Vou pensar em um numero entre 0 e 5. Tente adivinhar...')
print('-=-'* 20)
jogador = int(input('Enque numero eu pensei...?'))  #o jogador tentar adivinhar
print('PROCESSANDO...')
sleep(2)
print('Tente novamente')
if jogador == computador:
    print('Parabens voce acertou o numero *.*')

else:
    print('GANHEI eu pensei no numero {} e não no {}'.format(computador, jogador))
