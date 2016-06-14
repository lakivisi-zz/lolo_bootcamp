
import math

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

def get_prime(n):
    primes = [2]
    current_no = 3
    div = math.sqrt(current_no)
    print int(div)
     
    while True:
            isPrime = True
            for prime in primes:
                for i in range(1,int(div)):
                        if current_no%i == 0:
                                isPrime = False
                                break
            if isPrime:
                    primes.append(current_no)
            current_no += 1
            if len(primes) == n:
                    break
    return primes

print get_prime(1)