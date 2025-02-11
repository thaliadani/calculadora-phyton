def calculadora(num1, num2, op):
    if op == "+":
        return num1 + num2
    elif op == "-":
        return num1 - num2
    elif op == "*":
        return num1 * num2
    elif op == "/":
        return num1 / num2
    else:
        return 0

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
op = input("Digite a operação (+, -, *, /): ")
print(calculadora(num1, num2, op))