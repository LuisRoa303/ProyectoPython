# Uso de for con lista mediante variable ejemplo 1

# Variable tipo lista

frutas= ["fresa","mora","sandia","banano","pitaya","guayaba"]
contador=0

for fruta in frutas:
    contador +=1
    print (f"fruta #{contador}: {fruta}")
    if fruta == "pitaya": # esto es para parar el conteo en algo espeficico
        break # esto lo detiene