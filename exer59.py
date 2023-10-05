n1 = int(input('Primeiro valor:'))
n2 = int(input('Segundo valor:'))
opcao = 0
while opcao !=5:
    print('''    [1] somar:
    [2] multiplicar:
    [3] maior:
    [4] novos numeros:
    [5] sair do programa:''')
    opcao = int(input('Qual a sua opção?:'))
    if opcao == 1:
        soma = (n1 + n2)
        print('A soma entre {} e {} é {}'.format(n1, n2, soma))
    elif opcao == 2:
        opcao == 2
        produto = n1 * n2
        print('O resultado de {} e {} é {}'.format(n1, n2, produto))
    elif opcao == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('entre {} e {} o maior é {}'.format(n1, n2, maior))
    elif opcao == 4:
        print('informa os valores novamednte!')
        n1 = int(input('Primeiro valor:'))
        n2 = int(input('Segundo Valor:'))
    elif opcao == 5:
        print('Finalizando...')
    else:
        print('Opção invalida!!')
print('fim do programa!!!')

