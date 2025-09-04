
#Computes largest common factor of two numbers

# def gcd(m, n):
#     cf = []
#     for i in range(1,min(m,n) + 1):
#         if (m % i) == 0 and (n % i) == 0:
#             cf.append(i)

#     return (cf[-1])

# print(gcd(100,25))


def gcd(m, n):
    for i in range(1, min(m, n) + 1):
        if (m % i) == 0 and (n % i) == 0:
            mrcf = i
    return mrcf

print(gcd(100,25))


# both will give same output