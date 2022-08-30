#Crear un programa que permita ingresar una lista de numeros al usuario y muestre por pantalla el maximo entre ambos numeros.

#Nota : Hacerlo con la función max(a,b) y luego con una comparación

#INICIO
cantidad = int(input("Ingrese la cantidad de valores que desea ingresar: "))
lista = []

for i in range(cantidad):
    aux = [int(input("Ingrese un valor: "))] 
    lista.append(aux)

def max (a,b):
    if a == b:
        print(f"el valor {a} es igual que el valor {b}")
    elif a > b:
        print(f"{a} es mayor que {b}")

for i in range(cantidad):
    for j in range(cantidad):
        if i != j:
            max(lista[i], lista[j])


#FIN