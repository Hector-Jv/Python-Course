def funcion_decoradora(funcion_parametro):

    def funcion_interior(*args, **kwargs):

        # Acciones adicionales que decoran

        print("Vamos a realizar un cálculo: ")

        funcion_parametro(*args, **kwargs)

        # Acciones adicionales que decoran

        print("Hemos terminado el cálculo. ")

    return funcion_interior

@funcion_decoradora
def suma(num1, num2):
    print(num1 + num2)

@funcion_decoradora
def resta(num1, num2):
    print(num1 - num2)

@funcion_decoradora
def potencia(base, exponente):
    print(pow(base, exponente))

suma(5, 6)
resta(5, 6)
potencia(base=5, exponente=3)