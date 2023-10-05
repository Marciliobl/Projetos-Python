sexo = str(input('informa seu sexo [M/F]')).upper().strip()[0]
while sexo not in 'MmFf':
    sexo = str(input('Dados invalidos, por favor informe seu sexo:')).strip().upper()[0]
print('Sexo {} registrado com sucesso.'.format(sexo))
