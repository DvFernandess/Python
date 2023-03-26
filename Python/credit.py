import sys

# AMEX - começam com 34 ou 37 e usam números de 15 dígitos
# MASTERCARD - a maioria dos números começa com 51, 52, 53, 54 ou 55 e usa números de 16 dígitos
# VISA - todos os números começam com 4 e usa números de 13 e 16 dígitos


def main():
    n_cartao = input("Entre com o número do cartao de crédito: ")
    cartao = len(str(n_cartao))
    
    if cartao < 13 or 16 < cartao:
        print("INVALID")
        sys.exit()

    soma_digito = 0
    s = 0
    v_cartao = - (cartao + 1)
    
    for i in range(-2, v_cartao, -2):
        resto = int(n_cartao[i]) * 2
        if (resto >= 10):
            soma_digito = soma_digito + resto - 9
        else:
            soma_digito = soma_digito + resto

    for i in range(-1, v_cartao, -2):
        temp = int(n_cartao[i])
        s = s + temp

    s_total = soma_digito + s
   
    if s_total % 2 == 0:
        if int(n_cartao[0]) == 3 and int(n_cartao[1]) == 4 or int(n_cartao[1]) == 7:
            print("AMEX")

        elif int(n_cartao[0]) == 5 and int(n_cartao[1]) == 1 or int(n_cartao[1]) == 2 or int(n_cartao[1]) == 3 or int(n_cartao[1]) == 4 or int(n_cartao[1]) == 5:
            print("MASTERCARD")

        elif int(n_cartao[0]) == 4:
            print("VISA")
        else:
            print("INVALID")

if __name__ == "__main__":
    main()