'''Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.'''

def área(larg, comp):
    a = larg * comp
    print(f'A área de um terreno {larg} x {comp} é igual a {a}m².')


l = float(input('Largura do terreno (m): '))
c = float(input('Comprimento do terreno (m): '))
área(l, c)

