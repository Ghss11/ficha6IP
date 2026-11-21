valor_duendes = int(input())
valor_elfos = int(input())
def fatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fatorial(n - 1)

fatorial_duende = fatorial(valor_duendes)
fatorial_elfos = fatorial(valor_elfos)
if fatorial_duende > fatorial_elfos:
    print('Os duendes se superaram dessa vez.')
elif fatorial_duende < fatorial_elfos:
    print('É, os elfos tiveram um resultado melhor.')
else:
    print('Ué, houve um empate.')

def mdc(a, b):
    if b == 0:
        return a
    else:
        return mdc(b, a % b)

resultado_mdc = mdc(fatorial_duende, fatorial_elfos)

if resultado_mdc > 10:
    print('Caixas gigantes! O Papai Noel vai precisar de um guindaste para empacotar tudo.')
else:
    print('Caixas compactas e organizadas perfeitamente.')

divisão_estabilidade = ((fatorial_duende + fatorial_elfos) // 2) + resultado_mdc

if divisão_estabilidade > 50:
    print('Atenção: O divisor de estabilidade está altíssimo!')
else:
    print('Divisor calculado com sucesso. A rampa está equilibrada.')

print('Calculando a inclinação geométrica do canhão...')
def potencia_recursiva(base, expoente):
    if expoente == 0:
        return 1
    else:
        return base * potencia_recursiva(base, expoente - 1)


def soma_cateto(cateto1, cateto2):

    q_cateto1 = potencia_recursiva(cateto1, 2)
    q_cateto2 = potencia_recursiva(cateto2, 2)

    return q_cateto1 + q_cateto2

hipotenusa_geometrica = soma_cateto(fatorial_duende, fatorial_elfos)

if hipotenusa_geometrica % divisão_estabilidade != 0:
    print('Lançamento autorizado!')
else:
    print('Lançamento não autorizado!')
