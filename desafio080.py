'''Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.'''

lista = []
for num in range(0, 5):
    n = int(input('Digite um número: '))
    if num == 0 or num > lista[-1]:
        lista.append(n)
    else:
        pos = 0 
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                break
            pos += 1
print('=' * 54)
print(f'Os valores digitados em ordem foram {lista}.')
print('=' * 54)
