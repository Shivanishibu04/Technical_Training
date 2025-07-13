# Print prime numbers in range 1-N

# Naive solution
def isPrime(n):
    for i in range(2, n//2+1):
        if(n%i) == 0:
            return False
    return True

n = int(input("Enter number: "))

for i in range(2, n+1):
    if isPrime(i):
        print(i)

# Intermediate solution
def isPrime(n):
    for i in range(2, int(n*0.5) + 1):
        if n % i == 0:
            return False
    return True

def markMultiplesFalse(a, num, n):
    for j in range(a*2, n+1, a):
        num[j] = False

n = int(input("Enter number : "))
num = [True] * (n + 1)
num[0] = num[1] = False

for i in range(2, n + 1):
    if num[i]:
        if isPrime(i):
            print(i)
            markMultiplesFalse(i, num, n)

# Optimal solution
def markMultiplesFalse(a):
    p = 2*a + 3
    for j in range(2*a**2 + 6*a + 3, size, p):
        isPrime[j] = False

n = int(input("Enter number : "))
size = (n-3) // 2 + 1
isPrime = [True] * size
prime = [2]
for i in range(size):
    if isPrime[i]:
        prime.append(2*i+3)
        markMultiplesFalse(i)

print(len(prime))
