from datetime import date
atual = date.today().year

nascimento = int(input('Digite o seu ano de nascimento'))
idade = atual - nascimento
print('O atleta tem {} anos'.format(idade))
if idade <= 9:
    print('Classificaçã MIRIM')
elif idade > 9 and idade <=14:
    print('Classificação: INFANTIL')
elif idade <=19:
    print('Classificação: JUNIOR')
elif idade <= 25:
    print('Classificação: SENIOR')
elif idade > 25:
    print('Classificação: MASTER')

