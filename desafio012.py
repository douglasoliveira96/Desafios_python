#Faça um algoritmo que leia o preço de um produto
#e mostre seu novo preço, com 5% de desconto.
p = float(input('Digite o valor do produto: R$'))
d = p*0.95
print('O preço do produto com 5% de desconto é R${:.2f}'.format(d))
