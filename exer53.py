frase = str(input('Digite uma frase:')).strip().upper()
palavras = frase.strip()
junto: str = ''.join(palavras)

inverso = junto [::-1]
'''for letra in range(len(junto) - 1,-1, -1):
    inverso += junto[letra]'''
print('o inverso de {} é {}'.format(junto, inverso))
if inverso == junto:
    print('Temos um palindromo!')
else:
    print('Nao é um palindromo!')