def factorial(numero):
    """Esta funcion se encarga de obtener el factorial de n numero
    """
    for i in range(1,n+1): 
    fact = fact * i 
      
    print ("The factorial of 23 is : ",end="") 
print (fact) 
   # if numero == 1:
      #  return 1
   # return numero * factorial(numero-1)
   
                

if __name__ == '__main__':
    numero = int(input("Ingrese el factorial del numero que quiere obtener: "))
    factorial(numero)
    
