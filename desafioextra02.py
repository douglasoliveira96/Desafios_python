'''Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. 
Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 
8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
salário bruto.
quanto pagou ao INSS.
quanto pagou ao sindicato.
o salário líquido.
calcule os descontos e o salário líquido, conforme a tabela abaixo:'''

print('-=' * 20)
hora = float(input('Quanto você ganha por hora? R$'))
mes = float(input('Horas trabalhadas por mês? '))

salário = hora * mes
imposto = salário - (salário * (89/100))
inss = salário - (salário * (92/100))
sindicato = salário - (salário * (95/100))
líquido = salário - (imposto + inss + sindicato)


print()
print(f'Salário bruto: R${salário:.2f}')
print(f'Desconto do INSS: R${inss:.2f}')
print(f'Desconto do sindicato: R${sindicato:.2f}')
print(f'Salário líquido R${líquido:.2f}')
print('-=' * 20)
