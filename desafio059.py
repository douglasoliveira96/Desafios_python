#Crie um programa que leia dois valores e mostre um menu na tela:
#[ 1 ] somar
#[ 2 ] multiplicar
#[ 3 ] maior
#[ 4 ] novos números
#[ 5 ] sair do programa
#Seu programa deverá realizar a operação solicitada em cada caso.
from time import sleep
valor1 = int(input('Digite o primeiro valor: '))
valor2 = int(input('Digite o segundo valor: '))
opção = 0
while opção != 5:
    print('\nPara somar, digite [ 1 ].')
    print('Para multiplicar, digite [ 2 ].')
    print('Para saber qual é o maior, digite [ 3 ].')
    print('Para digitar novos valores, digite [ 4 ].')
    print('Para sair do programa, digite [ 5 ].')
    opção = int(input('\n\033[1;34;40mO que deseja fazer?\033[m '))
    if opção == 1:
        soma = valor1 + valor2
        print('\033[1;34mA soma entre {} e {} é {}.\033[m'.format(valor1, valor2, soma))
    elif opção == 2:
        multiplicação = valor1 * valor2
        print('\033[1;34m{} multiplicado por {} é igual a {}.\033[m'.format(valor1, valor2, multiplicação))
    elif opção == 3:
        if valor1 > valor2:
            maior = valor1
        else:
            maior = valor2
        print('\033[1;34mEntre {} e {} o maior valor é o {}.\033[m'.format(valor1, valor2, maior))
    elif opção == 4:
        print('Informe os valores novamente: ')
        valor1 = int(input('Primeiro valor: '))
        valor2 = int(input('Segundo valor: '))
    elif opção == 5:
        print('Finalizando...')
        sleep(1)
    else:
        print('Opção inválida!')
print('Fim do programa! Volte sempre!')

