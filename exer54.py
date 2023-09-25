from datetime import date
atual = date.today().year
totalmaior = 0
totalmenor = 0
for pess in range ( 1, 8):
    ano1 = int(input('Em qua ano {}° a pessoa nasceu?:'.format(pess)))
    idade = atual - ano1
    if idade >=21:
        totalmaior += 1

    else:
        totalmenor+= 1
print('Ao todo tivemos {} pessoas maiores de idade e  {} menores de idade!'.format(totalmaior, totalmenor))
