# coding=UTF-8

"""

factor3:  Es mejora de factor2 porque recorre 

Se busca divisores de n hasta raiz de n.

"""
import os,sys,time

N = 10997442345

def factor3(n):
    d = 2
    factors = [ ]
    while n % d == 0:
        factors.append(d)
        n = n/d
        
    d = 3
    
    while n > 1 and d*d <= n:
        if n % d == 0:
            factors.append(d)
            n = n/d
        else:
            d = d + 2
    if n > 1:
        factors.append(n)
        
    return factors


a = time.time()
f = factor3(N)
b = time.time()

print "Time: ",a-b
       

for n in range(0,len(f)):
    print f[n]



