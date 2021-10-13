#Programa que lê um número inteiro
#e mostra na tela
#seu sucessor e anterior,
#seu dobro, seu triplo e sua raiz quadrada.
n = int(input('Digite um número: '))
s = n + 1
a = n - 1
d = n * 2
t = n * 3
r = n ** (1/2)
print('O sucessor de {} é {}'.format(n, s))
print('O anterior de {} é {}'.format(n, a))
print('O dobro de {} é {}'.format(n, d))
print('O triplo de {} é {}'.format(n, t))
print('A raiz quadrada de {} é {:.2f}'.format(n, r))



