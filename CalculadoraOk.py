def calculator():
    # Create dictionary
    menu = {
        '1': 'Suma',
        '2': 'Resta',
        '3': 'Multiplicación',
        '4': 'División',
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
        option = input("\n¿Qué operación deseas realizar? (1/2/3/4/0): ")

        # Validate option 0, close app
        if option == '0':
            exit()

        if option in menu:
            # Validate float number
            try:
                num1 = float(input("\nIngresa el primer número: "))
                num2 = float(input("Ingresa el segundo número: "))
            except ValueError:
                print("Entrada no valida")
        
            # Do operations
            if option == '1':
                print("El resultado de la suma es: ", suma(num1, num2) )
            elif option =='2':
                print("El resultado de la resta es: ", resta(num1, num2))
            elif option == '3':
                print("El resultado de la  multiplicación es: ", multiplicacion(num1, num2))
            elif option == '4':
                print("El resultado de la división es: ", division(num1, num2))
        else:
            print ("Opción no valida.")
        
        # Call function again
        again()

def suma(a, b):
    # Do sum
    return a + b

def resta(a, b):
    # Do abstract
    return a - b

def multiplicacion(a, b):
    # Do multiply
    return a * b

def division(a, b):
    # Validate division for 0
    if a == 0:
        # If division is for 0 return error msg
        return "No es posible la división entre 0"
    else:
        # Do division
        return a / b

def again():
    # Ask if need to do other operation and validate response
    calc_again = input("\n¿Deseas realizar otra operación? (s / n): ")

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