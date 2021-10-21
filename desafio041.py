#A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento
#de um atleta e mostre sua categoria, de acordo com a idade:
#– Até 9 anos: MIRIM
#– Até 14 anos: INFANTIL
#– Até 19 anos: JÚNIOR
#– Até 25 anos: SÊNIOR
#– Acima de 25 anos: MASTER
from datetime import date
ano = int(input('Qual é o ano de nascimento do atleta? '))
idade = date.today().year - ano
print('{} anos'.format(idade))
if idade <= 9:
    print('O atleta está na categoria \033[1;mMIRIM\033[m')
elif idade <= 14:
    print('O atleta está na categoria \033[1;mINFANTIL\033[m')
elif idade <= 19:
    print('O atleta está na categoria \033[1;mJÚNIOR\033[m')
elif idade <= 25:
    print('O atleta está na categoria \033[1;mSÊNIOR\033[m')
elif idade > 25:
    print('O atleta está na categoria \033[1;mMASTER\033[m')


