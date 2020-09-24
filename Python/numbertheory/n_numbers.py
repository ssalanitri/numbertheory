###################################################
# Name: n_numbers.py
# Description: n-agon number algoritms impementations.
# Author: Salanitri Sergio
# Date: 24-07-2018
# Version: 0.1 
##################################################

def triangular(n):
    nt = []
    
    for i in range(1,n):
        nt.append(i*(i+1)/2)
    
    return nt


def isTriangular(N):
    n=1
    
    while  n <= N:
        if(N == n*(n+1)/2):
            return True
        n = n + 1
        
    return False
        
# If N is triangular number return the next triagular, else return False.
def nextTriangular(N):
    
    near = []
    
    n=1
    
    while  n <= N:
        if(N == n*(n+1)/2):
            near.append((n-1)*n/2)
            near.append((n+1)*(n+2)/2)
            return Near
        n = n + 1
        
    return False
    
#Returns the lower and upper triangular to a given integer
#If n is triangular return n.
def nearTriangular(n):   
    near = []
    draft = []*(n+1)
    
    if n == 1: return n 
        
    for i in range(1,n+1):
         
        ni = i*(i+1)/2
        draft.append(ni)
        
        if  i > 1 and i == ni:
            return i
        elif ni > n:
            near.append((i-1)*i/2)
            near.append(ni)
            return near
      
    return n
    
        
n = 561
print nearInteger(n)


            
                
                
 