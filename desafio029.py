#Escreva um programa que leia a velocidade de um carro.
#Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
#A multa vai custar R$7,00 por cada Km acima do limite.
vel = float(input('Qual era a velocidade do carro? '))
multa = (vel - 80) * 7
if vel > 80:
    print('\033[4mO veículo atingiu a velocidade máxima permitida, você está multado!\033[m')
    print('\033[1mA sua multa é de\033[m \033[31mR${:.2f}\033[m.'.format(multa))
else:
    print('\033[1mTenha uma boa viagem!')
