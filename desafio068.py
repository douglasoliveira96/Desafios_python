#Faça um programa que jogue par ou ímpar com o computador.
#O jogo só será interrompido quando o jogador perder, mostrando o total
#de vitórias consecutivas que ele conquistou no final do jogo.
from random import randint
import pygame
v = 0
while True:
    print('-'*30)
    jogador = int(input('Digite um número: '))
    computador = randint(0, 10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar [P ou I]? ')).strip().upper()[0]
    print(f'Você escolheu {jogador}.')
    print(f'O computador escolheu {computador}.')
    print(f'A soma dá {total}.')
    print('\033[1mDeu PAR.\033[m' if total % 2 == 0 else '\033[1mDeu ÍMPAR.\033[m')
    if tipo == 'P':
        if total % 2 == 0:
            print('\033[1;34mVOCÊ VENCEU!\033[m')
            v += 1
        else:
            print('\033[1;31mVOCÊ PERDEU!\033[m')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('\033[1;34mVOCÊ VENCEU!\033[m')
            v += 1
        else:
            print('\033[1;31mVOCÊ PERDEU!\033[m')
            break
        print('Vamos jogar novamente...')
print('-' * 10)
print('\033[1;35;40mGAME OVER\033[m')
print(f'Você venceu {v} vezes.')
if v == 0:
    print('BOA SORTE NA PRÓXIMA...')
    pygame.mixer.init()
    pygame.init()
    pygame.mixer.music.load('derrota.mp3')
    pygame.mixer.music.play()
    input()
    pygame.event.wait()


