'''cont = ('zero', 'um', 'dois', 'três', 'quatro',
        'cinco', 'seis', 'sete', 'oito', 'nove',
        'dez','onze','doze', 'treze', 'catorze',
        'quinze','dezesseis', 'dezesete', 'dezoito',
        'dezenove', 'vinte')

while True:
    num = int(input('Digite um numero de 0 a 20:'))
    if 0 <= num <= 20:
        break
    print('Tente novamente', end=' ')
print(f'Voce digitou o numero {cont[num]}')

resp = ' '
while resp not in 'SN':
    resp = str(input('Quer continuar? [S/N]')).strip().upper()[0]
if resp == 'N':
    break'''

cont = ('zero', 'um', 'dois', 'três', 'quatro',
        'cinco', 'seis', 'sete', 'oito', 'nove',
        'dez', 'onze', 'doze', 'treze', 'quatorze',
        'quinze', 'dezesseis', 'dezesete', 'dezoito',
        'dezenove', 'vinte')

while True:
    num = int(input('Digite um número entre 0 e 20: '))
    if 0 <= num <= 20:
        print(f'Você digitou o número {cont[num]}')
    else:
        print('Número fora do intervalo. Tente novamente.')

    resp = ' '
    while resp not in 'SN':
        resp = input('Quer continuar? [S/N]').strip().upper()[0]
    if resp == 'N':
        break













