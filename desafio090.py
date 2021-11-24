'''Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. 
No final, mostre o conteúdo da estrutura na tela.'''

aluno = {}
aluno['nome'] = str(input('Nome: ')).strip().capitalize()
aluno['média'] = float(input(f'Média do aluno {aluno["nome"]}: '))

if aluno['média'] <= 4.5:
    print(f'O aluno {aluno["nome"]} está REPROVADO.')
elif aluno['média'] > 4.5 and aluno['média'] < 6.5:
    print(f'O aluno {aluno["nome"]} está de RECUPERAÇÃO.')
else: 
    print(f'O aluno {aluno["nome"]} está APROVADO.')
