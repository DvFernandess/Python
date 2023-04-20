# Função para realizar a adição
def add(x, y):
    return x + y

# Função para realizar a subtração
def subtract(x, y):
    return x - y

# Função para realizar a multiplicação
def multiply(x, y):
    return x * y

# Função para realizar a divisão
def divide(x, y):
    return x / y

print("Selecione a operação.")
print("1.Adicionar")
print("2.Subtrair")
print("3.Multiplicar")
print("4.Dividir")

# Obter entrada do usuário
escolha = input("Digite a sua escolha (1/2/3/4): ")

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

if escolha == '1':
    print(num1,"+",num2,"=", add(num1,num2))

elif escolha == '2':
    print(num1,"-",num2,"=", subtract(num1,num2))

elif escolha == '3':
    print(num1,"*",num2,"=", multiply(num1,num2))

elif escolha == '4':
    print(num1,"/",num2,"=", divide(num1,num2))
else:
    print("Opção inválida!")