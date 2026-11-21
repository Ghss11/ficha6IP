n = int(input())
def calcular_cristal(n, nivel_atual=0, fator_brilho=1.0, energia_acumulada=1.0):
    if nivel_atual == n:
        return fator_brilho, energia_acumulada

    proximo_brilho = 1 / (2 + fator_brilho)
    proxima_energia = energia_acumulada + proximo_brilho

    return calcular_cristal(n, nivel_atual + 1, proximo_brilho, proxima_energia)

print('SISTEMA DE CALIBRAGEM DA ÁRVORE QUÂNTICA DE NATAL\nOficina Central do Papai Noel - Setor de Engenharia Fractal v1.0')

print()

print('[INFO] Carregando protocolos de recursão dos duendes...\n[INFO] Conectando ao gerador de auroras boreais...')

print()

print(f'[PROCESSANDO] Calculando as camadas fractais para o nível {n}...')
print('[AGUARDE] Desdobrando a pilha de recursão no núcleo do cristal...')

print()

fator_brilho, energia_acumulada = calcular_cristal(n)
print('[RELATÓRIO DE ENERGIA ACUMULADA]')
print(f'A soma dos índices de energia do nível 0 até o nível {n} é {energia_acumulada:.4f}.')

print()

if n == 0:
    print("[AVISO DO DUENDE CHEFE]: Você acessou o Núcleo Primordial (Nível 0)!")
    print(f"Este cristal não possui camadas externas, mas sua pureza de {fator_brilho:.4f} é máxima.\n")
elif fator_brilho < 0.35:
    print(f"[STATUS DO CRISTAL]: Fator de Brilho = {fator_brilho:.4f}")
    print("Resultado: Brilho Fraco! O cristal está absorvendo pouca energia.")
    print("Dica do Papai Noel: Tente aumentar o nível da árvore para iluminar o Polo Norte!\n")
elif fator_brilho > 0.42:
    print(f"[STATUS DO CRISTAL]: Fator de Brilho = {fator_brilho:.4f}")
    print("Resultado: SUPERCARGA ENERGÉTICA DETECTADA!")
    print("Cuidado! O cristal está gerando tanto brilho que pode fazer o trenó voar mais rápido do que o permitido!\n")
else:
    print(f"[STATUS DO CRISTAL]: Fator de Brilho = {fator_brilho:.4f}")
    print("Resultado: RESSONÂNCIA PERFEITA!")
    print("Atenção, duendes! Este cristal está pronto para ir direto para o topo de nossa Árvore de Natal!\n")

print("Calibração encerrada com sucesso!")
print("Que o seu código compile na primeira tentativa. Feliz Natal!")
