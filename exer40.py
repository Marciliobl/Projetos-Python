nota1 = float(input('Digite sua primeira nota:'))
nota2 = float(input('Digite sua segunda nota:'))
media = (nota1 + nota2) / 2
print('Tirando {:.1f} e {:.1f} e media do aluno é {}'.format(nota1, nota2, media))
if 7 > media >=5:
    print('O aluno estar em RECUPERAÇÃO!!!')
elif media <5:
    print('O aluno estar REPROVADO')
else:
    print('O aluno estar APROVADO!!!')