def leap_year():
# Defino la variable "año", para luego aplicarla al "if":

    a = int(input("Año: "))

    if (a % 4 == 0) and (a % 100 != 0 or a % 400 == 0):
        print(f"El {a} es BISIESTO")
    else:
        print(f"El {a} NO es BISIESTO")
