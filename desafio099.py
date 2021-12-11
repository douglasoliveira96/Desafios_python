'''Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior.'''

from time import sleep
def maior(* num):
    cont = maior = 0
    print('\nAnalisando os valores passados...') 
    for valor in num:
        print(f' {valor}', end='', flush=True)
        sleep(0.3)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'\nForam digitados {cont} valores, o maior deles foi o {maior}.')
# Programa principal

maior(2, 3, 6, 1, 7, 9)
maior(3, 5, 8, 4)
maior(3, 9, 1, 10, 8)
maior(6, 4)
