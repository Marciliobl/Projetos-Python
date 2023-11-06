numeros = list()
while True:
    n = int(input('Digite um valor:'))
    if  n not in numeros:
        numeros.append(n)
        print('Valor adicionado com sucesso!!..')
    else:
        print('Valor Duplicado não vou adicionar...')

    r = str(input('Quer continuar?? [S/N]?')).strip().upper()[0]
    if r in 'Nn':
        break

numeros.sort()
print(f'Voce digitou os valos {numeros}')