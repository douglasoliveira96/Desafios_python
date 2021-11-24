'''Crie um programa que gerencie o aproveitamento de um jogador de futebol. 
O programa vai ler o nome do jogador e quantas partidas ele jogou. 
Depois vai ler a quantidade de gols feitos em cada partida. 
No final, tudo isso será guardado em um dicionário, 
incluindo o total de gols feitos durante o campeonato.'''

dados = dict()
partidas = list()
print()
dados['nome'] = str(input('Nome do jogador: ')).upper()
tot = int(input('Partidas jogadas: '))

for p in range(0, tot):
    partidas.append(int(input(f'Quantos gols o jogador {dados["nome"]} fez na partida {p}? ')))
dados['gols'] = partidas[:]
dados['total'] = sum(partidas)
print('=='*30)
print(dados)
print('=='*30)

for k, v in dados.items():
    print(f'    -  O campo {k} tem o valor {v}')
print('**'*30)
print(f'O jogador {dados["nome"]} jogou {len(dados["gols"])} partidas.')
for i, v in enumerate(dados['gols']):
    print(f'    => Na partida {i}, fez {v} gols.')
print(f'Foi um total de {dados["total"]} gols.')
print()
