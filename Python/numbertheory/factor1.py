    # coding=UTF-8
import os,sys,time
"""
Factorización de n

"""
N = 10997442345

def factor(n):
    d = 2
    factors = [ ]
    while n > 1:
        if n % d == 0:
            factors.append(d)
            n = n/d
        else:
            d = d + 1
    
    return factors

a = time.time()
f = factor(N)
b = time.time()

print "Time: ",b-a


for n in range(0, len(f)):
    print f[n]
