#Crie um programa que mostre na tela todos os números pares
#que estão no intervalo entre 1 e 50
from time import sleep
print('\033[1;30;46mOs números pares de 1 a 50 são:\033[m ')
for num in range(2, 51, 2):
        print('\033[1;34m{}\033[m'.format(num))
        sleep(0.30)
print('\033[1;31mFIM\033[m')
