# Importar variables de archivo ..///ConstantesCalificacion.py
import ConstantesCalificacion

# Ingresar Valor entero entre 0 a 100 mediante una variable vacia-tipo entero
nombrealunmo= input ("Introduce el nomnre del alunmo a calificar: ")
calificacion= int(input ("Introduce la calificación del Alunmo: "))



if calificacion >= ConstantesCalificacion.alta:
    print (nombrealunmo,"¡Felicidades! Has aprobado con una calificación sobresaliente.")
elif calificacion >= ConstantesCalificacion.media:
    print (nombrealunmo,"Has aprobado satisfactoriamente.")
elif calificacion >= ConstantesCalificacion.baja:
     print (nombrealunmo,"Has aprobado, pero necesitas mejorar un poco.")
else:
     print (nombrealunmo,"Lo siento, has reprobado. Debes esforzarte más en la próxima evaluación.")





