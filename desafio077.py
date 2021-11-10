'''Crie um programa que tenha várias palavras (não usar acentos).
Depois disso, você deve mostrar cada palavra, quais são as suas vogais.'''

palavras = ('Aprender', 'Programar', 'Linguagem', 'Python', 'Curso', 'Mercado', 'Trabalhar', 'Futuro')

for p in palavras:
    print(f'\nNa palavra {p.upper()} temos: ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end = ' ')