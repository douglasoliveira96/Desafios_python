#Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
#– Média abaixo de 5.0: REPROVADO
#– Média entre 5.0 e 6.9: RECUPERAÇÃO
#– Média 7.0 ou superior: APROVADO
nota1 = float(input('Digite a nota do aluno no primeiro bimestre: '))
nota2 = float(input('Digite a nota do aluno no segundo bimestre: '))
média = (nota1 + nota2) / 2
print('\033[1mMédia {}\033[m'.format(média))
if média < 5.0:
    print('O aluno está \033[1;31mREPROVADO!\033[m')
elif média == 5.0 or média <= 6.9:
    print('O aluno está de \033[1;33mRECUPERAÇÃO!\033[m')
elif média >= 7.0:
    print('O aluno está \033[1;32mAPROVADO!\033[m')
    print('\033[1;35mP\033[m\033[1;34mA\033[m\033[1;31mR\033[m\033[1;32mA\033[m\033[1;33mB\033[m\033[1;35mÉ\033[m\033[1;34mN\033[m\033[1;37mS!\033[m')
