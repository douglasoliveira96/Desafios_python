#Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
#No final do programa, mostre: a média de idade do grupo, qual é o
#nome do homem mais velho e quantas mulheres têm menos de 20 anos.
somaidade = 0
média = 0
maiorhomem = 0
nomevelho = ''
totmulher20 = 0
for c in range(1, 5):
    print('\033[1;35m-------- {}° PESSOA --------\033[m'.format(c))
    nome = str(input('Qual é o nome da {}° pessoa? '.format(c))).strip().title()
    idade = int(input('Quantos anos a {}° pessoa tem? '.format(c)))
    sexo = str(input('Qual é o sexo da {}° pessoa [M/F]? '.format(c))).strip().upper()
    somaidade += idade
    if c == 1 and sexo in 'M':
            maiorhomem = idade
            nomevelho = nome
    if sexo in 'M' and idade > maiorhomem:
            maiorhomem = idade
            nomevelho = nome
    if sexo in 'F' and idade < 20:
        totmulher20 += 1
média = somaidade / 4
print('\n\033[1;36;40mA média de idade do grupo é de {} anos.\033[m'.format(média))
print('\033[1;36;40mO {} é o homem mais velho e ele tem {} anos.\033[m'.format(nomevelho, maiorhomem))
print('\033[1;36;40mHá {} mulheres com menos de 20 anos.\033[m'.format(totmulher20))