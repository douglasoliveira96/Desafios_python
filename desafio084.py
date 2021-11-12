'''Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves.'''

temp = []
princ = []
maior = menor = 0
while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))
    if len(princ) == 0:
        maior = menor = temp[1]
    else: 
        if temp[1] > maior:
            maior = temp[1]
        if temp[1] < menor:
            menor = temp[1] 
    princ.append(temp[:])
    temp.clear()
    continuar = str(input('Deseja continuar [S ou N]? ')).upper()[0]
    if continuar in 'Nn':
        break
print('=' * 50)
print(f'Os dados foram {princ}.')
print(f'{len(princ)} pessoas foram adicionadas.')
print(f'O maior peso foi {maior}KG.')
print(f'O menor peso foi {menor}KG.')
print('=' * 50)
