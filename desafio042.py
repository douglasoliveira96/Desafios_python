#Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso
#de mostrar que tipo de triângulo será formado:
#– EQUILÁTERO: todos os lados iguais
#– ISÓSCELES: dois lados iguais, um diferente
#– ESCALENO: todos os lados diferentes
r1 = float(input('Digite o segmento da reta 1: '))
r2 = float(input('Digite o segmento da reta 2: '))
r3 = float(input('Digite o segmento da reta 3: '))
if (r1 + r2) > r3 and (r2 + r3) > r1 and (r3 + r1) > r2:
    print('\033[1;34mForma um triângulo\033[m')
    if r1 == r2 == r3:
        print('\033[1;36mEQUILÁTERO\033[m')
    if r1 == r2 != r3 or r3 == r1 !=r2:
        print('\033[1;36mISÓSCELES\033[m')
    elif r1 != r2 != r3 != r1:
        print('\033[1;36mESCALENO\033[m')
else:
    print('\033[1;31mNão forma um triângulo!\033[m')
