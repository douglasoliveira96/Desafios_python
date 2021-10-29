#Faça um programa que leia um número qualquer e mostre o seu fatorial.
from math import factorial
num = int(input('Digite um número para saber o seu fatorial: '))
fatorial = factorial(num)
print('O fatorial de {}! é {}.'.format(num, fatorial))
