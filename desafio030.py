#Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.
num = int(input('\033[1mDigite um número qualquer: '))
resto = (num % 2)
if resto == 0:
    print('O número \033[1;34m{}\033[m \033[1mé um número \033[1;34mPAR'.format(num))
else:
    print('O número \033[1;31m{}\033[m \033[1mé um número \033[1;31mÍMPAR'.format(num))
