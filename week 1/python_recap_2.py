def factors(n):
    factors_list = []

    for i in range(1, n+1):
        if (n % i) == 0:
            factors_list.append(i)

    return factors_list
    
def prime(n):
    return(factors(n) == [1,n])


def primesupto(m):
    prime_list = []
    for i in range(1, m + 1):
        if prime(i):
            prime_list.append(i)

    return prime_list


print(primesupto(100))