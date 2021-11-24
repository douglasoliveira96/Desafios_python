'''Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) 
em um dicionário. Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. 
Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.'''

from datetime import date
dados = dict()
dados['nome'] = str(input('Nome: ')).strip().capitalize()
nascimento = int(input('Ano de nascimento: '))
dados['ctps'] = int(input('N° carteira de trabalho: '))

if dados['ctps'] != 0:
    dados['contratação'] = int(input('Ano de contratação: '))
    dados['salario'] = float(input('Salário: '))
    dados['aposentadoria'] = dados['contratação'] + 35
if dados['ctps'] == 0:
    print('Você não trabalha formalmente.')

ano_atual = date.today().year
dados['idade'] = ano_atual - nascimento
dados['idade_aposentadoria'] = dados['aposentadoria'] - nascimento
print('='*30)
for k, v in dados.items():
    print(f'  -  {k} tem o valor {v}.')
print('='*30)
