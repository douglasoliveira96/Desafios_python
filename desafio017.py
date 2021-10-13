'''Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo.
Calcule e mostre o comprimento da hipotenusa.
a = float(input('Digite quanto mede o cateto adjacente: '))
b = float(input('Digite quanto mede o cateto oposto: '))
h = (a**2 + b**2) ** (1/2)
print('A hipotenusa mede: {:.2f}'.format(h))'''
from math import hypot
a = float(input('Digite quanto mede o cateto adjacente: '))
b = float(input('Digite quanto mede o cateto oposto: '))
h = hypot(a, b)
print('A hipotenusa mede: {:.2f}'.format(h))



