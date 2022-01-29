def contador_uno_en_uno():
    contador = int(input("Ingrese hasta que numero quiere que llege el contador: "))
    incremento = int(input("Ingrese el incremente que desea: "))
    i = 0
    while i < contador:
        print(i)
        i += incremento
    print(i)
    print("Boom!!!!!")


def contador_con_limite():
    j = int(input("Ingrese el numero a iniciar: "))
    incremento = int(input("Ingrese el incremento: "))
    contador = int(input("Ingrese el numero a contar: "))
    while j < contador:
        print(j)
        j += incremento
    print(j)
    print("jalo")


def multiplos():
    """Programa que te ayudar a obtener multiplos de m*n"""
    m = int(input("Ingrese el numero m: "))
    n = int(input("Ingrese el numero n: "))
    multiplicacion = m*n
    print(multiplicacion)
    i = 1
    multiplos = []
    no_multiplos = []
    while i < 100:
        resultado = i/multiplicacion
        #print(f"El valor de i es {i} entre {multiplicacion} da un resultado de {resultado} ")
        
        if  i%multiplicacion == 0:
            modulo = i%multiplicacion
            multiplos.append(i)
            #print (f"{i} es multiplo de {multiplicacion}")
            
        else:
            #print(f"{i} no es multiplo de {multiplicacion}")
            no_multiplos.append(i)
        i += 1
    print(f"Estos numero son multiplos {multiplos} de {multiplicacion} ")
    print(f"Estos numeros {no_multiplos} no son multiplos de {multiplicacion}")


def potencias():
    numero = int(input("Ingrese del que desea hacer la potencia: "))
    potencia = int(input("Ingrese cuantas interacion quiere hacer: "))
    i = 0 
    while i < potencia:
        potencia_elevada = numero**i
        print(f"La potencia de {numero} elevado a la {i} da un resultado de {potencia_elevada}")
        i +=1


def sumatoria():
    n = int(input("Ingrese un numero"))
    m = int(input("Ingrese el numero hasta el que deseas sumar"))
    i = n+1
    limite = m+1
    if n<m:
        while i < limite:
            print(f"n es ={n} y i tiene un valor de={i} la suma de estos dos es ={n+i}")
            n = n+i
            i +=1
    else:
        print("m no puede ser mayor a n") 


def factorial(numero):
    #numero = int(input("Ingrese el numero que desea obtener el factorial: "))
    i = 1
    factorial = 1
    limite = numero+1
    while i < limite:
        factorial = factorial*i
        i+=1
    #print(f"El factorial de {numero} es igual a {factorial}")
    return factorial


def combinaciones():
    n = int(input("Ingrese el numero n: "))
    m = int(input("Ingrese el numero m: "))
    if n >=m:
        c = factorial(n)/(factorial(n-m)*factorial(m))
        print(c)
    else:
        print("n es menor a m")



if __name__ == '__main__':
    opcion_menu = int(input("Ingrese que programa quiere ejecutar: "))
    if opcion_menu == 1:
        contador_uno_en_uno()
    elif opcion_menu ==2:
        contador_con_limite()
    elif opcion_menu == 3:
        multiplos()
    elif opcion_menu == 4:
        potencias()
    elif opcion_menu ==5:
        sumatoria()
    elif opcion_menu == 6:
        numero = int(input("Ingrese el numero que desea obtener el factorial: "))
        factorial(numero)
    elif opcion_menu == 7:
        combinaciones()