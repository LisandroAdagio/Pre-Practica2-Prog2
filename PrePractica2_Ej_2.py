#Crear un programa que permita al usuario ingresar una lista de numeros. De esa lista de numeros almacenar en otra lista los numeros impares.

#El programa debe de mostrar por pantalla la lista de numeros originales y la lista de numeros impares.

#INICIO
lista = []
lista_impar = []
for i in range(3):
    valor = int(input("Ingrese un valor porfa "))
    lista.append(valor)
    if valor % 2 != 0:
        lista_impar.append(valor)

print(lista)
print(lista_impar)

#FIN