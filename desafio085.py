'''Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os 
em uma lista única que mantenha separados os valores pares e ímpares. 
No final, mostre os valores pares e ímpares em ordem crescente.'''

usuário = []
pares = []
ímpares = []
print('=-' * 16)
print('{:^32}'.format('USUÁRIO, DIGITE 7 VALORES.'))
print('=-' * 16)
for u in range(1, 8):
    usuário.append(int(input(f'Digite o {u}° valor: ')))
print(f'\nValores digitados: {usuário}.')
for i, v in enumerate(usuário):
    if v % 2 == 0:
        pares.append(v)
        pares.sort()
    else:
        ímpares.append(v)
        ímpares.sort()
print(f'Valores pares: {pares}.')
print(f'Valores ímpares: {ímpares}.')
print()
