'''Crie um programa que simule o funcionamento de um caixa eletrônico.
No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro)
e o programa vai informar quantas cédulas de cada valor serão entregues.
OBS: considere que o caixa possui cédulas de R$100 R$50, R$20, R$10 R$5 e R$2.'''

print('=' * 30)
print('{:^30}'.format('\033[1;32mBANCO CEV\033[m'))
print('=' * 30)
valor = int(input('Qual o valor do saque? R$'))
total = valor
céd = 100
totcéd = 0

while True:
    if total >= céd:
        total -= céd
        totcéd += 1
    else:
        if totcéd > 0:
            print(f'Total de {totcéd} cédulas de R${céd}.')
        if céd == 100:
            céd = 50
        elif céd == 50:
            céd = 20
        elif céd == 20:
            céd = 10
        elif céd == 10:
            céd = 5
        elif céd == 5:
            céd = 2
        elif céd == 2:
            céd = 1
        totcéd = 0
        if total == 0:
            break

