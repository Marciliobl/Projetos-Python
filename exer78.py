lista = []
mai = 0
me = 0
for c in range(0,5):
    lista.append(int(input(f'Digite um Valor para a posição {c}:')))
    if c == 0:
        mai = me = lista[c]
    else:
        if lista [c] > mai:
            mai = lista[c]
        if lista[c] < me:
            me = lista[c]

print(f'Voce digitou os valores {lista}')
print(f'O maior valor digitado foi {mai} nas posições ', end='')

for i, v in enumerate(lista):
     if v == mai:
         print(f'{i}...', end='')
print()
print(f'O menor valor digitado foi {me} nas posições ', end='')

for i, v in enumerate(lista):
    if v == me:
        print(f'{i}...', end='')
print()