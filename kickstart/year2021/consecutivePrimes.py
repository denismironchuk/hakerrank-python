from math import sqrt

def isPrime(n):
    i = 2
    while i * i <= n:
        if (n % i == 0):
            return False
        i += 1

    return True

def findClosestLowerPrime(n):
    while (True):
        if isPrime(n):
            return n
        n -= 1

def findClosestUpperPrime(n):
    while (True):
        if isPrime(n):
            return n
        n += 1

if __name__ == '__main__':
    T = int(input())

    for t in range(1, T + 1):
        z = int(input())
        pivot = int(sqrt(z))

        primes = []

        if isPrime(pivot):
            primes.append(findClosestLowerPrime(pivot - 1))
            primes.append(pivot)
            primes.append(findClosestUpperPrime(pivot + 1))
        else:
            lowerPrime = findClosestLowerPrime(pivot)
            lower2Prime = findClosestLowerPrime(lowerPrime - 1)
            upperPrime = findClosestUpperPrime(pivot)

            primes.append(lower2Prime)
            primes.append(lowerPrime)
            primes.append(upperPrime)

        if (primes[1] * primes[2] <= z):
            print("Case #{}: {}".format(t, primes[1] * primes[2]))
        else:
            print("Case #{}: {}".format(t, primes[0] * primes[1]))

