numero= int(input ("Ingresa un número: "))

match numero:
    case numero if numero <0:
        print("Estas ingresando un número negativo")
    case numero if 0 <= numero < 10:
        print("Ingresaste un número entre cero y 9")
    case numero if numero >=10:
        print("Ingresaste un número igual o mayor que diez")
    case _:
        print ("no se encuentra en ningún rango conocido.")


