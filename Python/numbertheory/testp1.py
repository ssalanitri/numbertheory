
# coding=UTF-8
"""
Algorithm
IsPrime: 

IMPUT: n perteneciente a Z
OUTPUT: True si n es primo , False si n es no primo

"""
import os,sys,time

#N = 367129485367127143774839380041017394964020200854210369

N = 10999993

def isprime(n):

    print "------------------------------------"
    print "n: ",n
    print "n < 2: ", n < 2
    
    if(n == 2):  #2 es el único primo par.
        return True
    
    print "n%2: ",n%2 == 0
    
 
    i = 3
    while (i**2 <= n):  #Computa has raiz de n.
        print "i: ",i
        print "i**2: ",i**2
        print "i**2 <=n: ",i**2<=n
        print "i%n: ",i%n == 0
        print "------------------------------------"
        
        if(i%n == 0):
            return False
            
        i = i + 2
        
    return True
        
        
    
a = time.time()        
print isprime(N)
b = time.time()
print "Time: ",a-b
