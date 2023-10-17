from random import randint
v = 0
while True:
    jogador = int(input('Diga um Valor:'))
    computador = randint(0,10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
       tipo =  str(input('Par ou Impar? [P/I].')).strip().upper()[0]
    print(f'Voce jogou {jogador} e o computador jogou {computador}. Total de {total}')
    if tipo == 'P':
        if total % 2 == 0:
            print('Voce VENCEU!!!')
            v += 1
        else:
            print('Voce PERDEU!!!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Voce VENCEU!!!')
            v += 1
        else:
            print('Voce PERDEU!!!!')
            break
    print('Vamos jogar')
print(f'GAME OVER" VOCE VENCEU {v} VEZES')