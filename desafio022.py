'''Crie um programa que leia o nome completo de uma pessoa e mostre:
– O nome com todas as letras maiúsculas e minúsculas.
– Quantas letras ao todo (sem considerar espaços).
– Quantas letras tem o primeiro nome.'''

nome = str(input('Digite um nome completo: ')).strip()
print('Nome digitado em letras maiúculas: {}.'.format(nome.upper()))
print('Nome digitado em letras minúsculas: {}.'.format(nome.lower()))
print('O nome digitado tem {} letras.'.format(len(nome) - nome.count(' ')))
#print('Seu primeiro nome tem {} letras.'.format(nome.find(' ')))
separa = nome.split()
print('Seu primeiro nome é "{}" e ele tem {} letras.'.format(separa[0], len(separa[0])))














