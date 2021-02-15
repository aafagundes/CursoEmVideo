#dicionario
#Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas
# partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em
# um dicionário, incluindo o total de gols feitos durante o campeonato.

jogador=dict()
partidas=list()
jogador["nome"]=str(input('nome do jogador:'))
total=int(input("quantas partidas jogou?"))
for c in range(0,total):
    partidas.append(int(input(f'quantos gols fez na partida numero {c+1}?')))
print(jogador)
print(partidas)
jogador['gols']=partidas[:]
jogador['total']=sum(partidas)
print('-='*30)
print(jogador)
print('-='*30)
for c,v in jogador.items():
    print(f'o campo {c} tem o valor {v}')
print('-='*30)

print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas.')
for i,v in enumerate(jogador["gols"]):
    print(f'Na partida numero {i+1}, fez {v} gols.')
print(f'O total de gols feitos foi de: {jogador["total"]}.')