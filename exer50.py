soma = 0
cont = 0
for c in range(1, 7):
    num = int(input('Digite o {}° numero:'.format(c)))
    if num % 2 == 0:
        soma = soma + num
        cont = cont + 1
print('Voce informou {} numeros PARES e a soma é {}'.format(cont, soma))

