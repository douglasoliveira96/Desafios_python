#Faça um programa que leia um ano qualquer e mostre se ele é bissexto
from datetime import date
ano = int(input('Digite um ano qualquer: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano de \033[4m{}\033[m \033[1;36mé Bissexto!'.format(ano))
else:
    print('O ano de \033[4m{}\033[m \033[1;31mnão é Bissexto!'.format(ano))
