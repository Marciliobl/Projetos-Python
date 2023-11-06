times = ('bota fogo', 'bragantino', 'flamengo', 'gremio',
         'palmeiras', 'athletico-PR', 'athletico-MG', 'fortaleza',
         'fluminense', 'cuiaba', 'sao paulo', 'internacional',
         'corinthinhas', 'bahia', 'cruzeiro', 'vasco da gama',
         'santos', 'goias', 'coritiba', 'america-MG')
print('=-'*100)
print(f'Lista de times {times}')
print('=-'*100)
print(f'Os 5 primeiros sao {times[0:5]}')
print(f'Os 4 ultimos colocados {times [-4:]}')
print(f'Times em ordem alfabetica: {sorted(times)}')
print(f'O Vasco estar na {times.index("vasco da gama")+1} posição.')