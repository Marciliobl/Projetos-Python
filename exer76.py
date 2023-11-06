lista = ('Lapis', 1.50,
         'Borracha', 0.50,
         'caderno', 5.00,
         'Estojo', 6.50,
         'Compasso', 5.00,
         'Machila', 100.00,
         'Canetas', 1.00,
         'Livros', 10.00)
for pos in range(0, len(lista)):
    if pos % 2 == 0:
        print(f'{lista[pos]:.<30}', end='')
    else:
        print(f'R$ {lista[pos]:>7.2f}')
