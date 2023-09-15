from random import shuffle
n1 = str(input('Primeiro:'))
n2 = str(input('Segundo:'))
n3 = str(input('Terceiro:'))
n4 = str(input('Quarto:'))
n5 = str(input('Quinto:'))
n6 = str(input('Sexto:'))

lista = [n1, n2, n3, n4, n5, n6]
shuffle (lista)
print('Esta é uma ordem aleatoria de quem é mais gay nesse grupo:')
print(lista)