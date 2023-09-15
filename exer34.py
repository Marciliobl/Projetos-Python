num = float(input('Qual o valor do seu salario?:'))
if num <= 1250:
    novo = num + (num * 15 / 100)
else:
    novo = num + (num * 10 / 100)
print('Seu novo Salario é {}'.format(novo))
