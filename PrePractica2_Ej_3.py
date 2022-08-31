#Crear un programa que utilice la estructura try - catch. El usuario debe de ingresar dos numeros y mostrar por pantalla
#el resultado de la división entre ambos numeros. 

#En caso de que el divisor sea 0 utilizar la excepción ZeroDivisionError y mostrar el error por pantalla.


#INICIO
num_1 = int(input("Ingrese el primer numero: ")) 
num_2 = int(input("Ingrese el segundo numero: "))
try:
    resultado = num_1 / num_2
except ZeroDivisionError as exception:
    print(f"Ha ocurrido un error | {exception}")
finally:
    print("Proceso finalizado " + str(resultado))
#FIN