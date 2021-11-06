'''Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro
de Futebol, na ordem de colocação.
Depois mostre:
a) Os 5 primeiros times.
b) Os últimos 4 colocados.
c) Times em ordem alfabética.
d) Em que posição está o time da Chapecoense.'''

times = ('Atletico-MG', 'Flamengo', 'Palmeiras', 'Bragantino', 'Fortaleza',
         'Corinthians', 'Internacional', 'Fluminense', 'Cuiabá',
         'América-MG', 'Atlético-GO', 'São Paulo', 'Ceará SC',
         'Athletico-PR', 'Santos', 'Bahia', 'Sport Recife', 'Juventude',
         'Grêmio', 'Chapecoense')

print('-=' * 142)
print('\033[1;33;40m{:^80}\033[m'.format('CAMPEONATO BRASILEIRO 2021'))
print('-=' * 142)
print('\033[1m{}\033[m'.format(times))
print('-=' * 142)
print(f'\033[34mOs 5 primeiros times são: {times[0:5]}\033[m')
print('-=' * 142)
print(f'\033[31mOs 4 últimos times são: {times[-4:]}\033[m')
print('-=' * 142)
print(f'\033[1mOs times em ordem alfabética: {sorted(times)}\033[m')
print('-=' * 142)
print(f'\033[32mA Chapecoense está na {times.index("Chapecoense")+1}° posição.')
