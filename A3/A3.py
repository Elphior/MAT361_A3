import math

def euclid(a, b):
    x0, x1, y0, y1 = 1, 0, 0, 1

    while b != 0:
        q = a // b
        r = a % b
        print(f"{a} = {q} * {b} + {r}")
        a, b = b, r

        tempX = x0
        x0, x1 = x1, tempX - q * x1

        tempY = y0
        y0, y1 = y1, tempY - q * y1

    return a, x0, y0

def sieve(a, b):
    is_prime = [True] * (b + 1)
    is_prime[0] = is_prime[1] = False

    for i in range(2, int(math.sqrt(b)) + 1):
        if is_prime[i]:
            for j in range(i * i, b + 1, i):
                is_prime[j] = False

    primes = [i for i in range(a, b + 1) if is_prime[i]]
    return primes

def factorization(n):
    prime = sieve(0, 1000000)
    p, e = [], []
    current = n
    i = 0

    while i < len(prime):
        if current % prime[i] == 0:
            if prime[i] in p:
                index = p.index(prime[i])
                e[index] += 1
            else:
                p.append(prime[i])
                e.append(1)
            current //= prime[i]
        else:
            i += 1
            temp = prime[i] * prime[i]
            if temp > current:
                break

    if current > 1:
        p.append(current)
        e.append(1)

    return p, e

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1

    gcd, x1, y1 = extended_gcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y

def lineareqsolver(a, b, c):
    g = gcd(abs(a), abs(b))
    if c % g != 0:
        print("No integer solutions.")
        return
    a, b = abs(a), abs(b)
    g_extended, x0, y0 = extended_gcd(a, b)

    x0 *= c // g
    y0 *= c // g

    print(f"Initial solution: x = {x0}, y = {y0}")
    print("Other Solutions:")
    print(f"x = {b // g}t {'+ ' if (x0 > 0) else '- '}{abs(x0)}")
    print(f"y = {-a // g}t {'+ ' if (y0 > 0) else '- '}{abs(y0)}")

def multinv(a, m):
    gcd, x, y = extended_gcd(a, m)
    if gcd != 1:
        print("Inverse doesn't exist (a and m are not coprime).")
        return -1

    result = (x % m + m) % m
    return result

def modexp(a, x, m):
    result = 1
    a = a % m

    while x > 0:
        if x % 2 == 1:
            result = (result * a) % m
        x = x // 2
        a = (a * a) % m

    return result

def main():
    print("MAT361 Fall 2023: Week3 Program Compilation Python - Sungmin Moon")
    print("This program is uploaded in https://github.com/Elphior/MAT361_A3.git\n")
    print("Program #1: euclid(a, b)")
    print("Program #2: sieve(a, b)")
    print("Program #3: trialdivision(n)")
    print("Program #4: lineareqsolver(e)")
    print("Program #5: multinv(a, m)")
    print("Program #6: modexp(a, x, m)")
    select = int(input("Select which program to run: "))

    if select == 1:
        print("\nSelected Euclid")
        a = int(input("Enter a positive integer a: "))
        b = int(input("Enter a positive integer b: "))

        gcd_val, x, y = euclid(a, b)
        print(f"gcd({a}, {b}): {gcd_val}")
        print(f"{x} * {a} + {y} * {b} = {x * a + y * b}")
    elif select == 2:
        print("\nSelected Sieve of Eratosthenes")
        a = int(input("Enter a positive integer a: "))
        b = int(input("Enter a positive integer b: "))

        primes = sieve(a, b)
        print(*primes)
    elif select == 3:
        print("\nSelected Trial Division")
        n = int(input("Enter a positive integer n: "))

        p, e = factorization(n)
        print("p:", *p)
        print("e:", *e)
    elif select == 4:
        print("\nSelected Linear Equation Solver")
        print("ax + by = c")
        a = int(input("Enter value for a: "))
        b = int(input("Enter value for b: "))
        c = int(input("Enter value for c: "))

        lineareqsolver(a, b, c)
    elif select == 5:
        print("\nSelected multinv")
        a = int(input("Enter value for a: "))
        m = int(input("Enter value for m: "))

        inv = multinv(a, m)
        if inv != -1:
            print(f"multinv({a}, {m}) = {inv}")
    elif select == 6:
        print("\nSelected modexp")
        a = int(input("Enter value for a: "))
        x = int(input("Enter value for x: "))
        m = int(input("Enter value for m: "))

        result = modexp(a, x, m)
        print(f"{a}^{x} mod {m} = {result}")
    else:
        print("\nInvalid Input!")
        print("Terminating...")

if __name__ == "__main__":
    main()
