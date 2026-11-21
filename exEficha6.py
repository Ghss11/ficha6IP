ordem_pecas = ['torre', 'cavalo', 'bispo', 'dama', 'rei', 'bispo', 'cavalo', 'torre']

arbetura = {
    'a Defesa Siciliana': [('N', (6, 4), (4, 4)), ('C', (1, 2), (3, 2))],
    'a Defesa Escandinava': [('N', (6, 4), (4, 4)), ('C', (1, 3), (3, 3))],
    'o Gambito da Rainha': [('N', (6, 3), (4, 3)), ('C', (1, 3), (3, 3)), ('N', (6, 2), (4, 2))],
}


def caminho_livre(origem, destino, brancas, pretas):
    dl = destino[0] - origem[0]
    dc = destino[1] - origem[1]

    passo_l = 0
    if dl > 0:
        passo_l = 1
    if dl < 0:
        passo_l = -1

    passo_c = 0
    if dc > 0:
        passo_c = 1
    if dc < 0:
        passo_c = -1

    passos = abs(dl)
    if dl == 0:
        passos = abs(dc)

    for i in range(1, passos):
        casa = (origem[0] + i * passo_l, origem[1] + i * passo_c)
        if brancas.get(casa, '') != '' or pretas.get(casa, '') != '':
            return False
    return True


def movimento_valido(jogador, origem, destino, brancas, pretas):
    if jogador == 'N':
        minhas = brancas
        adversarias = pretas
        frente = -1
        linha_inicial = 6
    else:
        minhas = pretas
        adversarias = brancas
        frente = 1
        linha_inicial = 1

    for v in [origem[0], origem[1], destino[0], destino[1]]:
        if v < 0 or v > 7:
            return False
    if origem == destino:
        return False

    peca = minhas.get(origem, '')
    if peca == '' or minhas.get(destino, '') != '':
        return False

    dl = destino[0] - origem[0]
    dc = destino[1] - origem[1]
    reto = dl == 0 or dc == 0
    diagonal = abs(dl) == abs(dc)
    destino_vazio = brancas.get(destino, '') == '' and pretas.get(destino, '') == ''

    if peca == 'torre':
        return reto and caminho_livre(origem, destino, brancas, pretas)
    if peca == 'bispo':
        return diagonal and caminho_livre(origem, destino, brancas, pretas)
    if peca == 'dama':
        return (reto or diagonal) and caminho_livre(origem, destino, brancas, pretas)
    if peca == 'cavalo':
        return (abs(dl), abs(dc)) in [(1, 2), (2, 1)]
    if peca == 'rei':
        return abs(dl) <= 1 and abs(dc) <= 1
    if peca == 'peao':
        if dc == 0 and dl == frente:
            return destino_vazio
        if dc == 0 and dl == 2 * frente and origem[0] == linha_inicial:
            meio = (origem[0] + frente, origem[1])
            return brancas.get(meio, '') == '' and pretas.get(meio, '') == '' and destino_vazio
        if abs(dc) == 1 and dl == frente:
            return adversarias.get(destino, '') != ''
    return False


def turno(vez, nome, brancas, pretas, historico, validas):
    # lê a jogada
    texto = input().replace('(', '').replace(')', '').replace(',', '')
    partes = texto.split()
    jogador = partes[0]
    origem = (int(partes[1]), int(partes[2]))
    destino = (int(partes[3]), int(partes[4]))

    if jogador == 'N':
        nome_jogador = 'Papai Noel'
        minhas = brancas
        adversarias = pretas
        outro = 'C'
    else:
        nome_jogador = nome
        minhas = pretas
        adversarias = brancas
        outro = 'N'

    coordenadas = f'{origem[0]} {origem[1]} -> {destino[0]} {destino[1]}'

    # insistência
    if jogador != vez:
        historico.append(f'{nome_jogador}: {coordenadas} [FORA DA VEZ]')
        print(f'{nome_jogador} insistiu em jogar fora da vez! A partida foi encerrada.')
        return outro

    if not movimento_valido(jogador, origem, destino, brancas, pretas):
        historico.append(f'{nome_jogador}: {coordenadas} [ERRADA]')
        print('Jogada errada, perdeu a vez!')
    else:
        historico.append(f'{nome_jogador}: {coordenadas} [VÁLIDA]')

        capturada = adversarias.get(destino, '')
        if capturada != '':
            del adversarias[destino]
        peca = minhas[origem]
        del minhas[origem]
        minhas[destino] = peca

        validas.append((jogador, origem, destino))
        for abertura, sequencia in arbetura.items():
            if validas == sequencia:
                print(f'Muito bem, {nome_jogador} utilizou {abertura}!')

        # rei capturado
        if capturada == 'rei':
            print(f'O rei foi capturado! {nome_jogador} venceu a partida!')
            return jogador

    return turno(outro, nome, brancas, pretas, historico, validas)

nome = input()

print('Ho ho ho! Quem ousa desafiar o Papai Noel numa partida de xadrez de Natal?')
if nome == 'Beth Harmon':
    print('Nossa, temos um gênio aqui')
elif nome == 'Magnus Carlsen':
    print('Essa vai ser difícil! O menino é um prodígio!')
print('Que a partida comece! O Papai Noel joga com as peças brancas.')

brancas = {}   # Papai Noel linha 6 e 7
pretas = {}    # criança linha 0 e 1
for coluna in range(8):
    brancas[(7, coluna)] = ordem_pecas[coluna]
    brancas[(6, coluna)] = 'peao'
    pretas[(0, coluna)] = ordem_pecas[coluna]
    pretas[(1, coluna)] = 'peao'

historico = []
validas = []

vencedor = turno('N', nome, brancas, pretas, historico, validas)

print('Histórico da partida:')
numero = 1
for linha in historico:
    print(f'{numero}. {linha}')
    numero += 1

if vencedor == 'C':
    print(f'Parabéns, {nome}! Você venceu o Papai Noel e ganhou um presente!')
else:
    print(f'Ho ho ho! Você não foi uma criança boa durante o ano, {nome}, e por isso perdeu. Sem presente!')
