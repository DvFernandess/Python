from cs50 import get_float

while True:
    n = get_float("Qual o valor do troco: ")
    if n < 0:
        print("Troco Inválido")
        n = get_float("Qual o valor do troco: ")
    if n > 0:
        centavos = round(n * 100)
        i = 0

    while centavos >= 25:
        centavos = centavos - 25
        i += 1
    print(f"Qtd de moedas de 25: {i}")
    j = 0
    while centavos >= 10:
        centavos = centavos - 10
        j += 1
    print(f"Qtd de moedas de 10: {j}")
    k = 0
    while centavos >= 5:
        centavos = centavos - 5
        k += 1
    print(f"Qtd de moedas de 5: {k}")
    l = 0
    while centavos >= 1:
        centavos = centavos - 1
        l += 1
    print(f"Qtd de moedas de 1: {l}")
    
    total = i + j + k + l
    print(f"Qtd de moedas total: {total}")
    break