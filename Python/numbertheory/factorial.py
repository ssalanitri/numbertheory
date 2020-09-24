
# coding=UTF-8
"""
Factorial: Evalute n factorial, 
recursive implementation

"""

def factorial(n):
    if n == 0 or n==1:
        return 1
        
    else:
        return n*factorial(n-1)
        
def factorialR(n):
    if n<0:
        return None
    elif n<2:
        return n
    else:
        return n*factorial(n-1)

def combin(n,k):
    return factorial(n)/factorial(n-k)

def permut(n,k):
    return combin(n,k)/factorial(k)

print factorial(5), combin(33,6), permut(33,6)       
        

        