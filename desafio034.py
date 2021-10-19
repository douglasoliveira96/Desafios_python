#Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
#Para salários superiores a R$1250,00, calcule um aumento de 10%.
#Para os inferiores ou iguais, o aumento é de 15%.
funcionario = str(input('Qual é o nome do funcionário? ')).strip().title()
sal = float(input('Qual é o salário do funcionário? '))
aumento1 = sal * (10 / 100)
aumento2 = sal * (15 / 100)
atual1 = sal + aumento1
atual2 = sal + aumento2
if sal > 1250.00:
    print('O funcionário \033[1m{}\033[m recebeu um aumento de \033[1;32mR${:.2f}.\033[m'.format(funcionario, aumento1))
    print('Seu salário atual é de \033[1;32mR${:.2f}.\033[m'.format(atual1))
if sal <= 1250.00:
    print('O funcionário \033[1m{}\033[m recebeu um aumento de \033[1;32mR${:.2f}.\033[m'.format(funcionario, aumento2))
    print('Seu salário atual é de \033[1;32mR${:.2f}.'.format(atual2))
