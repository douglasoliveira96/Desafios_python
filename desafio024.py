#Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”.
city = str(input('Digite o nome de uma cidade: ')).strip()
print((city[0:5].upper()) == 'SANTO')

