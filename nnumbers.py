###################################################
# Name: nnumbers.py
# Description: n-agon number algoritms impementations.
# Author: Salanitri Sergio
# Date: 24-07-2018
# Version: 0.1 
##################################################


class Triangular(object):
    """docstring for ClassName."""
    # def __init__(self, arg):
    #     super(Triangular, self).__init__()
    #     self.arg = arg
        
    #Get the triangular numbers minir than n. 
    def getTriangulars(self,n):
        nt = []
        
        for i in range(1,n):
            nt.append(i*(i+1)/2)
        
        return nt

    def getTriangular(self, n):
        """
        Get the nth trianguular number (sum i=1  to n {i})
        """
        return n*(n+1)/2


    def isTriangular(self,n):
        x=1
        
        while  x <= n:
            if(n == x*(x+1)/2):
                return True
            n = n + 1
            
        return False
            
    # If N is triangular number return the next triagular, else return False.
    def nextTriangular(self, n):
        
        near = []
        
        x=1
        
        while  x <= n:
            if(n == x*(x+1)/2):
                near.append((x-1)*x/2)
                near.append((x+1)*(x+2)/2)
                return near
            n = n + 1
            
        return False
        
    #Returns the lower and upper triangular to a given integer
    #If n is triangular return n.
    def nearTriangular(self, n):   
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
        
        
# for(n in range(10)):
#     t =Triangular()
#     print(t.get_triangular(n))

            
                
                
 