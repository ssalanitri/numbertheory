# coding=UTF-8

"""
Factor2: Mejora de factor1

En este caso oevita dividir por los multimplos de 2
Luego de probar si es multiplo de 2 el algoritmo prueba con los números pares

"""
import os,sys,time

N = 10997442345

def factor2(n):
    d = 2
    factors = [ ]
    while n % d == 0:
        factors.append(d)
        n = n/d
        
    d = 3
    
    while n > 1:
        if n % d == 0:
            factors.append(d)
            n = n/d
        else:
            d = d + 2
        
    return factors
        
a = time.time()
f = factor2(N)
b = time.time()

print "Time: ",b-a
       

for n in range(0,len(f)):
    print f[n]
