'''Média de gols de um jogador'''

dados = list()
nome = str(input('Nome: ')).strip().upper()
partidas = int(input('N° de partidas: '))

for g in range(0, partidas):
    dados.append(int(input(f'Quantos gols o jogador {nome} fez na partida {g}? ')))

media = (sum(dados)) / partidas
print(f'\nO jogador {nome} jogou {partidas} partidas e fez {sum(dados)} gols.')
print(f'Uma média de {media} gols por jogo.')
