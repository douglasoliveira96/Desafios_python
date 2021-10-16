'''Faça um programa que leia uma frase pelo teclado e
mostre quantas vezes aparece a letra “A”,
em que posição ela aparece a primeira vez e
em que posição ela aparece a última vez.'''
frase = str(input('Digite uma frase: ').strip().upper())
c = frase.count('A')
p = (frase.find('A'))+1
u = (frase.rfind('A'))+1
print(frase)
print('A letra "A" aparece {} vezes,\nna primeira vez ela aparece na posição {}\ne na última vez ela aparece na posição {}.'.format(c, p, u))
