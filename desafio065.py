#Crie um programa que leia vários números inteiros pelo teclado. No final da execução,
#mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
#O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
continua = 'S' or 'N'
cont = 0
soma = 0
maior = menor = 0
while continua == 'S':
    n = int(input('Digite um número: '))
    continua = str(input('Quer continuar? [S ou N] ')).upper().strip()[0]
    cont += 1
    soma += n
    média = soma / cont
    if cont == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
print('\n\033[4mVocê digitou {} números e a média foi {:.2f}.'.format(cont, média))
print('O maior número digitado foi o {} e o  menor número foi o {}.'.format(maior, menor))
