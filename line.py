def line():
    # Pido al usuario que introduzca los valores para (A y B) y (X1 y X2):

    A = float(input("Ingrese un val para (A): "))
        B = float(input("Ingrese un val para (B): "))

    X1 = float(input("Ingrese un val. para (X1): "))
    X2 = float(input("Ingrese un val. para (X2): "))

# Defino la funcion lineal con la que quiero trabajar:

    Y1 = A*X1 + B
    Y2 = A*X2 + B

# Defino la funcion "Distancia" :
    
    distacia = (((Y1+Y2)**2+(X1+X2)**2)**0.5)

# Repaso de valores:

    print("Repazo de valores:")
    print(f"El coeficiente A de su ecuación de la recta es: {A}")
    print(f"El coeficiente B de su ecuación de la recta es: {B}")
    print(f"El coeficiente X1 de su ecuación de la recta es: {X1}")
    print(f"El coeficiente X2 de su ecuación de la recta es: {X2}")
    print(f"El coeficiente Y1 de su ecuación de la recta es: {Y1}")
    print(f"El coeficiente Y2 de su ecuación de la recta es: {Y2}")

# Presento los (prints) en el formato pedido:

    print("Para la siguiente ecuacion, los valores serán: ")
    
    print(f"\t Y = {A}*X + {B}")
    print("")
    print(f"P1: {X1};{Y1}")
    print(f"P2: {X2};{Y2}")

# Pinteo el calculo de la distancia: 
    print(f"La DISTANCIA entre P1 y P2 es: {distacia}")    
