nome = str(input('Qual é seu nome:?:'))
if nome == 'Marcilio':
    print('Que nome Lindooooo!!!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Aline':
    print('Seu nome é bem popular no brasil')
else:
    print('Seu nome é bem normal')
print('Tenha um bom dia, {}!'.format(nome))