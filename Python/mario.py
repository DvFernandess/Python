from cs50 import get_int
n = 0
while n < 1 or n > 8:
    n = get_int("Digite um número: ")
    if (n < 1 or n > 8):
        print("Inválido! Digite um número entre 1 e 8")
    for i in range(n):
        print(" " * (n - i - 1), end="")
        print("#" * (i + 1))