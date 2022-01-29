import math

def media(datos):
    return suma(datos)/ len(datos)

def suma(datos):
    resultado = 0 
    for numero in datos:
        resultado = resultado + numero
    return resultado

def varianza(datos):
    mu = media(datos) 
    sumatoria = 0 
    for dato in datos:
        sumatoria  += (dato-mu)**2
        #sumatoria = sumatoria + dato_menos_media
       # print(dato_menos_media) 
    #print(sumatoria)
    return sumatoria/len(datos)

def desviacion_estandar(datos):
    return math.sqrt(varianza(datos))

def mediana(datos):
    for dato in datos:
        
    
        
        
    


if __name__ == '__main__':
    
    print(f'La suma de los numeros es: {suma([1,2,3,4,5])}')
    print(f'La media es de:{media([1,2,3,4,5])}')
    print(f'La varianza es de: {varianza([1,2,3,4,5])}')
    print(f'La desviacion estandar es de: {desviacion_estandar([1,2,3,4,5])}')