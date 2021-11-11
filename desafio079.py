'''Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.'''
from time import sleep
valor = []
while True:
    v = int(input('\nDigite um valor: '))
    if v not in valor:
        valor.append(v)
        print('\033[1mAdicionado com sucesso!\033[m')
    else:
        print('\033[31mValor duplicado! Não vou adicionar!\033[m')
    continuar = str(input('Deseja continuar [S ou N]? ')).strip().upper()[0]
    if continuar in 'Nn':
        break
print('\n\033[1mAnalisando...\033[m')
sleep(1)
valor.sort()
print(f'\n\033[1;36;40mOs valores digitados foram {valor}.\033[m\n')