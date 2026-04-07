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