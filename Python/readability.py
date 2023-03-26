from cs50 import get_string

s = get_string("Digite o texto: ")

qtd_frases = 0
qtd_letras = 0
qtd_palavras = 1

for i in range(len(s)):
    if s[i].isalpha():
        qtd_letras += 1
    elif s[i].isspace():
        qtd_palavras += 1
    elif s[i] == '.' or s[i] == '!' or s[i] == '?':
        qtd_frases += 1

L = qtd_letras * 100 / qtd_palavras
S = qtd_frases * 100 / qtd_palavras

indice = 0.0588 * L - 0.296 * S - 15.8
indice = round(indice)

if indice > 16:
    print("Grade 16+")
elif indice > 1 and indice < 17:
    print(f"Grade {indice}")
else:
    print("Before Grade 1")