#Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’.
#Caso esteja errado, peça a digitação novamente até ter um valor correto.
sexo = str(input('Qual é o seu sexo [M ou F]? ')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('\033[31mDados inválidos, digite o sexo novamente:\033[m ')).strip().upper()[0]
print('\033[1mSexo {} registrado com sucesso.\033[m'.format(sexo))
