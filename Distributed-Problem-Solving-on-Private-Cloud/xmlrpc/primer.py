# segmented sieve

from math import *

def sumDigits(n):
	return sum(map(lambda x:x*x, map(int, (str(n)))))

def isHappy(n):
	history = set()
	while True:
		if n == 1:
			return True
		elif n in history:
			return False
		else:
			history.add(n)
		n = sumDigits(n)

def PrimeList(N):
	isPrime = [True for i in range(N+1)]
	isPrime[0] = isPrime[1] = False
	for i in range(2, int(sqrt(N))+1):
		if isPrime[i]:
			for j in range(i*i, N+1, i):
				isPrime[j] = False
	return filter(lambda x: isPrime[x], range(1, N+1))

def NumHappyPrimes(L, R):
	primes = PrimeList(int(sqrt(R)))
	isPrime = [1 for i in range(R-L+1)]
	if L == 1:
		isPrime[0] = 0
	for p in primes:
		j = (L//p)*p
		while j <= R:
			if j>1 and j>= L and j != p:
				isPrime[j-L] = 0
			j += p
	# ans = map(lambda x: x+L, filter(lambda x: isPrime[x], range(R-L+1)))
	# print ans
	for i in range(R-L+1):
		if isPrime[i]:
			if not isHappy(L+i):
				isPrime[i]=0
			# else:
			# 	print(L+i)
	res = sum(isPrime)
	print ("Answer to Query: " + str(res))
	return res

if __name__ == '__main__':
	MAX = 100
	print(NumHappyPrimes(1,MAX))
	# print PrimeList(MAX)