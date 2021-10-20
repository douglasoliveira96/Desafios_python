#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
#Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
#A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.
valor = float(input('Qual é o valor da casa? R$'))
salário = float(input('Quanto é o seu salário? R$'))
parcelas = int(input('Quantos anos de financiamento? '))
prestação = valor / parcelas
pm = prestação / 12
porcentagem = salário * (30 / 100)
print('Para pagar uma casa no valor de R${:.2f} durante {} anos a prestação será de R${:.2f} por mês.'.format(valor, parcelas, pm))
if pm > porcentagem:
    print('\033[31mEMPRÉSTIMO NEGADO!\033[m')
else:
    print('\033[34mEMPRÉSTIMO CONCEDIDO!\033[m')
