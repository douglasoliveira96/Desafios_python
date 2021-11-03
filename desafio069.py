''' Crie um programa que leia a idade e o sexo de várias pessoas.
A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar.
No final, mostre:
A) quantas pessoas tem mais de 18 anos.
B) quantos homens foram cadastrados.
C) quantas mulheres tem menos de 20 anos.'''
from time import sleep
tot = tot18 = totH = totM20 = 0
while True:
    tot += 1
    print('\033[1m-' * 30)
    print('CADASTRO')
    print('-' * 30)
    idade = int(input(f'Qual é a idade da {tot}° pessoa? '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input(f'Qual é o sexo da {tot}° pessoa? ')).upper().strip()[0]
    if idade > 18:
        tot18 += 1
    if sexo == 'M':
        totH += 1
    if sexo == 'F' and idade < 20:
        totM20 += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input(f'Deseja continuar? \033[m')).upper().strip()[0]
    if resp == 'N':
        break
print('...')
sleep(1)
print(f'\033[1;32;40mCadastramos {tot} pessoas no total.\033[m')
print(f'\033[1;32;40mTemos {tot18} pessoas com mais de 18 anos.\033[m')
print(f'\033[1;32;40mTemos {totH} homens cadastrados.\033[m')
print(f'\033[1;32;40mTemos {totM20} mulheres com menos de 20 anos.\033[m')
