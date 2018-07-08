def isPrime(number):
    for i in range(2, number):
        if number % i == 0:
            return False
    
    return True

primeNumbers = list(filter(isPrime, range(1, 100)))

print(primeNumbers)
