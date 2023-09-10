import sys

def sieve_of_eratosthenes(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    
    for p in range(2, int(n ** 0.5) + 1):
        if is_prime[p]:
            for i in range(p * p, n + 1, p):
                is_prime[i] = False
    
    return is_prime

max_upp_bnd = 1000000
is_prime = sieve_of_eratosthenes(max_upp_bnd)
prime_sums = [0] * ( max_upp_bnd+1)

curr_sum = 0
for i in range(2,max_upp_bnd+1):
    if is_prime[i]:
        curr_sum += i
    prime_sums[i] = curr_sum
        
t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(prime_sums[n])
