#Faça um programa que leia a largura e a altura de uma parede em metros, calcule sua área e a quantidade de tinta necessária para pintá-la,
#sabendo que cada litro de tinta, pinta uma área de 2m quadrados.
m = float(input('Qual é a altura da parede em metros? '))
c = float(input('Qual é o comprimento da parede em metros? '))
a = m * c
l = a/2
print('A área da parede mede: {:.2f} '.format(a))
print('Serão necessário {:.2f} litros de tinta para pintar essa parede.'.format(l))
