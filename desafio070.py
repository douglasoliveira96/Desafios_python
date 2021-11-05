''' Crie um programa que leia o nome e o preço de vários produtos.
O programa deverá perguntar se o usuário vai continuar ou não.
No final, mostre:
A) qual é o total gasto na compra.
B) quantos produtos custam mais de R$1000.
C) qual é o nome do produto mais barato.'''
tot = maismil = menor = cont = 0
barato = ' '
while True:
    print('-'*30)
    produto = str(input('Nome do produto: ')).capitalize().strip()
    preço = float(input('Preço do produto: R$'))
    cont += 1
    resp = ' '
    tot += preço
    if preço > 1000:
        maismil += 1
    if cont == 1 or preço < menor:
        menor = preço
        barato = produto
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja continuar [S ou N]? ')).strip().upper()[0]
        print('-' * 30)
    if resp == 'N':
        break
print(f'\n\033[1mTotal = R${tot:.2f}')
print(f'{maismil} produtos custam mais de mil reais.')
print(f'O produto mais barato foi o {barato} que custa: R${menor:.2f}.')
