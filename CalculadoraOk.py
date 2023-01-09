import numpy as np

def calculator():
    # Create dictionary
    menu = {
        '1': 'Sumar',
        '2': 'Restar',
        '3': 'Multiplicar',
        '4': 'Dividir',
        '5': 'Raíz n',
        '6': 'Exponente n',
        '7': 'Seno',
        '8': 'Coseno',
        '9': 'Tangente',
        '0': 'Salir'
    }

    # Initilize option for first time
    option = '1'

    # Validate that option is in menu
    while option in menu:
        # Print title
        print("\n>>>>> Calculadora")
        # Iterate menu dictionary and print
        for key in menu.keys():
            print(f'{key}. {menu[key]}')

        # Request operation
        option = input("\n¿Qué operación deseas realizar? (1 / 2 / 3/ 4 / 5 / 6 / 7 / 8 / 9 / 0): ")

        # Validate option 0, close app
        if option == '0':
            exit()

        if option in menu:
            # Do operations
            if option == '1':
                print("SUMA > El resultado es: ", sumar())
            elif option =='2':
                print("RESTA > El resultado es: ", restar())
            elif option == '3':
                print("MULTIPLICACIÓN > El resultado es: ", multiplicar())
            elif option == '4':
                print("DIVIDIR > El resultado es: ", dividir())
            elif option == '5':
                print("RAIZ CUADRADA > El resultado es: ", raiz())
            elif option == '6':
                print("EXPONENCIAL > El resultado es: ", exponencial())
            elif option == '7':
                print("SENO > El resultado es: ", seno())
            elif option == '8':
                print("COSENO > El resultado es: ", coseno())
            elif option == '9':
                print("TANGENTE > El resultado es: ", tangente())
        else:
            print ("Opción no valida.")
        
        # Call function again
        again()

def sumar():
    # Validate float number
    try:
        a = float(input("\nIngresa el primer número: "))
        b = float(input("Ingresa el segundo número: "))
        return a + b
    except ValueError:
        print("Entrada no valida")

def restar():
    # Validate float number
    try:
        a = float(input("\nIngresa el primer número: "))
        b = float(input("Ingresa el segundo número: "))
        return a - b
    except ValueError:
        print("Entrada no valida")

def multiplicar():
    # Validate float number
    try:
        a = float(input("\nIngresa el primer número: "))
        b = float(input("Ingresa el segundo número: "))
        return a * b
    except ValueError:
        print("Entrada no valida.")

def dividir():
    try:
        a = float(input("\nIngresa el primer número: "))
        b = float(input("Ingresa el segundo número: "))
        if a == 0:
            # If division is for 0 return error msg
            return "No es posible la división entre 0"
        else:
            # Do division
            return a / b
    except ValueError:
        print("Entrada no valida.")
    
def raiz ():
    try:
        a = float(input("\nIngresa el primer número: "))
        return np.sqrt(a)
    except ValueError:
        print("Entrada no valida.")
    
def exponencial():
    # Validate float number
    try:
        a = float(input("\nIngresa el número: "))
        b = float(input("Ingresa la exponencia: "))
        return np.power(a, b)
    except ValueError:
        print("Entrada no valida")

def seno():
    # Validate float number
    try:
        a = float(input("\nIngresa los grados: "))
        return np.sin(np.radians(a))
    except ValueError:
        print("Entrada no valida")

def coseno():
    # Validate float number
    try:
        a = float(input("\nIngresa los grados: "))
        return np.cos(np.radians(a))
    except ValueError:
        print("Entrada no valida")

def tangente():
    # Validate float number
    try:
        a = float(input("\nIngresa los grados: "))
        return np.tan(np.radians(a))
    except ValueError:
        print("Entrada no valida")

def again():
    # Ask if need to do other operation and validate response
    calc_again = input("\n¿Deseas regresar al menú? (s / n): ")

    # Validate response
    if calc_again.lower() == 's':
        # Yes invocate funtion calculator
        calculator()
    elif calc_again.lower() == 'n':
        # No invocate exit
        exit()
    else:
        again()

calculator()