velocidade = float(input('Qual a velocidade do seu carro?:'))
if velocidade > 80:
    print('VOCÊ FOI MULTADO0, o limite permitido é ate 80Km/h'.format(velocidade))
    multa = (velocidade-80) *7
    print('Voce deve pagar uma multa de {:.2f}R$'.format(multa))
print('DIRIJA COM SEGURANÇA!!!')