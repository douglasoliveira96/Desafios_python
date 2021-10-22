#Desenvolva uma lógica que leia o peso e a altura de uma pessoa,
#calcule seu Índice de Massa Corporal (IMC)
#e mostre seu status, de acordo com a tabela abaixo:
#– IMC abaixo de 18,5: Abaixo do Peso
#– Entre 18,5 e 25: Peso Ideal
#– 25 até 30: Sobrepeso
#– 30 até 40: Obesidade
#– Acima de 40: Obesidade Mórbida
peso = float(input('Quanto você pesa? '))
alt = float(input('Qual é a sua altura? '))
imc = peso / (alt * alt)
print('Seu IMC é de {:.1f}.'.format(imc))
if imc <= 18.5:
    print('Você está \033[1;37mABAIXO DO PESO.\033[m')
elif imc <= 25:
    print('Você está com o \033[1;34mPESO IDEAL.\033[m')
elif imc <= 30:
    print('Você está com \033[1;33mSOBREPESO.\033[m')
elif imc <= 40:
    print('Você está com \033[1;31mOBESIDADE.\033[m')
else:
    print('Você está com \033[1;31mOBESIDADE MÓRBIDA.\033[m')
