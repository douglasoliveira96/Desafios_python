#Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher,
#só que agora utilizando um laço for.
n = int(input('Digite um número: '))
for vezes in range(1, 11):
    igual = n * vezes
    print('{} x {} = \033[1m{}\033[m'.format(n, vezes, igual))

