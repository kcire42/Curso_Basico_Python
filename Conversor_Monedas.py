def conversor_pesos_a_dolares(moneda_local,valor_dolar):
    pesos = float(input("Ingrese la cantidad de pesos " + moneda_local+": " ))
    valor_dolar_americano = float(valor_dolar)
    dolares_americanos = pesos/valor_dolar_americano
    dolares_americanos = round(dolares_americanos,2)
    dolares_americanos = str(dolares_americanos)
    resultado ="Usted tiene: "+ dolares_americanos + " dolares"
    return resultado
    

menu_principal = """Bienvenido al convertidor de monedas
1- Convertir de pesos a dolares
2- Convertir de dolares a pesos
Ingrese la opcion deseada: """
opcion_menu = input(menu_principal)
opcion_menu = int(opcion_menu)
if opcion_menu == 1:
    menu_monedas = """
    1- Convertir de pesos mexicanos a dolares
    2- Convertir de pesos argentinos a dolares
    3- Convertir de pesos colombianos a dolares
    Ingrese la opcion deseada: """
    tipo_moneda = int(input(menu_monedas))
    if tipo_moneda == 1:
        convertido = conversor_pesos_a_dolares("mexicanos","22.07")
        print(convertido)

        #pesos_mexicanos = input("Ingrese la cantidad de pesos: ")
        #valor_dolar_americano = 22.07
        #dolares_americanos = float(pesos_mexicanos)/valor_dolar_americano
        #dolares_americanos = round(dolares_americanos,2)
        #dolares_americanos = str(dolares_americanos)
        #print("Usted tiene: "+ dolares_americanos + " dolares")
    elif tipo_moneda == 2:
        convertido = conversor_pesos_a_dolares("argentinos","72.57")
        print(convertido)
        #pesos_argentinos = input("Ingrese la cantidad de pesos: ")
        #valor_dolar_americano = 72.57
        #dolares_americanos = float(pesos_argentinos)/valor_dolar_americano
        #dolares_americanos = round(dolares_americanos,2)
        #dolares_americanos = str(dolares_americanos)
        #print("Usted tiene: "+ dolares_americanos + " dolares")
    elif tipo_moneda == 3:
        convertido = conversor_pesos_a_dolares("colombianos","3782.00")
        print(convertido)
        #pesos_colombianos = input("Ingrese la cantidad de pesos: ")
        #valor_dolar_americano = 3782.00
        #dolares_americanos = float(pesos_colombianos)/valor_dolar_americano
        #dolares_americanos = round(dolares_americanos,2)
        #dolares_americanos = str(dolares_americanos)
        #print("Usted tiene: "+ dolares_americanos + " dolares")

if opcion_menu == 2:
    dolares_americanos = input("Ingrese la cantidad de dolares: ")
    valor_dolar_americano = 22.07
    pesos_mexicanos = float(dolares_americanos)*valor_dolar_americano
    pesos_mexicanos = round(pesos_mexicanos,2)
    pesos_mexicanos = str(pesos_mexicanos)
    print("Usted tiene: " + pesos_mexicanos + "pesos")