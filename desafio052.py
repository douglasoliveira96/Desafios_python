#Faça um programa que leia um número inteiro e diga
#se ele é ou não um número primo.
num = int(input('Digite um número: '))
tot = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[1;35m', end='')
        tot += 1
    else:
        print('\033[1;37m', end='')
    print('{} \033[m'.format(c), end='')
if tot == 2:
    print('\nO número \033[1;35m{}\033[m é \033[1;35mPRIMO.\033[m'.format(num))
else:
    print('\nO número \033[1;37m{}\033[m \033[1;37mNÃO É PRIMO.\033[m'.format(num))
