#Crie um programa que leia vários números inteiros pelo teclado.
#O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
#No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).
n = 0
cont = -1
soma = -999
print('\033[1;37mPara parar digite [ 999 ].\033[m')
while n != 999:
    n = int(input('\033[1mDigite um número: \033[m'))
    soma += n
    if cont != 999:
        cont += 1
print('\033[1;4;35m{}\033[m \033[1;35mnúmeros foram digitados.'.format(cont))
print('O resultado da soma entre eles é igual a \033[1;4;35m{}\033[m.'.format(soma))
