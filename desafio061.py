#Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA,
#mostrando os 10 primeiros termos da progressão usando a estrutura while.
num = int(input('Digite o primeiro termo da P.A: '))
razão = int(input('Digite a razão dessa P.A: '))
print('Os 10 primeiros termos dessa P.A são:')
termo = num
cont = 1
while cont <= 10:
    print('{}, '.format(termo), end='')
    termo += razão
    cont += 1
print('FIM')
