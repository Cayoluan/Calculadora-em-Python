def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b != 0:
        return a / b
    else:
        return "Não é possível dividir por zero."

while True:
    print("Escolha a operação desejada:")
    print("1. Adição")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("5. Sair")

    numPrincipal = input("Digite o número da operação desejada: ")

    if numPrincipal == '5':
        print("Encerrando programa...")
        break

    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    if numPrincipal == '1':
        print(num1, "+", num2, "=", soma(num1, num2))
    elif numPrincipal == '2':
        print(num1, "-", num2, "=", subtracao(num1, num2))
    elif numPrincipal == '3':
        print(num1, "*", num2, "=", multiplicacao(num1, num2))
    elif numPrincipal == '4':
        resultado = divisao(num1, num2)
        print(num1, "/", num2, "=", resultado)
    else:
        print("Opção inválida. Por favor, selecione uma opção válida entre 1 a 4.")
