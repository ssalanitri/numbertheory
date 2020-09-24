
 # coding=UTF-8

import sys,time
N = 100

#Devuelve la cantidad de números primos menores que n. 
def criba_eratostenes(n):
  multiplos = set()
  for i in range(2, n+1):
    if i not in multiplos:
      print(i)
      
      multiplos.update(range(i*i, n+1, i))

a = time.time()
criba_eratostenes(N)
b = time.time()

print("Criba: ",str(N), str(b - a) + "s")