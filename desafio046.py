#Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício,
#indo de 10 até 0, com uma pausa de 1 segundo entre eles.
from time import sleep
for c in range(10, -1, -1):
    print(c)
    sleep(1)
print('''\033[1;37m🍾🍾🍾\033[m
\033[1;33;40mPIIIIIIIIUUUUU 🚀🚀🚀\033[m
\033[1;31;40mPARARARAPAPAPAPA ✨✨✨✨✨✨\033[m
\033[1;37;40mPOOOOOOWWW 🎆🎆🎆🎆🎆🎆\033[m
\033[1;31;40m🎉🎉🎉🎉🎉🎉🎉\033[m''')
