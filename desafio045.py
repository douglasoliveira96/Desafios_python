#Crie um programa que faça o computador jogar Jokenpô com você.
from random import randint
from time import sleep
print('Suas opções:\n'
      '[ 1 ] PEDRA\n'
      '[ 2 ] PAPEL\n'
      '[ 3 ] TESOURA')
você = int(input('Pedra, papel ou tesoura, 1, 2 ou 3? '))
print('\033[1;36mJO\033[m')
sleep(1)
print('\033[1;36mKEN\033[m')
sleep(1)
print('\033[1;36mPÔ!!!\033[m')
computador = randint(1, 3)
#print('Vc escolheu {} e o pc escolheu {}'.format(você, computador))
if você == 1 and computador == 3:
      print('Você escolheu \033[1;34mPEDRA\033[m e o computador escolheu \033[1;34mTESOURA\033[m.')
      print('\033[1;34;40mVOCÊ VENCEU!\033[m')
if você == 3 and computador == 2:
      print('Você escolheu \033[1;34mTESOURA\033[m e o computador escolheu \033[1;34mPAPEL.\033[m')
      print('\033[1;34;40mVOCÊ VENCEU!\033[m')
if você == 2 and computador == 1:
      print('Você escolheu \033[1;34mPAPEL\033[m e o computador escolheu \033[1;34mPEDRA.\033[m')
      print('\033[1;34;40mVOCÊ VENCEU!\033[m')
elif você == 2 and computador == 3:
      print('Você escolheu \033[1;31mPAPEL\033[m e o computador escolheu \033[1;31mTESOURA.\033[m')
      print('\033[1;31;40mO COMPUTADOR VENCEU!\033[m')
elif você == 3 and computador == 1:
      print('Você escolheu \033[1;31mTESOURA\033[m e o computador escolheu \033[1;31mPEDRA.\033[m')
      print('\033[1;31;40mO COMPUTADOR VENCEU!\033[m')
elif você == 1 and computador == 2:
      print('Você escolheu \033[1;31mPEDRA\033[m e o computador escolheu \033[1;31mPAPEL.\033[m')
      print('\033[1;31;40mO COMPUTADOR VENCEU!\033[m')
elif você == computador:
      print('\033[1;35;40mEMPATE!\033[m')
elif você > 3:
      print('\033[1;37mJOGADA INVÁLIDA\033[m')
