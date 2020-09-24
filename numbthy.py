######################################################################################
# NUMBTHY.PY
# Basic Number Theory functions implemented in Python
# Note: Version 0.7 changes some function names to align with SAGE
# Note: Version 0.8 is compatible with both Python 2.5+ and 3.x
# Author: Robert Campbell, <r.campbel.256@gmail.com>
# Contributors: Ege Alpay; ZhiHang Fan
# Date: 13 Oct, 2019
# Version 0.84
# License: Simplified BSD (see details at bottom)
######################################################################################
"""Basic number theory functions.
	Functions implemented are:
		gcd(a,b) - Compute the greatest common divisor of a and b.
		xgcd(a,b) - Find [g,x,y] such that g=gcd(a,b) and g = ax + by.
		power_mod(b,e,n) - Compute b^e mod n efficiently.
		inverse_mod(b,n) - Compute 1/b mod n.
		is_prime(n) - Test whether n is prime using a variety of pseudoprime tests.
		euler_criterion(a, p) - Test whether a is a quadratic residue mod p
		euler_phi(n) - Compute Euler's Phi function of n - the number of integers strictly less than n which are coprime to n.
		carmichael_lambda(n) - Compute Carmichael's Lambda function of n - the smallest exponent e such that b**e = 1 for all b coprime to n.
		factor(n) - Return a sorted list of the prime factors of n with exponents.
		prime_divisors(n) - Returns a sorted list of the prime divisors of n.
		is_primitive_root(g,n) - Test whether g is primitive - generates the group of units mod n.
		sqrtmod(a,n) - Compute sqrt(a) mod n using various algorithms.
		TSRsqrtmod(a,grpord,n) - Compute sqrt(a) mod n using Tonelli-Shanks-RESSOL algorithm.
	Usage and help for the module is printed with the command help(numbthy) and a list of functions in the module with the command dir(numbthy).
	Some functions which are used internally and names used prior to ver 0.7 of existing functions are:
		isprime(n) - Test whether n is prime using a variety of pseudoprime tests. (Renamed is_prime(b,n) in ver 0.7)
		isprimeF(n,b) - Test whether n is prime or a Fermat pseudoprime to base b.
		isprimeE(n,b) - Test whether n is prime or an Euler pseudoprime to base b.
		factorone(n) - Find a factor of n using a variety of methods.
		factors(n) - Return a sorted list of the prime factors of n. (Prior to ver 0.7 named factor(n))
		factorPR(n) - Find a factor of n using the Pollard Rho method.
		invmod(b,n) - Compute 1/b mod n. (Renamed inverse_mod(b,n) in ver 0.7)
		powmod(b,e,n) - Compute b^e mod n efficiently. (Renamed power_mod(b,e,n) in ver 0.7)
		eulerphi(n) - Compute Euler's Phi function of n - the number of integers strictly less than n which are coprime to n. (Renamed euler_phi(n) in ver 0.7)
		carmichaellambda(n) - Compute Carmichael's Lambda function of n - the smallest exponent e such that b**e = 1 for all b coprime to n.  (Renamed carmichael_lambda(n) in ver 0.7)
		isprimitive(g,n) - Test whether g is primitive mod n.  (Renamed is_primitive_root(g,n) in ver 0.8)
"""

__version__ = '0.84'  # Format specified in Python PEP 396
Version = 'NUMBTHY.PY, version ' + __version__ + ', 13 Oct, 2019, by Robert Campbell, <r.campbel.256@gmail.com>'

import math  # Use sqrt, floor
import functools # Use reduce (Python 2.5+ and 3.x)
from mod import  Mod 

list_primes = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997, 1009, 1013, 1019, 1021, 1031, 1033, 1039, 1049, 1051, 1061, 1063, 1069, 1087, 1091, 1093, 1097, 1103, 1109, 1117, 1123, 1129, 1151, 1153, 1163, 1171, 1181, 1187, 1193, 1201, 1213, 1217, 1223, 1229, 1231, 1237, 1249, 1259, 1277, 1279, 1283, 1289, 1291, 1297, 1301, 1303, 1307, 1319, 1321, 1327, 1361, 1367, 1373, 1381, 1399, 1409, 1423, 1427, 1429, 1433, 1439, 1447, 1451, 1453, 1459, 1471, 1481, 1483, 1487, 1489, 1493, 1499, 1511, 1523, 1531, 1543, 1549, 1553, 1559, 1567, 1571, 1579, 1583, 1597, 1601, 1607, 1609, 1613, 1619, 1621, 1627, 1637, 1657, 1663, 1667, 1669, 1693, 1697, 1699, 1709, 1721, 1723, 1733, 1741, 1747, 1753, 1759, 1777, 1783, 1787, 1789, 1801, 1811, 1823, 1831, 1847, 1861, 1867, 1871, 1873, 1877, 1879, 1889, 1901, 1907, 1913, 1931, 1933, 1949, 1951, 1973, 1979, 1987, 1993, 1997, 1999, 2003, 2011, 2017, 2027, 2029, 2039, 2053, 2063, 2069, 2081, 2083, 2087, 2089, 2099, 2111, 2113, 2129, 2131, 2137, 2141, 2143, 2153, 2161, 2179, 2203, 2207, 2213, 2221, 2237, 2239, 2243, 2251, 2267, 2269, 2273, 2281, 2287, 2293, 2297, 2309, 2311, 2333, 2339, 2341, 2347, 2351, 2357, 2371, 2377, 2381, 2383, 2389, 2393, 2399, 2411, 2417, 2423, 2437, 2441, 2447, 2459, 2467, 2473, 2477, 2503, 2521, 2531, 2539, 2543, 2549, 2551, 2557, 2579, 2591, 2593, 2609, 2617, 2621, 2633, 2647, 2657, 2659, 2663, 2671, 2677, 2683, 2687, 2689, 2693, 2699, 2707, 2711, 2713, 2719, 2729, 2731, 2741, 2749, 2753, 2767, 2777, 2789, 2791, 2797, 2801, 2803, 2819, 2833, 2837, 2843, 2851, 2857, 2861, 2879, 2887, 2897, 2903, 2909, 2917, 2927, 2939, 2953, 2957, 2963, 2969, 2971, 2999, 3001, 3011, 3019, 3023, 3037, 3041, 3049, 3061, 3067, 3079, 3083, 3089, 3109, 3119, 3121, 3137, 3163, 3167, 3169, 3181, 3187, 3191, 3203, 3209, 3217, 3221, 3229, 3251, 3253, 3257, 3259, 3271, 3299, 3301, 3307, 3313, 3319, 3323, 3329, 3331, 3343, 3347, 3359, 3361, 3371, 3373, 3389, 3391, 3407, 3413, 3433, 3449, 3457, 3461, 3463, 3467, 3469, 3491, 3499, 3511, 3517, 3527, 3529, 3533, 3539, 3541, 3547, 3557, 3559, 3571, 3581, 3583, 3593, 3607, 3613, 3617, 3623, 3631, 3637, 3643, 3659, 3671, 3673, 3677, 3691, 3697, 3701, 3709, 3719, 3727, 3733, 3739, 3761, 3767, 3769, 3779, 3793, 3797, 3803, 3821, 3823, 3833, 3847, 3851, 3853, 3863, 3877, 3881, 3889, 3907, 3911, 3917, 3919, 3923, 3929, 3931, 3943, 3947, 3967, 3989, 4001, 4003, 4007, 4013, 4019, 4021, 4027, 4049, 4051, 4057, 4073, 4079, 4091, 4093, 4099, 4111, 4127, 4129, 4133, 4139, 4153, 4157, 4159, 4177, 4201, 4211, 4217, 4219, 4229, 4231, 4241, 4243, 4253, 4259, 4261, 4271, 4273, 4283, 4289, 4297, 4327, 4337, 4339, 4349, 4357, 4363, 4373, 4391, 4397, 4409, 4421, 4423, 4441, 4447, 4451, 4457, 4463, 4481, 4483, 4493, 4507, 4513, 4517, 4519, 4523, 4547, 4549, 4561, 4567, 4583, 4591, 4597, 4603, 4621, 4637, 4639, 4643, 4649, 4651, 4657, 4663, 4673, 4679, 4691, 4703, 4721, 4723, 4729, 4733, 4751, 4759, 4783, 4787, 4789, 4793, 4799, 4801, 4813, 4817, 4831, 4861, 4871, 4877, 4889, 4903, 4909, 4919, 4931, 4933, 4937, 4943, 4951, 4957, 4967, 4969, 4973, 4987, 4993, 4999, 5003, 5009, 5011, 5021, 5023, 5039, 5051, 5059, 5077, 5081, 5087, 5099, 5101, 5107, 5113, 5119, 5147, 5153, 5167, 5171, 5179, 5189, 5197, 5209, 5227, 5231, 5233, 5237, 5261, 5273, 5279, 5281, 5297, 5303, 5309, 5323, 5333, 5347, 5351, 5381, 5387, 5393, 5399, 5407, 5413, 5417, 5419, 5431, 5437, 5441, 5443, 5449, 5471, 5477, 5479, 5483, 5501, 5503, 5507, 5519, 5521, 5527, 5531, 5557, 5563, 5569, 5573, 5581, 5591, 5623, 5639, 5641, 5647, 5651, 5653, 5657, 5659, 5669, 5683, 5689, 5693, 5701, 5711, 5717, 5737, 5741, 5743, 5749, 5779, 5783, 5791, 5801, 5807, 5813, 5821, 5827, 5839, 5843, 5849, 5851, 5857, 5861, 5867, 5869, 5879, 5881, 5897, 5903, 5923, 5927, 5939, 5953, 5981, 5987, 6007, 6011, 6029, 6037, 6043, 6047, 6053, 6067, 6073, 6079, 6089, 6091, 6101, 6113, 6121, 6131, 6133, 6143, 6151, 6163, 6173, 6197, 6199, 6203, 6211, 6217, 6221, 6229, 6247, 6257, 6263, 6269, 6271, 6277, 6287, 6299, 6301, 6311, 6317, 6323, 6329, 6337, 6343, 6353, 6359, 6361, 6367, 6373, 6379, 6389, 6397, 6421, 6427, 6449, 6451, 6469, 6473, 6481, 6491, 6521, 6529, 6547, 6551, 6553, 6563, 6569, 6571, 6577, 6581, 6599, 6607, 6619, 6637, 6653, 6659, 6661, 6673, 6679, 6689, 6691, 6701, 6703, 6709, 6719, 6733, 6737, 6761, 6763, 6779, 6781, 6791, 6793, 6803, 6823, 6827, 6829, 6833, 6841, 6857, 6863, 6869, 6871, 6883, 6899, 6907, 6911, 6917, 6947, 6949, 6959, 6961, 6967, 6971, 6977, 6983, 6991, 6997, 7001, 7013, 7019, 7027, 7039, 7043, 7057, 7069, 7079, 7103, 7109, 7121, 7127, 7129, 7151, 7159, 7177, 7187, 7193, 7207, 7211, 7213, 7219, 7229, 7237, 7243, 7247, 7253, 7283, 7297, 7307, 7309, 7321, 7331, 7333, 7349, 7351, 7369, 7393, 7411, 7417, 7433, 7451, 7457, 7459, 7477, 7481, 7487, 7489, 7499, 7507, 7517, 7523, 7529, 7537, 7541, 7547, 7549, 7559, 7561, 7573, 7577, 7583, 7589, 7591, 7603, 7607, 7621, 7639, 7643, 7649, 7669, 7673, 7681, 7687, 7691, 7699, 7703, 7717, 7723, 7727, 7741, 7753, 7757, 7759, 7789, 7793, 7817, 7823, 7829, 7841, 7853, 7867, 7873, 7877, 7879, 7883, 7901, 7907, 7919, 7927, 7933, 7937, 7949, 7951, 7963, 7993, 8009, 8011, 8017, 8039, 8053, 8059, 8069, 8081, 8087, 8089, 8093, 8101, 8111, 8117, 8123, 8147, 8161, 8167, 8171, 8179, 8191, 8209, 8219, 8221, 8231, 8233, 8237, 8243, 8263, 8269, 8273, 8287, 8291, 8293, 8297, 8311, 8317, 8329, 8353, 8363, 8369, 8377, 8387, 8389, 8419, 8423, 8429, 8431, 8443, 8447, 8461, 8467, 8501, 8513, 8521, 8527, 8537, 8539, 8543, 8563, 8573, 8581, 8597, 8599, 8609, 8623, 8627, 8629, 8641, 8647, 8663, 8669, 8677, 8681, 8689, 8693, 8699, 8707, 8713, 8719, 8731, 8737, 8741, 8747, 8753, 8761, 8779, 8783, 8803, 8807, 8819, 8821, 8831, 8837, 8839, 8849, 8861, 8863, 8867, 8887, 8893, 8923, 8929, 8933, 8941, 8951, 8963, 8969, 8971, 8999, 9001, 9007, 9011, 9013, 9029, 9041, 9043, 9049, 9059, 9067, 9091, 9103, 9109, 9127, 9133, 9137, 9151, 9157, 9161, 9173, 9181, 9187, 9199, 9203, 9209, 9221, 9227, 9239, 9241, 9257, 9277, 9281, 9283, 9293, 9311, 9319, 9323, 9337, 9341, 9343, 9349, 9371, 9377, 9391, 9397, 9403, 9413, 9419, 9421, 9431, 9433, 9437, 9439, 9461, 9463, 9467, 9473, 9479, 9491, 9497, 9511, 9521, 9533, 9539, 9547, 9551, 9587, 9601, 9613, 9619, 9623, 9629, 9631, 9643, 9649, 9661, 9677, 9679, 9689, 9697, 9719, 9721, 9733, 9739, 9743, 9749, 9767, 9769, 9781, 9787, 9791, 9803, 9811, 9817, 9829, 9833, 9839, 9851, 9857, 9859, 9871, 9883, 9887, 9901, 9907, 9923, 9929, 9931, 9941, 9949, 9967, 9973)

def euler_criterion(a, p):
    """p is odd prime, a is positive integer. Euler's Criterion will check if
	a is a quadratic residue mod p. If yes, returns True. If a is a non-residue
	mod p, then False"""
    return pow(a, (p - 1) // 2, p) == 1

def gcd(a,b):
	"""gcd(a,b) returns the greatest common divisor of the integers a and b."""
	a = abs(a); b = abs(b)
	while (a > 0):
		b = b % a
		tmp=a; a=b; b=tmp
	return b

def xgcd(a,b):
	"""xgcd(a,b) returns a tuple of form (g,x,y), where g is gcd(a,b) and
	x,y satisfy the equation g = ax + by."""
	a1=1; b1=0; a2=0; b2=1; aneg=1; bneg=1
	if(a < 0):
		a = -a; aneg=-1
	if(b < 0):
		b = -b; bneg=-1
	while (1):
		quot = -(a // b)
		a = a % b
		a1 = a1 + quot*a2; b1 = b1 + quot*b2
		if(a == 0):
			return (b, a2*aneg, b2*bneg)
		quot = -(b // a)
		b = b % a;
		a2 = a2 + quot*a1; b2 = b2 + quot*b1
		if(b == 0):
			return (a, a1*aneg, b1*bneg)

def power_mod(b,e,n):
	"""power_mod(b,e,n) computes the eth power of b mod n.
	(Actually, this is not needed, as pow(b,e,n) does the same thing for positive integers.
	This will be useful in future for non-integers or inverses.)"""
	if e<0: # Negative powers can be computed if gcd(b,n)=1
		e = -e
		b = inverse_mod(b,n)
	accum = 1; i = 0; bpow2 = b
	while ((e>>i)>0):
		if((e>>i) & 1):
			accum = (accum*bpow2) % n
		bpow2 = (bpow2*bpow2) % n
		i+=1
	return accum

def inverse_mod(a,n):
	"""inverse_mod(b,n) - Compute 1/b mod n."""
	(g,xa,xb) = xgcd(a,n)
	if(g != 1): raise ValueError("***** Error *****: {0} has no inverse (mod {1}) as their gcd is {2}, not 1.".format(a,n,g))
	return xa % n

def is_prime(n):
	"""is_prime(n) - Test whether n is prime using a variety of pseudoprime tests."""
	if n<0: n=-n  # Only deal with positive integers
	if n<2: return False # 0 and 1 are not prime
	if (n in list_primes): return True
	return isprimeE(n,2) and isprimeE(n,3) and isprimeE(n,5)

def factor(n):
	"""factor(n) - Return a sorted list of the prime factors of n with exponents."""
	# Rewritten to align with SAGE.  Previous semantics available as factors(n).
	if ((abs(n) == 1) or (n == 0)): raise ValueError('Unable to factor {0}'.format(n))
	factspow = []
	currfact = None
	thecount = 1
	for thefact in factors(n):
		if thefact != currfact:
			if currfact != None:
				factspow += [(currfact,thecount)]
			currfact = thefact
			thecount = 1
		else:
			thecount += 1
	factspow += [(thefact,thecount)]
	return tuple(factspow)

def prime_divisors(n):
	"""prime_divisors(n) - Returns a sorted list of the prime divisors of n."""
	return tuple(set(factors(n)))

def euler_phi(n):
	"""euler_phi(n) - Computer Euler's Phi function of n - the number of integers
	strictly less than n which are coprime to n.  Otherwise defined as the order
	of the group of integers mod n."""
	if n == 1: return 1
	if n <= 0: return 0
	# For each prime factor p with multiplicity n, a factor of (p**(n-1))*(p-1)
	return functools.reduce(lambda a,x:a*(x[0]**(x[1]-1))*(x[0]-1),factor(n),1)

def carmichael_lambda(n):
	"""carmichael_lambda(n) - Compute Carmichael's Lambda function
	of n - the smallest exponent e such that b**e = 1 for all b coprime to n.
	Otherwise defined as the exponent of the group of integers mod n."""
	# SAGE equivalent is sage.crypto.util.carmichael_lambda(n)
	if n == 1: return 1
	if n <= 0: raise ValueError("*** Error ***:  Input n for carmichael_lambda(n) must be a positive integer.")
	# The gcd of (p**(e-1))*(p-1) for each prime factor p with multiplicity e (exception is p=2).
	def _carmichael_lambda_primepow(theprime,thepow):
		if ((theprime == 2) and (thepow >= 3)):
			return (2**(thepow-2)) # Z_(2**e) is not cyclic for e>=3
		else:
			return (theprime-1)*(theprime**(thepow-1))
	return functools.reduce(lambda accum,x:(accum*x)//gcd(accum,x),tuple(_carmichael_lambda_primepow(*primepow) for primepow in factor(n)),1)

def is_primitive_root(g,n):
	"""is_primitive_root(g,n) - Test whether g is primitive - generates the group of units mod n."""
	# SAGE equivalent is mod(g,n).is_primitive_root() in IntegerMod class
	if gcd(g,n) != 1: return False  # Not in the group of units
	order = euler_phi(n)
	if carmichael_lambda(n) != order: return False # Group of units isn't cyclic
	orderfacts = prime_divisors(order)
	for fact in orderfacts:
		if pow(g,order//fact,n) == 1: return False
	return True

def sqrtmod(a,n):
	"""sqrtmod(a,n) - Compute sqrt(a) mod n using various algorithms.
	Currently n must be prime, but will be extended to general n (when I get the time)."""
	# SAGE equivalent is mod(g,n).sqrt() in IntegerMod class
	if(not isprime(n)): raise ValueError("*** Error ***:  Currently can only compute sqrtmod(a,n) for prime n.")
	if(pow(a,(n-1)//2,n)!=1): raise ValueError("*** Error ***:  a is not quadratic residue, so sqrtmod(a,n) has no answer.")
	return TSRsqrtmod(a,n-1,n)

def TSRsqrtmod(a,grpord,p):
	"""TSRsqrtmod(a,grpord,p) - Compute sqrt(a) mod n using Tonelli-Shanks-RESSOL algorithm.
	Here integers mod n must form a cyclic group of order grpord."""
	# Rewrite group order as non2*(2^pow2)
	ordpow2=0; non2=grpord
	while(not ((non2&0x01)==1)):
		ordpow2+=1; non2//=2
	# Find 2-primitive g (i.e. non-QR)
	for g in range(2,grpord-1):
		if (pow(g,grpord//2,p)!=1):
			break
	g = pow(g,non2,p)
	# Tweak a by appropriate power of g, so result is (2^ordpow2)-residue
	gpow=0; atweak=a
	for pow2 in range(0,ordpow2+1):
		if(pow(atweak,non2*2**(ordpow2-pow2),p)!=1):
			gpow+=2**(pow2-1)
			atweak = (atweak * pow(g,2**(pow2-1),p)) % p
			# Assert: atweak now is (2**pow2)-residue
	# Now a*(g**powg) is in cyclic group of odd order non2 - can sqrt directly
	d = invmod(2,non2)
	tmp = pow(a*pow(g,gpow,p),d,p)  # sqrt(a*(g**gpow))
	return (tmp*inverse_mod(pow(g,gpow//2,p),p)) % p  # sqrt(a*(g**gpow))//g**(gpow//2)

################ Internally used functions #########################################

def isprimeF(n,b):
	"""isprimeF(n) - Test whether n is prime or a Fermat pseudoprime to base b."""
	return (pow(b,n-1,n) == 1)

def isprimeE(n,b):
	"""isprimeE(n) - Test whether n is prime or an Euler pseudoprime to base b."""
	if (not isprimeF(n,b)): return False
	r = n-1
	while (r % 2 == 0): r //= 2
	c = pow(b,r,n)
	if (c == 1): return True
	while (1):
		if (c == 1): return False
		if (c == n-1): return True
		c = pow(c,2,n)

def factorone(n):
	"""factorone(n) - Find a prime factor of n using a variety of methods."""
	if (is_prime(n)): return n
	for fact in list_primes:
		if n%fact == 0: return fact
	return factorPR(n)  # Needs work - no guarantee that a prime factor will be returned

def factors(n):
	"""factors(n) - Return a sorted list of the prime factors of n. (Prior to ver 0.7 named factor(n))"""
	if n<0: n=-n  # Only deal with positive integers
	if (is_prime(n)):
		return [n]
	fact = factorone(n)
	if ((abs(n) == 1) or (n == 0)): raise ValueError('Unable to factor \"{0}\"'.format(n))
	facts = factors(n//fact) + factors(fact)
	facts.sort()
	return facts

def factorPR(n):
	"""factorPR(n) - Find a factor of n using the Pollard Rho method.
	Note: This method will occasionally fail."""
	numsteps=2*math.floor(math.sqrt(math.sqrt(n)))
	for additive in range(1,5):
		fast=slow=1; i=1
		while i<numsteps:
			slow = (slow*slow + additive) % n
			i = i + 1
			fast = (fast*fast + additive) % n
			fast = (fast*fast + additive) % n
			g = gcd(fast-slow,n)
			if (g != 1):
				if (g == n):
					break
				else:
					return g
	return 1

################ Functions renamed in ver 0.7 (to align with SAGE) #################
def powmod(b,e,n):
	"""powmod(b,e,n) computes the eth power of b mod n. (Renamed power_mod(b,e,n) in ver 0.7)"""
	return power_mod(b,e,n)

def isprime(n):
	"""isprime(n) - Test whether n is prime using a variety of pseudoprime tests. (Renamed is_prime in ver 0.7)"""
	return is_prime(n)

def invmod(b,n):
	"""invmod(b,n) - Compute 1//b mod n. (Renamed inverse_mod(b,n) in ver 0.7)"""
	return inverse_mod(b,n)

def eulerphi(n):
    """eulerphi(n) - Compute Euler's Phi function of n - the number of integers strictly less than n which are coprime to n.
    (Renamed euler_phi(n) in ver 0.7)"""
    return euler_phi(n)

def carmichaellambda(n):
	"""carmichaellambda(n) - Compute Carmichael's Lambda function
	of n - the smallest exponent e such that b**e = 1 for all b coprime to n.
	Otherwise defined as the exponent of the group of integers mod n. (Renamed carmichael_lambda(n) in ver 0.7)"""
	return carmichael_lambda(n)

def isprimitive(g,n):
	"""isprimitive(g,n) - Test whether g is primitive - generates the group of units mod n. (Renamed is_primitive_root(g,n) in ver 0.8)"""
	# SAGE equivalent is mod(g,n).is_primitive_root() in IntegerMod class
	return is_primitive_root(g,n)

###############################################################
# Addiional functions: Salanitri Sergio
###############################################################


# mu(n): Calculate the mu function (0 is n divide a square, (-1)^k if not divive a square, k is the
# count of divisors of a)
def  mu(n):
    pass

#Calculate congruence a modulo n 
def mod(a,n):
    
    return Mod(a,n)
    
def is_mersenne_prime(p):
# There is a specialized test for primality of Mersenne numbers called the
# Lucas-Lehmer test. This remarkably simple algorithm determines provably
# correctly whether or not a number 2p − 1 is prime. We implement it in a
# few lines of code and use the Lucas-Lehmer test to check for primality of
# two Mersenne numbers.
# The main advantage of this algoritms is that the primes factors are not needed 
# If the last element os lucas-lehmer sequecy is 0 is a Mersenne prime if not, 
# only Mersenne number

   if lucas_lehmer_series(p)[-1] == 0:
        return True
   return False

#Function to generate lucas lehmer sequency
#n0 = 4
#ni = (ni-1) mod 2^p-1 (i = 1 to p-1)
def lucas_lehmer_series(p):
    seq = [4]
    if p>2:
        for i in range(1, (p-2)+1):
            n_i = ((seq[i-1]) ** 2 - 2) % ((2 ** p) - 1)
            seq.append(n_i)
    return  seq

def mersenne_number(p):
    return 2**p-1


############################################## 
#Cuadratic residues.
############################################## 

def is_square(n):
    pass


#Function to find whether number 'p' is prime or not
#This function is inefficient for large numbers.
def is_prime_elemental(number):
    if number <= 1 or (number > 2 and number % 2 == 0):
        return False
    
    for factor in range(2, int(math.sqrt(number))+1):
        if number%factor == 0:
            return False
    return True

# 26 Mar 2007 - ver 0.4
#   Correct error in xgcd().
# 27 Apr 2007 - ver 0.41
#   Correct error in Pollard Rho factoring algorithm.
# 1 Oct 2012 - ver 0.5
#   Changed xgcd() to correctly use true divide "//", rather than float divide "/"
# 24 Nov 2012 - ver 0.6
#   Add sqrtmod() function implementing Tonelli-Shanks-RESSOL.
#   Add invmod() function as a convenience wrapper for xgcd().
# 6 July 2014 - ver 0.7
#   Changed to use SAGE-like function names.
# 14 Oct 2014 - ver 0.8
#   Complete refactoring. Works with Python 2.5+ and 3.x.
# 18 Nov 2014 - ver 0.81
#   Changes to Pollard Rho factoring algorithm.
# 4 Sept 2018 - ver 0.82
#   Replace gcd() with non-recursive version (in corner cases hits Python recursion limit)
# 17 July 2019 - ver 0.83
#   Throw exception when asked to factor 0 or 1
# 25 July 2020
#    Add is_prime_lucas_lehmer(), mu(), mod(), legendre_symbol(), is_square()
############################################################################
# License: Freely available for use, abuse and modification
# (this is the Simplified BSD License, aka FreeBSD license)
# Copyright 2001-2019 Robert Campbell. All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
#    1. Redistributions of source code must retain the above copyright notice,
#       this list of conditions and the following disclaimer.
#
#    2. Redistributions in binary form must reproduce the above copyright
#       notice, this list of conditions and the following disclaimer in
#       the documentation and/or other materials provided with the distribution.
############################################################################
