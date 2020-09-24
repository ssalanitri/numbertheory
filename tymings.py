# file = timings.py

import sys, time
from factorlib import factor, factor2, factor3

n = long( sys.argv[1] )
a = time.time()
result = factor(n)

b = time.time()
print "1: ", b - a
a = time.time()

result = factor2(n)
b = time.time()
print "2: ", b - a

a = time.time()
result = factor3(n)
b = time.time()
print "3: ", b - a

print n, "==>", result
