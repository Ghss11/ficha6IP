print('🎄 O Natal chegou na Cozinha! Vamos preparar um Biscoito digno do Papai Noel!')
def determinante(matriz):
    if len(matriz) == 1:
        return matriz[0][0]

    total = 0
    sinal = 1
    for coluna in range(len(matriz)):
        menor = []
        for linha in matriz[1:]:
            menor.append(linha[:coluna] + linha[coluna + 1:])
        total += matriz[0][coluna] * sinal * determinante(menor)
        sinal = -sinal
    return total



dimensoes = input().split()
linhas = int(dimensoes[0])
colunas = int(dimensoes[1])
while linhas != colunas or linhas <= 0:
    print('Esse Biscoito não cabe na Receita! Precisamos de um Quadrado com dimensões positivas!')
    dimensoes = input().split()
    linhas = int(dimensoes[0])
    colunas = int(dimensoes[1])

print('🍪 Hora de preparar a Massa! Qual a Gostosura de cada pedaço?')
biscoito = []
for i in range(linhas):
    valores = input().split()
    linha = []
    for v in valores:
        linha.append(int(v))
    biscoito.append(linha)

print('Vamos dar um toque de Magia! Onde colocaremos os Enfeites Natalinos?')
enfeites = {'E': 0, 'F': 0, 'P': 0, 'A': 0}
for i in range(linhas):
    simbolos = input().split()
    for j in range(colunas):
        enfeite = simbolos[j]
        if enfeite == 'E':
            biscoito[i][j] *= 2
        elif enfeite == 'F':
            biscoito[i][j] = -biscoito[i][j]
        elif enfeite == 'P':
            biscoito[i][j] += 5
        elif enfeite == 'A':
            biscoito[i][j] = biscoito[i][j] ** 2
        if enfeite != '.':
            enfeites[enfeite] += 1

gostosura = determinante(biscoito)
total_enfeites = enfeites['E'] + enfeites['F'] + enfeites['P'] + enfeites['A']

print('Vamos a Análise Final!')
print(f'\nGostosura: {gostosura}')

if gostosura < 0:
    print('Nem o Grinch teria Coragem de provar esse Biscoito!')
elif gostosura == 0:
    if total_enfeites == 0:
        print('A Magia do Biscoito se Anulou.')
    else:
        print('Tanta Decoração para nada! A Magia do Biscoito se Anulou.')
else:
    if enfeites['E'] > 0 and enfeites['F'] > 0 and enfeites['P'] > 0 and enfeites['A'] > 0:
        print('Um Pedaço de cada Encanto Natalino! Esse vai para o Papai Noel! 🎅')
    elif enfeites['F'] > enfeites['E'] + enfeites['P'] + enfeites['A']:
        print('Gostoso e Congelante! Sirva com uma Caneca de Chocolate Quente! ❄️')
    elif enfeites['A'] > 0 and enfeites['F'] == 0:
        print('Uma Floresta de gostosura! As Renas vão Adorar! 🎄')
    else:
        print('Receita Aprovada! Já pode colocar ao lado do Copo de Leite! 🥛')
