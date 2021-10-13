#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira
#e mostre quantos dólares, euro e bitcoin ela pode comprar
#(considerando as cotações do dia 13/10/2021).
real = float(input('Digite quanto de dinheiro você tem na carteira: R$ '))
dolar = real/5.53
euro = real/6.40
bitcoin = real/305047.81
print('Com R${:.2f} você consegue comprar US${:.2f} ou €{:.2f} ou BTC {:.6f}.'.format(real, dolar, euro, bitcoin))
