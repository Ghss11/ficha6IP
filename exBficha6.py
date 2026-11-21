quantidade_setores = int(input())
minimo_possibilidades = int(input())

lista = []

aprovados = 0

def combinação(n,k):
    if k == 1:
        return n
    if k == 0 or k == n:
        return 1

    inclui = combinação(n-1, k-1)
    nao_inclui = combinação(n-1, k)

    return inclui + nao_inclui

for i in range(quantidade_setores):

    n = int(input())
    k = int(input())

    n_possibilidades = combinação(n,k)
    lista.append(n_possibilidades)

print('Relatório dos escudos de Norte:')

i = 1
for k in lista:
    if k >= minimo_possibilidades:
        print(f'Setor {i}: {lista[i-1]} possibilidade(s). Variedade suficiente!')
        aprovados += 1
    else:
        print(f'Setor {i}: {lista[i-1]} possibilidade(s). Precisa de mais alternativas!')
    i += 1

print(f'Setores que atingiram a meta: {aprovados} de {quantidade_setores}.')
if aprovados == quantidade_setores:
    print('Tudo pronto! O planejamento dos escudos foi aprovado!')
else:
    print('Norte precisa revisar o planejamento!')
