#Escreva um programa em Python que leia um número inteiro qualquer
#e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.
num = int(input('Digite um número inteiro qualquer: '))
print('''Escolha uma das bases para conversão:
[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL''')
opção = int(input('Sua opção: '))
if opção == 1:
    print('\033[1m{}\033[m convertido para \033[1;32mBINÁRIO\033[m é igual a \033[1;32m{}.\033[m'.format(num, bin(num)[2:]))
elif opção == 2:
    print('\033[1m{}\033[m convertido para \033[1;36mOCTAL\033[m é igual a \033[1;36m{}.\033[m'.format(num, oct(num)[2:]))
elif opção == 3:
    print('\033[1m{}\033[m convertido para \033[1;33mHEXADECIMAL\033[m é igual a \033[1;33m{}.\033[m'.format(num, hex(num)[2:]))
else:
    print('\033[31mOPÇÃO INVÁLIDA')