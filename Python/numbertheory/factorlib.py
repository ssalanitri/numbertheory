    # coding=UTF-8
import os,sys,time
"""
Factorización de n
factor.py
"""
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

