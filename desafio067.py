#Faça um programa que mostre a tabuada de vários números, um de cada vez,
#para cada valor digitado pelo usuário.
#O programa será interrompido quando o número solicitado for negativo.
cont = 1
c = 1
print('\033[37mCaso digite um número negativo o programa será encerrado.\033[m')
while True:
    num = int(input('\033[1mDigite um número para saber sua tabuada: \033[m'))
    if num < 0:
        break
    print('-' * 12)
    for c in range(1, 11):
        multi = num * c
        print(f'\033[34m{num} x {c} = {multi}\033[m')
    print('-' * 12)
print('\n\033[31mPrograma encerrado.')

