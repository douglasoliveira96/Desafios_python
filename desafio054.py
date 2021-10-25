#Crie um programa que leia o ano de nascimento de sete pessoas.
#No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
from datetime import date
totalmaior = 0
totalmenor = 0
atual = date.today().year
for n in range(1, 8):
    ano = int(input('Em que ano a {}° pessoa nasceu? '.format(n)))
    idade = atual - ano
    if idade >= 18:
        totalmaior += 1
        print('\033[1m{} anos MAIOR DE IDADE\033[m'.format(idade))
    else:
        totalmenor += 1
        print('\033[1;37m{} anos MENOR DE IDADE\033[m'.format(idade))
print('\n\033[1mAo todo temos\033[m \033[1;36m{}\033[m \033[1mpessoas maiores de idade e\033[m \033[1;36m{}\033[m \033[1mpessoas menores de idade.\033[m'.format(totalmaior, totalmenor))
