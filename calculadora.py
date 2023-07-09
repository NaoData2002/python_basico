def calculadora():
    while True:
        operacion = input("Ingrese la operación (+, -, *, /): ")
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))

        if operacion == "+":
            resultado = num1 + num2
        elif operacion == "-":
            resultado = num1 - num2
        elif operacion == "*":
            resultado = num1 * num2
        elif operacion == "/":
            resultado = num1 / num2
        else:
            print("Operación inválida")

        print("El resultado es:", resultado)
calculadora()
