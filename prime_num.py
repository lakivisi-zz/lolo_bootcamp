
import math
# morris versiom
def get_primes(n):
    primes = [2]
    current_no = 3

    while True:
            isPrime = True
            for prime in primes:
                    if current_no%prime == 0:
                            isPrime = False
                            break
            if isPrime:
                    primes.append(current_no)
            current_no += 1
            if len(primes) == n:
                    break
    return primes

print get_primes(4)

#lolo's version
def prime(i, primes):
    for prime in primes:
        if not (i == prime or i % prime):
            return False
    primes.add(i)
    return i
    
def get_n_primes(n):
    primes = set([])
    i, p = 2, 1
    while True:
        if prime(i, primes):
            p += 1
            if p == n:
                return list(primes)
        i += 1
        
print get_n_primes(10)