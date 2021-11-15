'''Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, 
cadastrando tudo em uma lista composta'''

from random import randint
from time import sleep
print('\033[35;40m=-\033[m' * 20)
print('            \033[1;33mM E G A  S E N A\033[m')
print('\033[35;40m-=\033[m' * 20)

lista = list()
jogos = list()
quant = int(input('Quer que eu sorteie quantos jogos? '))
tot = 1
while tot <= quant:
    cont = 0 
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos .append(lista[:])
    lista.clear()
    tot +=1
print('>' * 5, f' SORTEANDO {quant} JOGOS ', '<' * 5)
for i, l in enumerate(jogos):
    sleep(1)
    print(f'Jogo {i+1}: {l}')
print('BOA SORTE!')
print()
