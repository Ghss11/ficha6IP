print('🎄 Alerta na Vila dos Quem! O Grinch sumiu com os presentes! Vamos investigar as pistas!')
pista = input().lower()

def palindromo(texto):
    if len(texto) <= 1:
        return True
    if texto[0] == texto[-1]:
        return palindromo(texto[1:-1])
    return False

pista_investigada = []
pista_valida = []
pontos = 0

while pista != 'fim':
    print('🔎 Qual será a próxima pista?')

    if pista in pista_investigada:
        print('🚫 Pistas repetidas não vão nos ajudar em nada!')
    else:
        pista_investigada.append(pista)

        if palindromo(pista):
            print(f"✅ Parece que a pista '{pista.upper()}' é um palíndromo!")

            if pista == 'osso':
                print('🐶 O osso do Max! O Grinch esteve por aqui! (+3 pontos)')
                pontos += 3
                pista_valida.append(pista)
            elif pista == 'radar':
                print('🛷 O radar do trenó! Estamos na trilha certa! (+5 pontos)')
                pontos += 5
                pista_valida.append(pista)
            elif pista == 'reviver':
                print('💚 Reviver o Natal... será que o Grinch está se arrependendo? (+10 pontos)')
                pontos += 10
                pista_valida.append(pista)
            elif pista == 'arara':
                print('🦜 Era uma arara de brinquedo! O Grinch plantou uma pista falsa! (-4 pontos)')
                pontos -= 4
            elif pista == 'sos':
                print('📻 Era um pedido de socorro falso! O Grinch está nos desviando do caminho! (-2 pontos)')
                pontos -= 2
            else:
                pontos += 1
                pista_valida.append(pista)
        else:
            print(f"❌ Poxa! Parece que a pista '{pista.upper()}' não nos ajudou muito...")

    pista = input().lower()

print('📁 Parece que a investigação terminou!')

qte_pistas = len(pista_investigada)
qte_palindromos = len(pista_valida)

if qte_pistas == 0 or qte_palindromos == 0:
    porcentagem = 0.0
else:
    porcentagem = round(qte_palindromos / qte_pistas * 100, 1)

print()
print('Vamos à Análise Final! 📋')
print()
print(f'Pistas investigadas: {qte_pistas}')
print(f'Palíndromos encontrados: {qte_palindromos}')
print(f'Aproveitamento: {porcentagem:.1f}%')
print(f'Pontos de Evidência: {pontos}')
print()

if qte_pistas == 0:
    print('Sem pistas, sem caso! O Grinch está rindo lá do Monte Crumpit... 😈')
elif qte_palindromos == 0:
    print('Nenhuma pista válida! O Grinch fugiu levando até o último enfeite! 💨')
elif 'osso' in pista_investigada and 'radar' in pista_investigada and 'reviver' in pista_investigada:
    print('Caso encerrado! O coração do Grinch cresceu três tamanhos e ele devolveu os presentes! 🎅💚')
elif porcentagem >= 75:
    print('Estamos quase lá! O Grinch já está ouvindo os cantos de Natal da Vila! 🎶')
elif porcentagem >= 50:
    print('A trilha está esquentando! Mais um pouco e pegamos o Grinch! 🔎')
else:
    print('Poucas pistas válidas... O Grinch está fazendo piada lá do Monte Crumpit. 🏔️')
