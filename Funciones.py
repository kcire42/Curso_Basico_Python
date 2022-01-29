#def imprimir_mensaje():
 #   print("Hola")
    
#imprimir_mensaje()
#imprimir_mensaje()
#imprimir_mensaje()
def conversacion(nombre,mensaje):
    print("Hola "+ nombre)
    print(mensaje)
    print("muchas gracias por tu atencion")

opcion = input("ingrese una opcion 1,2,3: ")
if opcion == '1':
    nombre = input("Ingrese su nombre: ")
    conversacion(nombre,"Elegista la opcion:"+opcion)
elif opcion == '2':
    nombre = input("Ingrese su nombre: ")
    conversacion(nombre,"Elegista la opcion: "+opcion)





