# coding=UTF-8

import math

def fino1(n):
    
    Fn = []
    Fn.append(1)
    Fn.append(1)
    for k in range(2,n):
      Fn.append(Fn[k-1] + Fn[k-2])

    return Fn[n-1]
    
    
    
#Implementación recursiva del algoritmos para calcular los numeros de fibonacci hasta n elementos.    
def recur_fibo(n):
   """Recursive function to
   print Fibonacci sequence"""
   if n <= 1:
       return n
   else:
       return(recur_fibo(n-1) + recur_fibo(n-2))
       


#Obtienen en n-enesimo numero de fibonacci usand fórmula de recurrencia.
def finoN(n):
    Fn = []
    enesimo = (1/math.sqrt(5)) #*math.pow(((1+math.sqrt(5)+1)/2),n+1) # - (1/math.sqrt(5)*math.pow(((1-math.sqrt(5)+1)/2),n+1)
    #Fn.append(nesimo)
    #Fn.append(fino1(n))
    print enesimo
    
    return Fn


"""
# Change this value for a different result
nterms = 120

# uncomment to take input from the user
#nterms = int(input("How many terms? "))

# check if the number of terms is valid
Fn = []

if nterms <= 0:
   nterms = raw_input("Plese enter a positive integer")
else:
   print("Fibonacci sequence:")
   for i in range(nterms):
       Fn.append(recur_fibo(i))
print Fn
"""