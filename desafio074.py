''''Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.'''

from random import randint
from time import sleep
n = (randint(1, 10), randint(1, 10), randint(1, 10),
     randint(1, 10), randint(1, 10))
print('Sorteando...')
sleep(1)
print(f'Os valores sorteados foram: \033[1m{n}\033[m.')
print(f'O maior número sorteado foi o \033[1m{max(n)}\033[m.')
print(f'O menor número sorteado foi o \033[1m{min(n)}\033[m.')
