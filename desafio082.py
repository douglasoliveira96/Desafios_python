'''Crie um programa que vai ler vários números e colocar em uma lista. 
Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. 
Ao final, mostre o conteúdo das três listas geradas.'''

num = []
par = []
ímpar = []
while True:
    num.append(int(input('Digite um número: ')))
    continuar = str(input('Deseja continuar [S ou N]? ')).strip().upper()[0]
    if continuar in 'Nn':
        break
for i, v in enumerate(num):
    if v % 2 == 0:
        par.append(v)
    else:
        ímpar.append(v)
print('-=' * 30)
print(f'Os números digitados foram: {num}.')
print(f'Os números pares foram: {par}.')
print(f'Os números ímpares foram: {ímpar}.')
print('-=' * 30)



