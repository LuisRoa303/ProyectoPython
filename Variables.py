# Ingresar valores mediante una variable vacia-tipo string
datoingresa= input("Introduce una palabra: ")

# Ingresar valores mediante una variable vacia-tipo entero
secuencia= int(input ("Introduce un número "))

# Ingresar valores mediante una variable vacia-tipo entero
dinero= float(input ("Introduce el salario "))

# Importar Contantes
import Constantes

# Variable de nombre principal

nombre="Luis F Roa Zarta"

# Variabel de edad principal
EDAD=36

#Variable en linea con diferente valor
profesion,residencia,empleador="Ingeniero Induatrial","Bogotá","Con un trabajo ganando millones"



"""
Esta es otra forma de 
bloque de cometentario

"""

print(secuencia,datoingresa,"Mi nombre es:", nombre, "y tengo:",EDAD, "años de edad", 
      "Y mi identificación es:",Constantes.UID,"me gradue como:",
      profesion,"vivo actualmente en",residencia,"y esto feliz dado que",empleador,dinero)

print (type(datoingresa))

print (type(secuencia))

# Operaciones aritméticas
x=10
y=5

print("suma de dos variales, resultado de X + Y=",(x + y))

print("resta de dos variales, resultado de X - Y=",(x - y))

print("multiplicación de dos variales, resultado de X * Y=",(x * y))

print("division de dos variales, resultado de X / Y=",(x / y))

print("division de dos variales (producto entero), resultado de X // Y=",(x // y))

print("Exponente usando dos variales, resultado de X ** Y=",(x ** y))


# Operadores comparativos

print("X es mayor que Y=",(x > y))

print("X es menor que Y=",(x < y))

print("X es igual que Y=",(x == y))

print("X no es igual que Y=",(x != y))

print("X  es mayor o igual que Y=",(x >= y))

print("X  es menor o igual que Y=",(x <= y))
 

# Uso de if

if secuencia < x:
    print("secuencia;",secuencia,"es menor que x:",x)
elif secuencia < 15:
    print("secuencia;",secuencia,"es menor que 15")
else:
    print("secuuencia;",secuencia,"se fue por el else jajaja")

# Uso de match puro 

match secuencia:

    case 1:
        print("Ruta Inicial")
    case 3:
        print("ruta intermedia")
    case _:
        print("toca que hagas algo")


# Uso de match con if

match secuencia:

    case 0:
        print("El cero es neutro")
    case secuencia if secuencia % 2 ==0:
        print("El número ingresado es par")
    case secuencia if secuencia % 2 !=0:
        print("El número es impar")
    case _:
        print("Número no reconocido")


# Uso de for con lista mediante variable ejemplo 1

# Variable tipo lista

frutas= ["fresa","mora","sandia","banano","pitaya","guayaba"]
contador=0

for fruta in frutas:
    contador +=1
    print (f"fruta #{contador}: {fruta}")
    if fruta == "pitaya": # esto es para parar el conteo en algo espeficico
        break # esto lo detiene


# Uso de for con lista mediante variable ejemplo 2

numeroslista = [1,2,3,4,5,6,7,8]

for lista in numeroslista:
    cuadrado = lista ** 2
    print(f"El número: {lista} tiene su valor al cuadrado: {cuadrado}")

# Uso de for con lista mediante variable ejemplo 3 promedio


numeros = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
suma = 0

for numero in numeros:
 suma += numero

promedio= suma / len (numeros)

print (f"el promedio de es: {promedio}")

numeros.append(21)

print(f"Se agrego un núevo número {numeros}")

del numeros[0]

print(f"Se removio un número {numeros}")

# uso de bucle while 

contador=1

while contador <=5:
    print (f"El conteo es #: {contador}")
    contador +=2

# suma con bucle while del 1 al 60

adicion=0
incremental=1


while incremental <= 60:
    adicion += incremental
    incremental += 1

print (adicion)


##################### uso de while con condicion de ingreso para detener##############################

a=0
b= int(input("Ingrese un número entero para generar suma progresvia de datos relacionados 'para salir ingresar número entero negativo' "))

while b >=0:
    a += b
    b= int(input("Ingrese un número entero para generar suma progresvia de datos relacionados 'para salir ingresar número entero negativo' "))

print(f"la suma de los datos ingresados es: {a}")



# suma con bucle while iniciando en 1 hasta donde diga el dato ingresado

ingreso= int(input("Ingrese un número entero para generar suma progresvia de datos relacionados: "))
adicion=0
incremental=1


while incremental <= ingreso:
    adicion += incremental
    print (f"Los datos a contrar son: {incremental}")
    incremental += 1
   

print (f"La suma acumulada de los datos es: {adicion}")


# Manejo de Cadenas len, upper, lower, split , substring

nombres= "Luis Fernado Roa Zarta"
Apellidos="Roa Zarta"
textocorto="hola"
textolargo="Nos va a ir muy bien todo es un proceso con calma y dedicación"
saldo= 200000

longuitud= len(nombres)

minisculas=nombres.lower()

mayuscula=Apellidos.upper()

cambio=textocorto.replace("hola",nombres)

print(f"la longitud de es de: {longuitud}")

print(f"El primer apellidos es: {Apellidos[0:3]}")

print(f"split para hacer un texto lista-matriz: {Apellidos.split()}")

print(f" nombre en minuscula: {minisculas}")

print(f" nombre en mayuscula: {mayuscula}")

print(f" uso de replace: {cambio}")

# Reemplazo mas avanzado

nombre = "Luis"
saldo = 25000

tpl = "Hola {nombre}, tu saldo es {saldo}."

res = (tpl
       .replace("{nombre}", nombre)
       .replace("{saldo}", f"${saldo:,}"))
print(res)



# otra forma usando format 

tpl = "Hola {nombre}, tu saldo es de $: {saldo}."
print(tpl.format(nombre=nombres, saldo=saldo))


# Tuplas ejercicio 1

mi_tupla1= (("Luis",36),("Ruben",30),("Fernanda",33))

for nombre, edad in mi_tupla1:
    if edad <=35:
        print (f"tienen menos de 35 años: {nombre}")

# Tuplas ejercicio 2

mi_tupla2=(1,2,3,4,5,6)

suma= sum(mi_tupla2)

print(f"La suma total de la tupla es: {suma}")

# Tuplas ejercicio 3
var1=0
for conteo in mi_tupla2:
    if conteo <3:
        var1 +=conteo

print (var1)
        
#### Ejemplo con tupla##

palabra_buscar= input("Por favor ingrese el nomnbre de la fruta que desea buscar: ")
frutas=("manzana","banana","cereza")


    
if palabra_buscar in frutas:
       print ("esta en el inventario")
else:
       print ("no esta en el inventario")    

################### Uso de Diccionario############################

persona= {"nombre":"luis",
          "apellido":"roa",
          "edad":36,
          "ciudad":"Bogotá"}

perfil=persona

print(persona["nombre"])

print(perfil["ciudad"])

################### Uso de Diccionario con ingreso de datos############################

persona= {"nombre":None,
          "apellido":None,
          "edad":None,
          "direccion":None,
          "ciudad":None}

persona["nombre"]= str(input("Escribe tu nombre: "))
persona["apellido"]= str(input("Escribe tu apellido: "))
persona["edad"]= int(input("Escribe tu edad: "))
persona["direccion"]= str(input("Escribe tu direccion: "))
persona["ciudad"]= str(input("Escribe tu ciudad: "))

print(persona)

print(f"Me llamo:",persona["nombre"],persona["apellido"],"tengo",persona["edad"],"años de edad vivo en",persona["ciudad"], "en la", persona["direccion"] )

################### Uso de funciones############################

def suma (a,b):
    resultado= a+b
    return resultado

operacion= suma(10,9)

print(operacion)


################### Uso de funciones con datos de entrada############################

def adicion (c,d):
    respuesta= c+d
    return respuesta

varc= int(input("Ingresa el primer número entero: "))
vard= int(input("Ingresa el segundo número entero: "))

operacion1= adicion(varc,vard)

print(operacion1)

################### Uso de funciones con datos de entrada y con if ############################

def espar(numero):
    if numero % 2 ==0:
        return True
    else:
        return False
    
numero= int(input("Ingresa un número entero: "))

if espar(numero)== True:
    print ("El número es par")
else:
    print ("El número es inpar")


###################### uso de max lista y funciones #######################

def maxlista(numeros):
    maximo= max(numeros)
    return maximo

listanumeros= [50,60,100,250,1213,1214]
resultado= maxlista(listanumeros)

print(resultado)


################ Calculadora###################

def calculadora(numero1,numero2,operador):
    if operador == "+":
        return numero1 + numero2
    elif operador == "-":
         return numero1 - numero2
    elif operador == "*":
         return numero1 * numero2
    elif operador == "/":
         return numero1 - numero2
    else:
         return "Operación no valida"
    

numero1=int(input("Escribe tu primer número: ")) 
numero2=int(input("Escribe tu segundo número: ")) 
operador=str(input("Escribe tu operador matematico +,-,*,/: ")) 

respuesta=calculadora(numero1,numero2,operador)

if respuesta=="Operación no valida":
     print(f"Tu operador matematico ingresado ha generado una {respuesta}")
else:
     print(f"Tu resultado es: {respuesta}")

############################# uso de Modulos calculadora.py#########################
import calculadora

numero1= int(input("Ingresa tu primer número: "))
numero2= int(input("Ingresa tu segundo número: "))

suma= calculadora.suma(numero1,numero2)

resta= calculadora.resta(numero1,numero2)

multiplicacion= calculadora.multiplicacion(numero1,numero2)

division= calculadora.division(numero1,numero2)

print(f"El resultado de su suma es: {suma}, de tu resta: {resta}, de tu multiplicacion es: {multiplicacion}, de tu division es: {division}"  )


############################### uso de clases #########################################

class persona:
    def __init__(self,nombre,edad,profesion):
        self.nombre=nombre
        self.edad=edad
        self.profesion=profesion

    def saludar(self):
        print(f"Mi nombres es: {self.nombre} tengo {self.edad} años de edad y mi profesión es: {self.profesion}")

persona1= persona("Luis",36,"ingeniero industrial")

persona1.saludar()

persona2= persona("Fernanda",33,"ingeniero sistemas")

persona2.saludar()


################################3 Manejo de Clases II ##############################

class calculadora2:
    def suma(self,numero1,numero2):
        return numero1+numero2
    
    def resta(self,numero1,numero2):
        return numero1-numero2
    
    def multiplicacion(self,numero1,numero2):
        return numero1*numero2
    
    def division(self,numero1,numero2):
        if numero1==0 and numero2==0:
            print("Su resultado es Indefinido")
        elif numero2==0:
            print("Su resultado es Indefinido")
        else:
            return numero1/numero2
        
numero1=float(input("Ingrese el primer número: "))
numero2=float(input("Ingrese el segundo número: "))

cal= calculadora2()

resulsuma= cal.suma(numero1,numero2)
resulresta= cal.resta(numero1,numero2)
resulmultiplicacion= cal.multiplicacion(numero1,numero2)
resuldivision= cal.division(numero1,numero2)

print(f"tu resultado de suma es: {resulsuma}, el de resta es: {resulresta}, el de multiplicacion es: {resulmultiplicacion} y el de division es: {resuldivision} ")









