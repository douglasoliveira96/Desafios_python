#Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10.
#Só que agora o jogador vai tentar adivinhar até acertar,
#mostrando no final quantos palpites foram necessários para vencer.
from time import sleep
from random import randint
print('-'*50)
print('\033[1;34;40mO COMPUTADOR IRÁ PENSAR EM UM NÚMERO ENTRE 0 E 10.\033[m')
print('-'*50)
sleep(1.5)
computador = randint(0, 10)
palpites = 1
jogador = int(input('\033[1;34;40mEm qual número o computador pensou?\033[m '))
while jogador != computador:
    sleep(0.25)
    jogador = int(input('\033[31mVocê errou, tente novamente: \033[m'))
    palpites += 1
if palpites == 1:
    print('\n\033[1;7;30;46mPARABÉNS, SORTUDO, você acertou de primeira.\033[m')
if palpites > 6:
    print('\033[37mAzarado\033[m')
print('\033[1;34mVOCÊ ACERTOU!\033[m')
print('\033[34mForam necessários \033[4m{} palpites\033[m \033[34maté que você acertasse.\033[m'.format(palpites))
