nome = str(input('Digite seu nome:')).upper().strip()
print('A letra A aparece {} vezes na frase'.format(nome.count('A')))
print('A letra A aparece na posição {}'.format(nome.find('A')+1))
print('A Letra A aparece a ultima vez em {}'.format(nome.rfind('A')+1))