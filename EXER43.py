peso = float(input('Qual é seu peso (Kg)?:'))
altura = float(input('Qual é sua altura em (M):'))
imc = peso / (altura ** 2 )
print('O IMC dessa pessoa é de {:.1f}'.format(imc))
if imc < 18.5:
    print('Voce estar Abaixo do PESO')
elif  18.5 <= imc <25:
    print('Voce estar no peso ideal')
elif  25 <= imc <30:
    print('Voce esta em Sobre peso')
elif 30 <= imc < 40:
    print('Voce estar Obeso')
else:
    print('Voce estar em Obesidade morbida')