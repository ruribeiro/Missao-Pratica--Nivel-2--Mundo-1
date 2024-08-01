saida = ""

def adicao(num1, num2):
    return num1 + num2

def subtracao(num1, num2):
    return num1 - num2

def multiplicacao(num1, num2):
    return num1 * num2

def divisao(num1, num2):
    if num2 == 0:
        return "Não foi possível realizar a divisão por 0"
    else:
        return num1 / num2

def calculadora(num1, num2, operacao):
    if operacao == "+" or operacao == "adicao":
        resultado = adicao(num1, num2)
    elif operacao == "-" or operacao == "subtracao":
        resultado = subtracao(num1, num2)
    elif operacao == "*" or operacao == "multiplicacao":
        resultado = multiplicacao(num1, num2)
    elif operacao == "/" or operacao == "divisao":
        resultado = divisao(num1, num2)
    else:
        return "Operação inválida"
    return resultado

while saida.upper() != "N":
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    operacao = input("Digite a operação (+, -, *, / ou o nome da operação): ")
    resultado = calculadora(num1, num2, operacao)
    print("Resultado da operação:", resultado)
    saida = input("Deseja continuar? (S/N): ")


