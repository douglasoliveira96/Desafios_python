'''Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla.
No final, mostre:
A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os números pares.'''

num = (int(input('Digite um número: ')),
    int(input('Digite outro número: ')),
    int(input('Digite mais um número: ')),
    int(input('Digite o último número: ')))

print(f'\n\033[1;35;40mOs números digitados foram: {num}\033[m')
print(f'\033[1;35;40mO número 9 apareceu {num.count(9)} vezes.\033[m')
if 3 in num:
    print(f'\033[1;35;40mO número 3 apareceu na {num.index(3)+1}ª posição.\033[m')
else:
    print('\033[1;35;40mO número 3 não foi digitado em nenhuma posição.\033[m')
print('\033[1;35;40mOs números pares digitados foram: \033[m')
for n in num:
    if n % 2 == 0:
        print(f'\033[1;4;35m{n}\033[m', end=' ')

