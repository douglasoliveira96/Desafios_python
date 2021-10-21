#Faça um programa que leia o ano de nascimento de um jovem e informe,
#de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar,
#se é a hora exata de se alistar ou se já passou do tempo do alistamento.
#Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
from datetime import date
ano = int(input('Informe seu ano de nascimento: '))
idade = date.today().year - ano
faltam = 18 - idade
passou = idade - 18
if idade < 18 and faltam > 1:
    print('Você tem {} anos, ainda \033[1;31mnão está na hora\033[m de se alistar.'.format(idade))
    print('Faltam {} anos'.format(faltam))
elif faltam == 1: #Coloquei essa linha simplesmente para que o programa esteja escrito corretamente no plural
    print('Você tem {} anos, ainda \033[1;31mnão está na hora\033[m de se alistar.'.format(idade))
    print('Falta {} ano.'.format(faltam))
elif idade == 18:
    print('Você já fez ou fará {} anos esse ano, já \033[1;34mestá na hora\033[m de se alistar.'.format(idade))
elif idade > 18 and passou > 1:
    print('\033[1;4;33mVocê já passou do tempo de alistamento.\033[m')
    print('Está {} anos atrasado e deverá pagar \033[1;31mmulta.\033[m'.format(passou))
elif passou == 1: #Coloquei essa linha simplesmente para que o programa esteja escrito corretamente no plural
    print('\033[1;4;33mVocê já passou do tempo de alistamento.\033[m')
    print('Está {} ano atrasado e deverá pagar \033[1;31mmulta.\033[m'.format(passou))
