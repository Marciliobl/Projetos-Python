num = (int(input('Digite um numero: ')),
       int(input('Digite outro numero: ')),
       int(input('Digite mais um numero: ')),
       int(input('Digite o ultimo numero numero: ')))
print(f'Voce digitou os valoers {num}')
print(f'O valor 9 apareceu {num.count(9)} vezes')
if 3 in num:
    print(f'O valor 3 apareceu na {num.index(3)}')
else:
    print('O valor 3 nao foi digitado em nenhuma posição')
print(f'O valor 3 apareceu na {num.index(3)+1}° posição')
print('Os valores pares digitados foram', end='')
for n in num:
    if n % 2 == 0:
        print(n, end='')