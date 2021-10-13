#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado
#e a quantidade de dias pelos quais ele foi alugado.
# Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
km = float(input('Digite a quantidade de KM percorridos: '))
d = int(input('Digite por quantos dias o carro foi alugado: '))
preco = (d * 60) + (km * 0.15)
print('O valor a pagar pelo carro nesses {} dias alugados é R${:.2f}.'.format(d, preco))
