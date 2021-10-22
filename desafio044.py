#Elabore um programa que calcule o valor a ser pago por um produto,
#considerando o seu preço normal e condição de pagamento:
#– à vista dinheiro/cheque: 10% de desconto
#– à vista no cartão: 5% de desconto
#– em até 2x no cartão: preço formal
#– 3x ou mais no cartão: 20% de juros
valor = float(input('Qual é o valor do produto? '))
formas = int(input('Formas de pagamento:\n'
                   '[ 1 ] à vista dinheiro/cheque\n'
                   '[ 2 ] à vista cartão\n'
                   '[ 3 ] 2x no cartão\n'
                   '[ 4 ] 3x ou mais no cartão\n'))
if formas == 1:
    print('Se for pagar à vista no dinheiro ou no cheque o valor será de R${:.2f}'.format(valor * (90 / 100)))
    print('Você teve 10% de desconto')
if formas == 2:
    print('O valor à vista no cartão é de R${:.2f}'.format(valor * (95 / 100)))
    print('Você teve 5% de desconto.')
if formas == 3:
        print('O valor do produto parcelado duas vezes no cartão é de duas parcelas de R${:.2f}'.format((valor / 2)))
        print('R${:.2f} ao todo.'.format(valor))
if formas == 4:
        print('Se for parcelar em 3 vezes no cartão o produto sai a 3 parcelas de R${:.2f}.'.format(((120/100 * valor) / 3)))
        print('R${:.2f} ao todo.'.format(120 / 100 * valor))
        print('Por ter parcelado em 3 vezes você teve um acréscimo de 20% de juros.')
