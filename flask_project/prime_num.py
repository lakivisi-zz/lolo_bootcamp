def prime(i, primes):
    for prime in primes:
        if not (i == prime or i % prime):
            return False
    primes.add(i)
    return i
    
def get_n_primes(n):
    primes = set([])
    i, p = 2, 1

    if n < 2:
        return 'n should be 2 or more'
    while True:
        if prime(i, primes):
            p += 1
            if p == n:
                return list(primes)
        i += 1
        
