#Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos.
#O programa encerrará quando ele disser que quer mostrar 0 termos.
print('GERADOR DE P.A')
primeiro = int(input('Digite o primeiro termo da P.A: '))
razão = int(input('Digite a razão dessa P.A: '))
print('\nOs 10 primeiros termos dessa P.A são: ')
termo = primeiro
cont = 1
mais = 10
total = 0
while mais != 0:
    total = total + mais
    while cont <= total:
        print('\033[1m{},\033[m '.format(termo), end='')
        termo += razão
        cont += 1
    print('PAUSA...')
    mais = int(input('Deseja saber mais termos dessa P.A? Quantos? '))
print('\nFIM')
print('\n\033[4mForam exibidos {} termos dessa P.A.'.format(total))
