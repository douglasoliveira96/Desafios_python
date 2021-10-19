#Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
r1 = float(input('Digite o comprimento da reta1: '))
r2 = float(input('Digite o comprimento da reta2: '))
r3 = float(input('Digite o comprimento da reta3: '))
if (r1 + r2) > r3 and (r2 + r3) > r1 and (r3 + r1) > r2:
    print('As três retas digitadas \033[1;34mPODEM\033[m formar um triângulo.')
else:
    print('As três retas digitadas \033[1;31mNÃO PODEM\033[m formar um triângulo.')