'''Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.'''

cont = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco',
        'seis', 'sete', 'oito', 'nove', 'dez',
        'onze', 'doze', 'treze', 'catorze', 'quinze',
        'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

continua = 'S'
while True:
    num = int(input('Digite um número entre 0 e 20: '))
    if 0 <= num <= 20:
        break
    print('ERRO')
print(f'Você digitou o número \033[4m{cont[num]}\033[m.')
while continua == 'S':
    continua = str(input('\nDeseja continuar [S ou N]? ')).strip().upper()[0]
    num = int(input('\nDigite um número entre 0 e 20: '))
    print(f'Você digitou o número \033[4m{cont[num]}\033[m.')
