def line():
    # Pido al usuario que introduzca los valores para A, B, X1 y X2
    A = float(input("Ingrese el coeficiente A: "))
    B = float(input("Ingrese el coeficiente B: "))
    X1 = float(input("Ingrese el coeficiente X1: "))
    X2 = float(input("Ingrese el coeficiente X2: "))

    # Defino la función lineal con la que quiero trabajar
    Y1 = A * X1 + B
    Y2 = A * X2 + B

    # Calculo la distancia entre los dos puntos
    distacia = (((Y1 - Y2) ** 2) + ((X1 - X2) ** 2)) ** 0.5

    # Repaso de valores solicitados (solo A, B, X1, X2)
    print(f"El coeficiente A de su ecuación de la recta es: {A}")
    print(f"El coeficiente B de su ecuación de la recta es: {B}")
    print(f"El coeficiente X1 de su ecuación de la recta es: {X1}")
    print(f"El coeficiente X2 de su ecuación de la recta es: {X2}\n")

    # Presentación de la ecuación
    print("Para la siguiente ecuación:")
    print(f"\tY = {A}X + {B}\n")

    # Presentación de los puntos
    print("Dados los siguientes puntos:")
    print(f"\tP1 ({X1}, {Y1})")
    print(f"\tP2 ({X2}, {Y2})\n")

    # Presentación de la distancia
    print(f"La distancia entre ellos es: {distacia}")
   
