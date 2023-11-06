valores =[]
while True:
    valores.append(int(input('digite um Valor:')))
    resp = str(input('Quer continuar? [S/N]'))
    if resp in 'Nn':
        break
print('-='* 30)
print(f'Voce digitou {len(valores)} elementos')
valores.sort(reverse=True)
print(f'Os valores em ordem decrescente é {valores}')
if 5 in valores:
    print('O numero 5 faz parte da lista')
else:
    print('O valor 5 nao foi encontrado na lista')