#Faça um programa que leia um ângulo qualquer e mostre na tela
#o valor do seno, cosseno e tangente desse ângulo.
from math import radians, sin, cos, tan
ângulo = float(input('Digite o valor do ângulo: '))
seno = sin(radians(ângulo))
print('O ângulo de {} tem o SENO de: {:.2f}'.format(ângulo, seno))
cosseno = cos(radians(ângulo))
print('O ângulo de {} tem o COSSENO de: {:.2f}'.format(ângulo, cosseno))
tangente = tan(radians(ângulo))
print('O ânguluo de {} tem a TANGENTE de {:.2f}'.format(ângulo, tangente))