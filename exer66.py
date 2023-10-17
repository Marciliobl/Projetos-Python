n = s = 0
while True:
    num = int(input('Digite um numero  [APERTE 999 PARA PARAR O PROGRAMA]:'))
    if num == 999:
        break
    s += num
print(f'A soma total é de {s}')