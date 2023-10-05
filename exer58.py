from random import randint
computador = randint(0,10)
print('Sou seu computador, acabei de pensar em um numero entra 0 e 10.')
print('Será que voce consegue adivinhar qual foi?')
acertou = False
palpites = 0
while not acertou:
    jogador= int(input('Qual é o seu palpite?:'))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... tente novamente')
        elif jogador > computador:
            print('Menos... Tente mais uma vez!')
print('Acertou com {} tentativas, PARABENS!!!'.format(palpites))