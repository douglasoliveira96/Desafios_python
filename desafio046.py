#FaΓ§a um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifΓ­cio,
#indo de 10 atΓ© 0, com uma pausa de 1 segundo entre eles.
from time import sleep
for c in range(10, -1, -1):
    print(c)
    sleep(1)
print('''\033[1;37mπΎπΎπΎ\033[m
\033[1;33;40mPIIIIIIIIUUUUU πππ\033[m
\033[1;31;40mPARARARAPAPAPAPA β¨β¨β¨β¨β¨β¨\033[m
\033[1;37;40mPOOOOOOWWW ππππππ\033[m
\033[1;31;40mπππππππ\033[m''')
