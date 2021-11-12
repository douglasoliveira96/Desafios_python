''' Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, mostre:
A) Quantos números foram digitados. 
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista.'''

num = []
cont = 0
while True:
    num.append(int(input('Digite um número: ')))
    cont += 1
    continuar = str(input('Deseja continuar [S ou N]? ')).strip().upper()[0]
    if continuar in 'Nn':
        break
num.sort(reverse = True)
print(f'\nVocê digitou {cont} números.')
print(f'Os números digitados em ordem decrescente: {num}.')
if 5 in num:
    print('O número 5 está na lista.')
else:
    print('O número 5 não foi encontrado na lista.')
