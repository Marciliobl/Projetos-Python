num = int(input('Me diga um numero qualquer:'))
resultado = num %2
if resultado == 0:
    print('O numero {} é PAR'.format(num))
else:
    print('O numero {} é IMPAR'.format(num))