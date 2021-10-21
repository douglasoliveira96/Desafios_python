# Escreva um programa que leia dois números inteiros e compare-os.
#mostrando na tela uma mensagem:
#– O primeiro valor é maior
#– O segundo valor é maior
#– Não existe valor maior, os dois são iguais
num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
if num1 > num2:
    print('O PRIMEIRO número digitado é maior.')
    print('O número {} é maior que o número {}.'.format(num1, num2))
elif num1 < num2:
    print('O SEGUNDO número digitado é maior.')
    print('O número {} é menor que o número {}.'.format(num1, num2))
elif num1 == num2:
    print('Não existe valor maior, os dois números são IGUAIS.')
