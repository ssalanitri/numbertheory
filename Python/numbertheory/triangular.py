# coding=UTF-8


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
        
# Si es es triangular devuelve el siguiente sino False.
def nearTriangular(N):
    
    Near = []
    
    n=1
    
    while  n <= N:
        if(N == n*(n+1)/2):
            Near.append((n-1)*n/2)
            Near.append((n+1)*(n+2)/2)
            return Near
        n = n + 1
        
    return False
    
#Devuele el triangular inferior y superior a un entero n dado.
#Si n es triangular devulve n.
def nearInteger(n):   
    Near = []
    draft = []*(n+1)
    
    if n == 1: return n 
        
    for i in range(1,n+1):
         
        ni = i*(i+1)/2
        draft.append(ni)
        
        if  i > 1 and i == ni:
            return i
        elif ni > n:
            Near.append((i-1)*i/2)
            Near.append(ni)
            return Near
       
        
    return n
    
        
n = 561
print nearInteger(n)


            
                
                
 