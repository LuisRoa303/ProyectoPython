############################# uso de Modulos calculadora.py#########################
import calculadora

numero1= int(input("Ingresa tu primer número: "))
numero2= int(input("Ingresa tu segundo número: "))

suma= calculadora.suma(numero1,numero2)

resta= calculadora.resta(numero1,numero2)

multiplicacion= calculadora.multiplicacion(numero1,numero2)

division= calculadora.division(numero1,numero2)

print(f"El resultado de su suma es: {suma}, de tu resta: {resta}, de tu multiplicacion es: {multiplicacion}, de tu division es: {division}"  )

