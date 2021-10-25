#Desenvolva um programa que leia os dois primeiros termos de uma P.A.
#No final, mostre a razão e os 10 primeiros termos dessa progressão.
soma = 0
cont = 0
n1 = int(input('Primeiro termo: '))
n2 = int(input('Segundo termo: '))
razão = n2 - n1
print('A razão entre {} e {} é {}.'.format(n1, n2, razão))
print('Os 10 primeiros termos dessa P.A são:')
for n in range(1, 11):
    soma += razão
    cont += 1
    print(n1 + soma, end=', ')
if razão > 0:
    print('\nP.A crescente.')
elif razão < 0:
    print('\nP.A decrescente.')
else:
    print('\nP.A constante.')
