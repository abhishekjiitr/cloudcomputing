# segmented sieve

from math import *

def PrimeList(N):
	isPrime = [True for i in range(N+1)]
	isPrime[0] = isPrime[1] = False
	for i in range(2, int(sqrt(N))+1):
		if isPrime[i]:
			for j in range(i*i, N+1, i):
				isPrime[j] = False
	return filter(lambda x: isPrime[x], range(1, N+1))

def NumPrimes(L, R):
	primes = PrimeList(int(sqrt(R)))
	isPrime = [1 for i in range(R-L+1)]
	if L == 1:
		isPrime[0] = 0
	for p in primes:
		j = (L/p)*p
		while j <= R:
			if j>1 and j>= L and j != p:
				isPrime[j-L] = 0
			j += p
	# ans = map(lambda x: x+L, filter(lambda x: isPrime[x], range(R-L+1)))
	# print ans
	return sum(isPrime)

if __name__ == '__main__':
	MAX = 102
	print NumPrimes(1,MAX)
	print PrimeList(MAX)