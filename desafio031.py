#Desenvolva um programa que pergunte a distância de uma viagem em Km.
#Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 para viagens mais longas.
viagem = float(input('Qual a distância da viagem em km? '))
passagem1 = viagem * 0.50
passagem2 = viagem * 0.45
if viagem <= 200:
    print('Você vai pagar \033[1mR${:.2f}\033[m pela viagem.'.format(passagem1))
else:
    print('Você vai pagar \033[1mR${:.2f}\033[m pela viagem.'.format(passagem2))