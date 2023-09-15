from datetime import date

atual = date.today().year
sexo = str(input('Digite Seu Sexo:'))
if sexo == 'Feminino':
    print("Voce não é Obrigada a se alistar, caso queira continue com o procedimento!")

nascimento = int(input('Ano de nascimento:'))
idade = atual - nascimento
print('Quem nasceu em {} tem {} anos.'.format(nascimento, idade, atual))
if idade == 18:
    print('Voce tem que se alistar IMEDIATAMENTE'.format())
elif idade < 18:
    saldo = 18 - idade
    print('Voce ainda nao tem 18 anos, ainda falta {} anos para o alistamento'.format(saldo))
    ano = atual + saldo
    print('Seu alistamenteo será em {} ano'.format(ano))
elif idade > 18:
    saldo = idade - 18
    ano = atual - saldo
    print('Seu alistamento foi em {}'.format(ano))
    print('Voce ja deveria ter se alistado há {} anos'.format(saldo))
