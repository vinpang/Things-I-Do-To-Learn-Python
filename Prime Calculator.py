#1 - calculates primes and outputs numbers once e.g. 2^10 will output 2 10 times

import math
import time

def unique_primes(n):
    start = time.time()
    primes = []
    temp_n = n
    composite = 1

    while temp_n % 2 == 0:
        temp_n /= 2
        primes.append(2)
        composite *= 2

    for i in range(3,int(n/composite)+1,2): #+1 or we miss out 3 when it's the only prime factor left
        if temp_n == 1:
            break
        while temp_n % i == 0:
            temp_n /= i
            primes.append(i)
            composite *= i
    
    if not primes:
        primes.append(n)
    
    print(time.time() - start)
    return(primes)

print(unique_primes(36))
print(unique_primes(3072))
# print(unique_primes(910482103))

print(list(set()))