'''Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados
de cada pessoa em um dicionário e todos os dicionários em uma lista. 
No final, mostre: 
A) Quantas pessoas foram cadastradas 
B) A média de idade 
C) Uma lista com as mulheres 
D) Uma lista de pessoas com idade acima da média'''

pessoa = dict()
galera = list()
mulher = list()
soma = idade = 0
tot = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome? ')).capitalize()
    while True:
        pessoa['sexo'] = str(input('Sexo [M ou F]? ')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('\033[31mERRO! Digite M ou F.\033[m')
    pessoa['idade'] = int(input('Idade? '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        resp = str(input('Deseja continuar [S ou N]? ')).upper()[0]
        if resp in 'SN':
            break
        print('\033[31mERRO! Digite S ou N.\033[m')
    print()
    tot += 1
    if resp in 'N':
        break
print(f'A) Um total de {tot} pessoas cadastradas.')
#print(galera)
média = soma / len(galera)
print(f'B) A média de idade é de {média:.2f} anos.')
print('C) As mulheres cadastradas foram: ')
for p in galera:
    if p['sexo'] in 'Ff':
        print(f'{p["nome"]}', end=' ')
print()
print('D) Lista das pessoas que estão acima da média de idade: ')
print()
for p in galera:
    if p['idade'] >= média:
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()
print('<<< ENCERRADO >>>') 


