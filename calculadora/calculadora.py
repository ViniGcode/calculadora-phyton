def adicionar(x, y):
    return x + y

def subtrair(x, y):
    return x - y

def multiplicar(x, y):
    return x * y

def dividir(x, y):
    if y == 0:
        return "Erro: Divisão por zero!"
    return x / y

def exponenciar(x, y):
    return x ** y

def mostrar_menu():
    print("\n--- Calculadora ---")
    print("Escolha uma operação:")
    print("1. Adição")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("5. Exponenciação")
    print("0. Sair")

while True:
    mostrar_menu()
    escolha = input("Digite o número da operação: ")

    if escolha == '0':
        print("Encerrando a calculadora. Até mais!")
        break

    if escolha in ['1', '2', '3', '4', '5']:
        try:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
        except ValueError:
            print("Erro: Entrada inválida! Por favor, digite números.")
            continue

        if escolha == '1':
            print(f"Resultado: {num1} + {num2} = {adicionar(num1, num2)}")
        elif escolha == '2':
            print(f"Resultado: {num1} - {num2} = {subtrair(num1, num2)}")
        elif escolha == '3':
            print(f"Resultado: {num1} * {num2} = {multiplicar(num1, num2)}")
        elif escolha == '4':
            print(f"Resultado: {num1} / {num2} = {dividir(num1, num2)}")
        elif escolha == '5':
            print(f"Resultado: {num1} ^ {num2} = {exponenciar(num1, num2)}")
    else:
        print("Opção inválida! Por favor, selecione uma opção do menu.")
