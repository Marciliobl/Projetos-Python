print('-=-' * 10)
print('Analisador de Triagulos')
print('-=-'* 10)


r1 = float(input('Primeiro segmento:'))
r2 = float(input('Segundo segmento:'))
r3 = float(input('Terceiro segmento:'))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos a cima PODEM SE FORMA UM TRIANGULO')
else:
    print('Os segmentos a cima NAO PODE SE FORMA UM TRIANGULO')