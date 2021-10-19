#Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))
print('Os números digitados foram \033[1;32m{}, {}, {}.\033[m'.format(n1, n2, n3))
# Verificando quem é menor...
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
# Verificando quem é maior...
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
print('O \033[1;33mMENOR\033[m número digitado foi o \033[1;33m{}\033[m e o \033[1;35mMAIOR\033[m número digitado foi o \033[1;35m{}\033[m.'.format(menor, maior))

